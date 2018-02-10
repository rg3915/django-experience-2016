from django import forms
from .models import Protest, Service, TypeService


class ProtestForm(forms.ModelForm):
    service = forms.ModelChoiceField(
        queryset=Service.objects.all(),
        label='Serviços',
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Protest
        fields = (
            'service',
            'typeservice',
            'description',
        )

    def __init__(self, *args, **kwargs):
        super(ProtestForm, self).__init__(*args, **kwargs)
        self.fields['typeservice'].queryset = TypeService.objects.none()

        if 'service' in self.data:
            try:
                service_id = int(self.data.get('service'))
                typeservice = TypeService.objects.filter(service_id=service_id)
                typeservice = typeservice.order_by('title')
                self.fields['typeservice'].queryset = typeservice
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            obj = self.instance.service.typeservice_set.order_by('title')
            self.fields['typeservice'].queryset = obj
