from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

from eqlog.models import Person, Equipment


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class FilterPersonForm(forms.Form):
    last_name = forms.CharField(label='Фамилия', max_length=50, required=False)
    first_name = forms.CharField(label='Имя', max_length=50, required=False)


class AddPersonForm(forms.ModelForm):
    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.fields['group'].empty_label = 'Не выбрана'

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name.isalpha():
            raise ValidationError('Недопустимые символы')
        return first_name

    class Meta:
        model = Person
        fields = ['last_name', 'first_name', 'middle_name', 'department', 'job_title', 'jobing_at', 'remote', 'city',
                  'slug']

class AddEquipmentForm(forms.ModelForm):

    class Meta:
        model = Equipment
        #slug = {"slug": ("id_number", )}
        fields = ['type', 'model', 'serial_number', 'id_number', 'slug', 'sale_date', 'price', 'is_working', 'testing',
                  'person', 'description']