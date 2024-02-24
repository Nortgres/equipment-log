from django.contrib import admin
from django.urls import path

from .views import about, login, persons, equipments, logout, EqlogHome, LoginUser, logout_user

urlpatterns = [
    path('', EqlogHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('persons/', persons, name='persons'),
#    path('addperson/', AddPerson.as_view(), name='addperson'),
#    path('persons/<slug:pers_slug>/', ShowPerson.as_view(), name='person'),
    path('equipments/', equipments, name='equipments'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]