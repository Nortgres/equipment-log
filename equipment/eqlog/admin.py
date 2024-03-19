from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import Person, Equipment, Department, SettingID


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'middle_name', 'department', 'job_title', 'created_at', 'remote', 'city',
                    'is_working')
    list_display_links = ('id', 'last_name')
    search_fields = ('last_name', 'first_name')
    list_filter = ('is_working', 'remote', 'city', 'created_at',)
    prepopulated_fields = {"slug": ("last_name", )}


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'model', 'serial_number', 'id_number', 'sale_date', 'price', 'is_working', 'testing',
                    'description')
    list_display_links = ('id', 'type', 'model')
    search_fields = ('type', 'id_number')
    list_filter = ('is_working', 'sale_date', 'type', 'id_number',)
    prepopulated_fields = {"slug": ("id_number", )}


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(SettingID, SingletonModelAdmin)

