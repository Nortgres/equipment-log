from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .filters import PersonFilter
from .forms import LoginUserForm
from .models import Equipment, Person
from .utils import menu, DataMixin
from django.contrib.auth.mixins import LoginRequiredMixin

def about(request):
    return render(request, 'eqlog/about.html', {'menu': menu, 'title': 'О сайте'})

def persons(request):
    return HttpResponse("Сотрудники")

def equipments(request):
    return HttpResponse("Оборудование")
class EqlogHome(DataMixin, ListView):
    model = Person
    template_name = 'eqlog/index.html'
    context_object_name = 'persons'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        auth = self.request.user.is_authenticated
        queryset = self.get_queryset()
        p_filter = PersonFilter(self.request.GET, queryset)
        c_def = self.get_user_context(title='Главная страница', auth=auth, eq_filter=p_filter)
        return {**context, **c_def}


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'eqlog/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return {**context, **c_def}
    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')