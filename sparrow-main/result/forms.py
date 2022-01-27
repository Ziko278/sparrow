from django.forms import ModelForm, Select, TextInput
from result.models import ResultModel


class ResultForm(ModelForm):
    """"""
    class Meta:
        model = ResultModel
        fields = '__all__'
        exclude = []
        widgets = {
            'school': TextInput(attrs={
                'class': 'form-control',
            }),
            'student_class': TextInput(attrs={
                'class': 'form-control',
            })
        }

