from django import forms
from djexperience.utils.lists import GENDER
from .models import Customer, Employee, Provider


class CustomerForm(forms.ModelForm):
    gender = forms.ChoiceField(
        label='Sexo', choices=GENDER, initial='M', widget=forms.RadioSelect)

    class Meta:
        model = Customer
        fields = ['gender', 'treatment', 'first_name', 'last_name', 'email',
                  'slug', 'photo', 'birthday', 'occupation', 'company',
                  'department', 'cpf', 'rg', 'cnpj', 'ie',
                  'address', 'complement', 'district', 'city', 'uf', 'cep',
                  'active', 'blocked']

    def clean_cpf(self):
        return self.cleaned_data['cpf'] or None

    def clean_cnpj(self):
        return self.cleaned_data['cnpj'] or None


class EmployeeForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = ['username', 'email', 'password']

    def clean_cpf(self):
        return self.cleaned_data['cpf'] or None


class ProviderForm(forms.ModelForm):
    gender = forms.ChoiceField(
        label='Sexo', choices=GENDER, initial='M', widget=forms.RadioSelect)

    class Meta:
        model = Provider
        fields = '__all__'
