from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .filters import PersonFilter, EquipmentFilter
from .forms import LoginUserForm, FilterPersonForm, AddPersonForm, AddEquipmentForm
from .models import Equipment, Person, SettingID, Eqlog
from .utils import menu, DataMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.signals import pre_save
from django.dispatch import receiver


def about(request):
    return render(request, 'eqlog/about.html', {'menu': menu, 'title': 'О сайте'})


def home(request):
    return render(request, 'eqlog/index.html', {'menu': menu, 'title': 'Главная страница'})


def show_person(request, pers_slug):
    person = get_object_or_404(Person, slug=pers_slug)

    context = {
        'ps': person,
        'menu': menu,
    }
    return render(request, 'eqlog/person.html', context=context)


def show_equipment(request, equip_slug):
    equipment = get_object_or_404(Equipment, slug=equip_slug)

    context = {
        'eq': equipment,
        'menu': menu,
    }
    return render(request, 'eqlog/equipment.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('login')


def log_save_data(**kwargs):
    pass


@receiver(pre_save, sender=Equipment)
def track_field_changes(sender, instance, user=None, **kwargs):
    if instance.pk:
        old_instance = sender.objects.get(pk=instance.pk)
        for field in instance._meta.fields:
            if getattr(old_instance, field.attname) != getattr(instance, field.attname):
                if field.name == 'person':
                    old_val = old_instance.person
                    new_val = instance.person
                else:
                    old_val = getattr(old_instance, field.attname)
                    new_val = getattr(instance, field.attname)
                Eqlog.objects.create(
                    class_name=sender,
                    attr_name=field.verbose_name,
                    old_value=old_val,
                    new_value=new_val,
                    user=instance.user
                )


@receiver(pre_save, sender=Person)
def track_field_changes(sender, instance, user=None, **kwargs):
    if instance.pk:
        old_instance = sender.objects.get(pk=instance.pk)
        for field in instance._meta.fields:
            if getattr(old_instance, field.attname) != getattr(instance, field.attname):
                if field.name == 'department':
                    old_val = old_instance.department
                    new_val = instance.department
                else:
                    old_val = getattr(old_instance, field.attname)
                    new_val = getattr(instance, field.attname)
                Eqlog.objects.create(
                    class_name=sender,
                    attr_name=field.verbose_name,
                    old_value=old_val,
                    new_value=new_val,
                    user=instance.user
                )


class Persons(DataMixin, ListView):
    model = Person
    template_name = 'eqlog/persons.html'
    context_object_name = 'persons'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        auth = self.request.user.is_authenticated
        queryset = self.get_queryset()
        ps_filter = PersonFilter(self.request.GET, queryset)
        c_def = self.get_user_context(title='Сотрудники', auth=auth, ps_filter=ps_filter)
        return {**context, **c_def}

    def get_queryset(self):
        queryset = super().get_queryset()
        ps_filter = PersonFilter(self.request.GET, queryset)
        return ps_filter.qs


class AddPerson(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPersonForm
    template_name = 'eqlog/addperson.html'
    success_url = reverse_lazy('persons')
    login_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить сотрудника')
        return {**context, **c_def}

    def form_valid(self, form):
        person = form.save(commit=False)
        person.user = User.objects.get(username=self.request.user)
        person.save()
        return redirect(reverse('persons'))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'eqlog/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return {**context, **c_def}

    def get_success_url(self):
        return reverse_lazy('home')


class ShowPerson(DataMixin, DetailView):
    model = Person
    template_name = 'eqlog/person.html'
    slug_url_kwarg = 'pers_slug'
    context_object_name = 'ps'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        auth = self.request.user.is_authenticated
        c_def = self.get_user_context(title='Главная страница', auth=auth)
        person: Persons = context['object']
        context.update({"equipments": person.get_equipments.all()})
        return {**context, **c_def}


class UpdatePerson(LoginRequiredMixin, DataMixin, UpdateView):
    model = Person
    form_class = AddPersonForm
    template_name = 'eqlog/update_person.html'
    context_object_name = 'ps'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Изменить данные сотрудника')
        return {**context, **c_def}

    def form_valid(self, form):
        person = form.save(commit=False)
        person.user = User.objects.get(username=self.request.user)
        person.save()
        return redirect(reverse('persons'))


class Equipments(DataMixin, ListView):
    model = Equipment
    template_name = 'eqlog/equipments.html'
    context_object_name = 'equipments'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        auth = self.request.user.is_authenticated
        queryset = self.get_queryset()
        eq_filter = EquipmentFilter(self.request.GET, queryset)
        c_def = self.get_user_context(title='Оборудование', auth=auth, eq_filter=eq_filter)
        return {**context, **c_def}

    def get_queryset(self):
        queryset = super().get_queryset()
        eq_filter = EquipmentFilter(self.request.GET, queryset)
        return eq_filter.qs


class ShowEquipment(DataMixin, DetailView):
    model = Equipment
    template_name = 'eqlog/equipment.html'
    slug_url_kwarg = 'equip_slug'
    context_object_name = 'eq'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        auth = self.request.user.is_authenticated
        c_def = self.get_user_context(title='Главная страница', auth=auth)
        return {**context, **c_def}


def generate_in(request):
    if request.method == 'GET':
        setting_id = SettingID.objects.get()
        eq = Equipment()
        id_numbers_len = len(setting_id.prefix) + setting_id.id_l
        id_numbers = list(filter(lambda x: len(x) == id_numbers_len, eq.get_id_numbers))
        if len(id_numbers) > 0:
            num_current = []
            for i in id_numbers:
                if setting_id.prefix in i:
                    num = int(i.split(setting_id.prefix)[1])
                    num_current.append(num)
            if num_current:
                id_number_new = setting_id.prefix + (str((max(num_current))+1).zfill(setting_id.id_l))
            else:
                id_number_new = setting_id.prefix + str(1).zfill(setting_id.id_l)
        else:
            id_number_new = setting_id.prefix + str(1).zfill(setting_id.id_l)
        return JsonResponse({'inventory_number': id_number_new})


class AddEquipment(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddEquipmentForm
    template_name = 'eqlog/addequipment.html'
    success_url = reverse_lazy('equipments')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить оборудование')
        return {**context, **c_def}

    def form_valid(self, form):
        equipment = form.save(commit=False)
        equipment.user = User.objects.get(username=self.request.user)
        equipment.save()
        return redirect(reverse('equipments'))


class UpdateEquipment(LoginRequiredMixin, DataMixin, UpdateView):
    model = Equipment
    form_class = AddEquipmentForm
    template_name = 'eqlog/update_equipment.html'
    context_object_name = 'eq'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Изменить данные о оборудовании')
        return {**context, **c_def}

    def form_valid(self, form):
        equipment = form.save(commit=False)
        equipment.user = User.objects.get(username=self.request.user)
        equipment.save()
        return redirect(reverse('equipments'))


# class EqlogEquipments(DataMixin, ListView):
#    model = EqlogEquipment
#    template_name = 'eqlog/eqlogs.html'
#    context_object_name = 'log'

#    def get_context_data(self, *, object_list=None, **kwargs):
#        context = super().get_context_data(**kwargs)
#        auth = self.request.user.is_authenticated
#        c_def = self.get_user_context(title='Главная страница', auth=auth)
#        #field_name: log.field_name = context['object']
#        #context.update({"equipments": person.get_equipments.all()})
#        return {**context, **c_def}
