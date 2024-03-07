from django.contrib import admin
from django.urls import path

from .views import about, login, equipments, logout, PersonHome, LoginUser, logout_user, ShowPerson

urlpatterns = [
    path('', PersonHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('persons/', PersonHome.as_view(), name='persons'),
    path('person/<slug:pers_slug>/', ShowPerson.as_view(), name='person'),
#    path('addperson/', AddPerson.as_view(), name='addperson'),
    path('equipments/', equipments, name='equipments'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]