from django.shortcuts import render, redirect
from django.urls import reverse
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import StaffModel, ClassesModel, ParentsModel, StudentsModel
from registration.forms import StaffForm, ParentForm, StudentForm
from sparrow_admin.models import SchoolsModel
from basic.models import SubjectsModel


# Create your views here.
class StaffCreateView(SuccessMessageMixin, CreateView):
    model = StaffModel
    form_class = StaffForm
    template_name = 'staff/create.html'
    success_message = 'Staff Successfully Registered'

    def get_success_url(self):
        return reverse('school_admin_staff_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=pk)
        context['user_school'] = user_school
        return context


class StaffListView(ListView):
    model = StaffModel
    fields = '__all__'
    template_name = 'staff/index.html'
    context_object_name = "staff_list"

    def get_queryset(self):
        pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=pk)
        return StaffModel.objects.filter(school=user_school)


class StaffDetailView(DetailView):
    model = StaffModel
    fields = '__all__'
    template_name = 'staff/detail.html'
    context_object_name = "staff"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=pk)
        subjects = SubjectsModel.objects.filter(teachers=self.object, school=user_school)
        class_form_teacher = ClassesModel.objects.filter(form_teacher=self.object, school=user_school)
        class_assistant_form_teacher = ClassesModel.objects.filter(assistant_form_teacher=self.object, school=user_school)
        context['user_school'] = user_school
        context['teacher_subject_list'] = subjects
        context['class_form_teacher'] = class_form_teacher
        context['class_assistant_form_teacher'] = class_assistant_form_teacher
        return context


class StaffUpdateView(SuccessMessageMixin, UpdateView):
    model = StaffModel
    form_class = StaffForm
    template_name = 'staff/edit.html'
    success_message = 'Staff Information Successfully Updated'

    def get_success_url(self):
        return reverse('school_admin_staff_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.session['user_school_id']
        subject_pk = self.kwargs.get('pk')
        user_school = SchoolsModel.objects.get(pk=pk)
        context['user_school'] = user_school
        return context


class StaffDeleteView(SuccessMessageMixin, DeleteView):
    model = StaffModel
    fields = '__all__'
    template_name = 'staff/delete.html'
    context_object_name = "staff"
    success_url = "../index"
    success_message = 'Staff Successfully Deleted'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=school_pk)
        staff_pk = self.kwargs.get('pk')
        staff = StaffModel.objects.get(pk=staff_pk)
        form_teacher = ClassesModel.objects.filter(form_teacher=staff)
        assistant_form_teacher = ClassesModel.objects.filter(assistant_form_teacher=staff)
        subject_list = SubjectsModel.objects.filter(school=user_school, teachers__in=[staff])
        context['user_school'] = user_school
        context['form_teacher'] = form_teacher
        context['subject_list'] = subject_list
        context['assistant_form_teacher'] = assistant_form_teacher
        return context


class ParentCreateView(SuccessMessageMixin, CreateView):
    model = ParentsModel
    form_class = ParentForm
    template_name = 'parent/create.html'
    success_message = 'Parent Registration Successful'

    def get_success_url(self):
        return reverse('school_admin_parent_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=pk)
        context['user_school'] = user_school
        return context


class ParentListView(ListView):
    model = ParentsModel
    fields = '__all__'
    template_name = 'parent/index.html'
    context_object_name = "parent_list"

    def get_queryset(self):
        pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=pk)
        return ParentsModel.objects.filter(school=user_school)


class ParentDetailView(DetailView):
    model = ParentsModel
    fields = '__all__'
    template_name = 'parent/detail.html'
    context_object_name = "parent"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_pk = self.request.session['user_school_id']
        parent_pk = self.kwargs.get('pk')
        parent = ParentsModel.objects.get(pk=parent_pk)
        user_school = SchoolsModel.objects.get(pk=school_pk)
        student_list = StudentsModel.objects.filter(parent=parent)
        context['user_school'] = user_school
        context['student_list'] = student_list
        return context


class ParentDeleteView(DeleteView):
    model = ParentsModel
    fields = '__all__'
    template_name = 'parent/delete.html'
    context_object_name = "parent"
    success_url = "../index"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=school_pk)
        parent_pk = self.kwargs.get('pk')
        parent = ParentsModel.objects.get(pk=parent_pk)
        student_list = StudentsModel.objects.filter(school=user_school, parent=parent)
        context['user_school'] = user_school
        context['student_list'] = student_list
        return context


class ParentUpdateView(SuccessMessageMixin, UpdateView):
    model = ParentsModel
    form_class = ParentForm
    template_name = 'parent/edit.html'
    success_message = 'Parent Information Successfully Updated'

    def get_success_url(self):
        return reverse('school_admin_parent_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=pk)
        context['user_school'] = user_school
        return context


class StudentCreateView(SuccessMessageMixin, CreateView):
    model = StudentsModel
    form_class = StudentForm
    template_name = 'student/create.html'
    success_message = 'Student Successfully Registered'

    def get_success_url(self):
        return reverse('school_admin_student_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, *args, **kwargs):
        return super(StudentCreateView, self).dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(StudentCreateView, self).get_form_kwargs()
        kwargs.update({'school_pk': self.request.session['user_school_id']})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_pk = self.request.session['user_school_id']
        parent_pk = self.kwargs.get('parent_pk')
        user_school = SchoolsModel.objects.get(pk=school_pk)
        student_parent = ParentsModel.objects.get(pk=parent_pk)
        context['user_school'] = user_school
        context['student_parent'] = student_parent
        return context


class StudentListView(ListView):
    model = StudentsModel
    fields = '__all__'
    template_name = 'student/index.html'
    context_object_name = "student_list"

    def get_queryset(self):
        pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=pk)
        return StudentsModel.objects.filter(school=user_school)


class StudentDetailView(DetailView):
    model = StudentsModel
    fields = '__all__'
    template_name = 'student/detail.html'
    context_object_name = "student"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=pk)
        context['user_school'] = user_school
        return context


class StudentDeleteView(SuccessMessageMixin, DeleteView):
    model = StudentsModel
    fields = '__all__'
    template_name = 'student/delete.html'
    context_object_name = "student"
    success_url = "../index"
    success_message = 'Student Successfully Deleted'


class StudentUpdateView(SuccessMessageMixin, UpdateView):
    model = StudentsModel
    form_class = StudentForm
    template_name = 'student/edit.html'
    success_message = 'Student Information Successfully Updated'

    def get_success_url(self):
        return reverse('school_admin_student_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, *args, **kwargs):
        return super(StudentUpdateView, self).dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(StudentUpdateView, self).get_form_kwargs()
        kwargs.update({'school_pk': self.request.session['user_school_id']})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_pk = self.request.session['user_school_id']
        student_parent = self.object.parent
        user_school = SchoolsModel.objects.get(pk=school_pk)
        context['user_school'] = user_school
        context['student_parent'] = student_parent
        return context


def student_check_parent_view(request):
    if request.method == 'POST':
        school_id = request.POST['school']
        student_class = request.POST['class']
        subject = request.POST['subject']
        request.session['result_class'] = student_class
        request.session['result_subject'] = subject
        return redirect(reverse('school_admin_result_upload'))

    school_pk = request.session['user_school_id']
    user_school = SchoolsModel.objects.get(pk=school_pk)
    parent_list = ParentsModel.objects.filter(school=user_school)
    parent_list = serializers.serialize("json", parent_list)

    context = {
        'user_school': user_school,
        'parent_list': parent_list,
    }
    return render(request, 'student/check_parent.html', context=context)

