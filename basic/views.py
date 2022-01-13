from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from basic.models import SubjectsModel
from basic.forms import SubjectForm, ClassesForm
from registration.models import ClassesModel, StaffModel, StudentsModel


from sparrow_admin.models import SchoolsModel


# Create your views here.
class SubjectCreateView(CreateView):
    model = SubjectsModel
    form_class = SubjectForm
    template_name = 'subject/create.html'

    def get_success_url(self):
        return reverse('school_admin_subject_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=pk)
        context['user_school'] = user_school
        return context


class SubjectListView(ListView):
    model = SubjectsModel
    fields = '__all__'
    template_name = 'subject/index.html'
    context_object_name = "subject_list"

    def get_queryset(self):
        pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=pk)
        return SubjectsModel.objects.filter(school=user_school)


class SubjectDetailView(DetailView):
    model = SubjectsModel
    fields = '__all__'
    template_name = 'subject/detail.html'
    context_object_name = "subject"


class SubjectDeleteView(DeleteView):
    model = SubjectsModel
    fields = '__all__'
    template_name = 'subject/delete.html'
    context_object_name = "subject"
    success_url = "../index"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.session['user_school_id']
        subject_pk = self.kwargs.get('pk')
        user_school = SchoolsModel.objects.get(pk=pk)
        subject = SubjectsModel.objects.get(pk=subject_pk)
        class_list = ClassesModel.objects.filter(school=user_school, subjects__in=[subject])
        context['user_school'] = user_school
        context['class_list'] = class_list
        return context


class SubjectUpdateView(UpdateView):
    model = SubjectsModel
    form_class = SubjectForm
    template_name = 'subject/edit.html'

    def get_success_url(self):
        return reverse('school_admin_subject_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=pk)
        context['user_school'] = user_school
        return context


class SubjectAssignTeachersView(UpdateView):
    model = SubjectsModel
    form_class = SubjectForm
    template_name = 'subject/assign_teacher.html'

    def get_success_url(self):
        return reverse('school_admin_subject_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, *args, **kwargs):
        return super(SubjectAssignTeachersView, self).dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(SubjectAssignTeachersView, self).get_form_kwargs()
        kwargs.update({'school_pk': self.request.session['user_school_id']})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=pk)
        staff = StaffModel.objects.filter(school=user_school)
        context['user_school'] = user_school
        context['staff'] = staff
        context['pk'] = user_school
        return context


class SubjectStatisticsView(TemplateView):
    template_name = 'subject/statistic.html'


class ClassCreateView(CreateView):
    model = ClassesModel
    form_class = ClassesForm
    template_name = 'class/create.html'

    def get_success_url(self):
        return reverse('school_admin_class_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=pk)
        context['user_school'] = user_school
        return context


class ClassListView(ListView):
    model = ClassesModel
    fields = '__all__'
    template_name = 'class/index.html'
    context_object_name = "class_list"

    def get_queryset(self):
        pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=pk)
        return ClassesModel.objects.filter(school=user_school)


class ClassDetailView(DetailView):
    model = ClassesModel
    fields = '__all__'
    template_name = 'class/detail.html'
    context_object_name = "class"


class ClassUpdateView(UpdateView):
    model = ClassesModel
    form_class = ClassesForm
    template_name = 'class/edit.html'

    def get_success_url(self):
        return reverse('school_admin_class_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=pk)
        context['user_school'] = user_school
        return context


class ClassDeleteView(DeleteView):
    model = ClassesModel
    fields = '__all__'
    template_name = 'class/delete.html'
    context_object_name = "class"
    success_url = "../index"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_pk = self.request.session['user_school_id']
        class_pk = self.kwargs.get('pk')
        user_school = SchoolsModel.objects.get(pk=school_pk)
        student_class = ClassesModel.objects.get(pk=class_pk)
        class_student = StudentsModel.objects.filter(school=user_school, student_class=student_class).count()
        context['user_school'] = user_school
        context['class_student'] = class_student
        return context


class ClassAssignSubjectsView(UpdateView):
    model = ClassesModel
    form_class = ClassesForm
    template_name = 'class/assign_subject.html'

    def get_success_url(self):
        return reverse('school_admin_class_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, *args, **kwargs):
        return super(ClassAssignSubjectsView, self).dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(ClassAssignSubjectsView, self).get_form_kwargs()
        kwargs.update({'school_pk': self.request.session['user_school_id']})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=pk)
        context['user_school'] = user_school
        return context


class ClassAssignTeacherView(UpdateView):
    model = ClassesModel
    form_class = ClassesForm
    template_name = 'class/assign_teacher.html'

    def get_success_url(self):
        return reverse('school_admin_class_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, *args, **kwargs):
        return super(ClassAssignTeacherView, self).dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(ClassAssignTeacherView, self).get_form_kwargs()
        kwargs.update({'school_pk': self.request.session['user_school_id']})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=pk)
        context['user_school'] = user_school
        return context
