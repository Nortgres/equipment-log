from django.contrib import admin
from django.urls import path

from .views import about, login, logout, PersonHome, LoginUser, logout_user, ShowPerson, Equipments, \
    ShowEquipment, AddPerson, home, UpdatePerson, AddEquipment, UpdateEquipment

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('persons/', PersonHome.as_view(), name='persons'),
    path('addperson/', AddPerson.as_view(), name='addperson'),
    path('person/<slug:pers_slug>/', ShowPerson.as_view(), name='person'),
    #path('person/<int:pk>/disable/', DisablePerson.as_view(), name="disable_person"),
    path('person/<int:pk>/update/', UpdatePerson.as_view(), name='update_person'),
    path('equipments/', Equipments.as_view(), name='equipments'),
    path('add_equipment/', AddEquipment.as_view(), name='add_equipment'),
    path('equipment/<slug:equip_slug>/', ShowEquipment.as_view(), name='equipment'),
    path('equipment/<int:pk>/update/', UpdateEquipment.as_view(), name='update_equipment'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]