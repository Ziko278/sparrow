from django.forms import ModelForm, Select, TextInput
from setting.models import SessionModel, SchoolAdminAcademicSettingModel
from sparrow_admin.models import SchoolsModel


class SessionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = SessionModel
        fields = '__all__'
        exclude = []
        widgets = {
            'school': TextInput(attrs={
                'class': 'form-control',
            }),
        }


class SchoolAdminAcademicSettingForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = SchoolAdminAcademicSettingModel
        fields = '__all__'
        exclude = []
        widgets = {
            'school': TextInput(attrs={
                'class': 'form-control',
            }),
        }
