from django.forms import ModelForm, Select, TextInput, CheckboxSelectMultiple, RadioSelect
from basic.models import SubjectsModel
from registration.models import ClassesModel, StaffModel
from sparrow_admin.models import SchoolsModel


class SubjectForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        if 'school_pk' in kwargs.keys():
            school_pk = kwargs.pop('school_pk')
            super(SubjectForm, self).__init__(*args, **kwargs)
            user_school = SchoolsModel.objects.get(pk=school_pk)
            self.fields['teachers'].queryset = StaffModel.objects.filter(school=user_school)
        else:
            super(SubjectForm, self).__init__(*args, **kwargs)

    class Meta:
        model = SubjectsModel
        fields = '__all__'
        exclude = []
        widgets = {
            'school': TextInput(attrs={
                'class': 'form-control',
            }),
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the name of the subject',
                'autocomplete': 'off'
            }),
            'code': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a short code the subject',
                'autocomplete': 'off'
            }),
            'teachers': CheckboxSelectMultiple(attrs={

            })
        }


class ClassesForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        if 'school_pk' in kwargs.keys():
            school_pk = kwargs.pop('school_pk')
            super(ClassesForm, self).__init__(*args, **kwargs)
            user_school = SchoolsModel.objects.get(pk=school_pk)
            self.fields['form_teacher'].queryset = StaffModel.objects.filter(school=user_school)
            self.fields['assistant_form_teacher'].queryset = StaffModel.objects.filter(school=user_school)
            self.fields['subjects'].queryset = SubjectsModel.objects.filter(school=user_school)
        else:
            super(ClassesForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ClassesModel
        fields = '__all__'
        exclude = []
        widgets = {
            'school': TextInput(attrs={
                'class': 'form-control',
            }),
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the name of the class',
                'autocomplete': 'off'
            }),
            'code': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a short code the class',
                'autocomplete': 'off'
            }),
            'subjects': CheckboxSelectMultiple(attrs={

            }),
            'form_teacher': RadioSelect(attrs={

            }),
            'assistant_form_teacher': RadioSelect(attrs={

            })
        }


