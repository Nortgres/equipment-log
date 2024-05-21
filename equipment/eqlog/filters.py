from django_filters import FilterSet, DateFilter, CharFilter
from .models import Person, Equipment, Department


class PersonFilter(FilterSet):
    start_date = DateFilter(field_name='jobing_at', lookup_expr='gte')
    end_date = DateFilter(field_name='jobing_at', lookup_expr='lte')
    last_name = CharFilter(field_name='last_name', lookup_expr='contains', label='Фамилия')
    first_name = CharFilter(field_name='first_name', lookup_expr='contains', label='Имя')
    department = Person.objects.filter(department__name='name')
    job_title = CharFilter(field_name='job_title', lookup_expr='contains', label='Должность')

    class Meta:
        model = Person
        fields = ['last_name', 'first_name', 'department', 'job_title']


class EquipmentFilter(FilterSet):
    start_date = DateFilter(field_name='sale_date', lookup_expr='gte')
    end_date = DateFilter(field_name='sale_date', lookup_expr='lte')
    type = CharFilter(field_name='type', lookup_expr='contains', label='Тип оборудования')
    model = CharFilter(field_name='model', lookup_expr='contains', label='Модель')
    id_number = CharFilter(field_name='id_number', lookup_expr='contains', label='Инвентарный номер')
    testing = CharFilter(field_name='testing', lookup_expr='contains', label='Доступно для тестирования')

    class Meta:
        model = Equipment
        fields = ['type', 'model', 'id_number', 'testing']