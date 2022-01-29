from django.forms import ModelForm, Select, TextInput
from .models import SchoolsModel


class SchoolsForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = SchoolsModel
        fields = '__all__'
        exclude = ["status", "registration_date", "activation_date"]



