from django import forms
from .models import Customer, Book


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'birthday']

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        prepositions = ['da', 'de', 'di', 'do', 'du']
        words = list(map(lambda w: w.capitalize()
                         if not w in prepositions else w, first_name.split()))
        return ' '.join(words)

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        prepositions = ['da', 'de', 'di', 'do', 'du']
        words = list(map(lambda w: w.capitalize()
                         if not w in prepositions else w, last_name.split()))
        return ' '.join(words)


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['name', 'authors']
