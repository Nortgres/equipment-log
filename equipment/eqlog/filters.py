from django_filters import FilterSet, DateFilter, CharFilter
from .models import Person


class PersonFilter(FilterSet):
    start_date = DateFilter(field_name='created_at', lookup_expr='gte')
    end_date = DateFilter(field_name='created_at', lookup_expr='lte')
    last_name = CharFilter(field_name='last_name', lookup_expr='contains', label='Фамилия')
    first_name = CharFilter(field_name='first_name', lookup_expr='contains', label='Имя')
#    middle_name = CharFilter(field_name='middle_name', lookup_expr='contains', label='Отчество')
#    department = CharFilter(field_name='department', lookup_expr='contains', label='Отдел')
#    job_title = CharFilter(field_name='job_title', lookup_expr='contains', label='Должность')

    class Meta:
        model = Person
        fields = ['last_name', 'first_name', 'middle_name', 'department', 'job_title']