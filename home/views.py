from django.shortcuts import render
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from sparrow_admin.views import SchoolsModel
from sparrow_admin.forms import SchoolsForm
from home.models import WebsiteInfoModel


# Create your views here.
class WebsiteHome(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['site_info'] = WebsiteInfoModel.objects.get(pk=1)
        except WebsiteInfoModel.DoesNotExist:
            context['site_info'] = None
        return context


class WebsiteAbout(TemplateView):
    template_name = 'about_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['site_info'] = WebsiteInfoModel.objects.get(pk=1)
        except WebsiteInfoModel.DoesNotExist:
            context['site_info'] = None
        return context


class WebsiteContact(TemplateView):
    template_name = 'contact_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['site_info'] = WebsiteInfoModel.objects.get(pk=1)
        except WebsiteInfoModel.DoesNotExist:
            context['site_info'] = None
        return context


class WebsiteProduct(TemplateView):
    template_name = 'our_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['site_info'] = WebsiteInfoModel.objects.get(pk=1)
        except WebsiteInfoModel.DoesNotExist:
            context['site_info'] = None
        return context


class WebsiteService(TemplateView):
    template_name = 'our_services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['site_info'] = WebsiteInfoModel.objects.get(pk=1)
        except WebsiteInfoModel.DoesNotExist:
            context['site_info'] = None
        return context


class SchoolsDashboard(TemplateView):
    template_name = 'school_admin_dashboard.html'


class SchoolsRegister(SuccessMessageMixin, CreateView):
    template_name = 'school_register.html'
    model = SchoolsModel
    form_class = SchoolsForm
    template_name = 'register_school.html'
    success_url = 'registration/successful'
    success_message = "REGISTRATION SUCCESSFUL, AN ACTIVATION MESSAGE WOULD BE SENT TO" \
                      "THE SCHOOL'S EMAIL ONCE YOUR APPLICATION IS APPROVED, THIS MAY TAKE FEW HOURS"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['site_info'] = WebsiteInfoModel.objects.get(pk=1)
        except WebsiteInfoModel.DoesNotExist:
            context['site_info'] = None
        return context


class SchoolsRegisterSuccess(TemplateView):
    template_name = 'school_register_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['site_info'] = WebsiteInfoModel.objects.get(pk=1)
        except WebsiteInfoModel.DoesNotExist:
            context['site_info'] = None
        return context


