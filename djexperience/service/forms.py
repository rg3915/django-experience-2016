from django import forms
from .models import Protest, Service


class ProtestForm(forms.ModelForm):
    service = forms.ModelChoiceField(
        queryset=None,
        label='Serviços',
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Protest
        fields = (
            'service',
            'typeservice',
            'councilman',
            'description',
        )

    def __init__(self, *args, **kwargs):
        super(ProtestForm, self).__init__(*args, **kwargs)
        self.fields['service'].queryset = Service.objects.all()
