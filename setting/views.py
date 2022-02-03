from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from setting.models import *
from setting.forms import *
from sparrow_admin.models import SchoolsModel


# Create your views here.
class SparrowSettingView(TemplateView):
    template_name = 'setting/sparrow_setting.html'


class SchoolSettingView(TemplateView):
    template_name = 'setting/school_setting.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=school_pk)
        academic_setting = SchoolAdminAcademicSettingModel.objects.filter(school=user_school)[:1]
        result_setting = SchoolAdminResultSettingModel.objects.filter(school=user_school)[:1]
        # print('academic_setting :', academic_setting.id)
        context['user_school'] = user_school
        context['academic_setting'] = academic_setting
        context['result_setting'] = result_setting
        return context


class SessionCreateView(SuccessMessageMixin, CreateView):
    model = SessionModel
    form_class = SessionForm
    template_name = 'session/create.html'
    success_message = 'Session Registered Successfully'

    def get_success_url(self):
        return reverse('admin_session_detail', kwargs={'pk': self.object.pk})


class SessionListView(ListView):
    model = SessionModel
    fields = '__all__'
    template_name = 'session/index.html'
    context_object_name = "session_list"


class SessionDetailView(DetailView):
    model = SessionModel
    fields = '__all__'
    template_name = 'session/detail.html'
    context_object_name = "session"


class SessionUpdateView(SuccessMessageMixin, UpdateView):
    model = SessionModel
    form_class = SessionForm
    template_name = 'session/edit.html'
    success_message = 'Session Information Successfully Updated'

    def get_success_url(self):
        return reverse('admin_session_detail', kwargs={'pk': self.object.pk})


class SessionDeleteView(SuccessMessageMixin, DeleteView):
    model = SessionModel
    fields = '__all__'
    template_name = 'session/delete.html'
    context_object_name = "session"
    success_url = "../index"
    success_message = 'Session Successfully Deleted'


class SchoolAcademicSettingCreateView(CreateView):
    model = SchoolAdminAcademicSettingModel
    form_class = SchoolAdminAcademicSettingForm
    template_name = 'setting/academic_setting/create.html'
    success_message = 'Academic Setting Saved Successfully'

    def get_success_url(self):
        return reverse('school_academic_setting_detail', kwargs={'pk': self.request.session['user_school_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=school_pk)
        context['user_school'] = user_school
        return context


class SchoolAcademicSettingUpdateView(UpdateView):
    model = SchoolAdminAcademicSettingModel
    form_class = SchoolAdminAcademicSettingForm
    template_name = 'setting/academic_setting/create.html'
    success_message = 'Academic Setting Saved Successfully'

    def get_success_url(self):
        return reverse('school_academic_setting_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=school_pk)
        context['user_school'] = user_school
        return context


class SchoolAcademicSettingDetailView(TemplateView):
    template_name = 'setting/academic_setting/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=school_pk)
        academic_setting = SchoolAdminAcademicSettingModel.objects.filter(school=user_school)[0]
        context['user_school'] = user_school
        context['academic_setting'] = academic_setting
        return context


class SchoolResultSettingCreateView(CreateView):
    model = SchoolAdminResultSettingModel
    form_class = SchoolAdminResultSettingForm
    template_name = 'setting/result_setting/create.html'
    success_message = 'Result Setting Saved Successfully'

    def get_success_url(self):
        return reverse('school_result_setting_detail', kwargs={'pk': self.request.session['user_school_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=school_pk)
        context['user_school'] = user_school
        return context


class SchoolResultSettingUpdateView(UpdateView):
    model = SchoolAdminResultSettingModel
    form_class = SchoolAdminResultSettingForm
    template_name = 'setting/result_setting/create.html'
    success_message = 'Result Setting Saved Successfully'

    def get_success_url(self):
        return reverse('school_result_setting_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=school_pk)
        context['user_school'] = user_school
        return context


class SchoolResultSettingDetailView(TemplateView):
    template_name = 'setting/result_setting/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_pk = self.request.session['user_school_id']
        user_school = SchoolsModel.objects.get(pk=school_pk)
        result_setting = SchoolAdminResultSettingModel.objects.filter(school=user_school)[0]
        print(result_setting.tests)
        context['user_school'] = user_school
        context['results_setting'] = result_setting
        return context
