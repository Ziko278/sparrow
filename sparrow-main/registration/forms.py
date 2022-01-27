from django.forms import ModelForm, Select, TextInput
from registration.models import StaffModel, ParentsModel, StudentsModel, ClassesModel
from sparrow_admin.models import SchoolsModel


class StaffForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = StaffModel
        fields = '__all__'
        exclude = []
        widgets = {
            'school': TextInput(attrs={
                'class': 'form-control',
            }),
        }


class ParentForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = ParentsModel
        fields = '__all__'
        exclude = []
        widgets = {
            'school': TextInput(attrs={
                'class': 'form-control',
            })
        }


class StudentForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        school_pk = kwargs.pop('school_pk')
        super(StudentForm, self).__init__(*args, **kwargs)
        user_school = SchoolsModel.objects.get(pk=school_pk)
        self.fields['student_class'].queryset = ClassesModel.objects.filter(school=user_school)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = StudentsModel
        fields = '__all__'
        exclude = []
        widgets = {
            'school': TextInput(attrs={
                'class': 'form-control',
            })
        }
