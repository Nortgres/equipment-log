from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .filters import PersonFilter, EquipmentFilter
from .forms import LoginUserForm, FilterPersonForm
from .models import Equipment, Person
from .utils import menu, DataMixin
from django.contrib.auth.mixins import LoginRequiredMixin


def about(request):
    return render(request, 'eqlog/about.html', {'menu': menu, 'title': 'О сайте'})


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


class PersonHome(DataMixin, ListView):
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
        return {**context, **c_def}

def logout_user(request):
    logout(request)
    return redirect('login')


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
