from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from sparrow_admin.models import SchoolsModel
from sparrow_admin.forms import SchoolsForm
from home.forms import WebsiteInfoForm
from home.models import WebsiteInfoModel


# Create your views here.
class Dashboard(TemplateView):
    """This is the view for the super admin of sparrow"""
    template_name = 'dashboard.html'


class SchoolDashboard(TemplateView):
    """This is the view for the super admin of sparrow"""
    template_name = 'school_dashboard.html'


class SchoolCreateView(CreateView):
    model = SchoolsModel
    form_class = SchoolsForm
    template_name = 'school/create.html'
    success_url = "index"


class SchoolListView(ListView):
    model = SchoolsModel
    fields = '__all__'
    template_name = 'school/index.html'
    context_object_name = "school_list"


class SchoolDetailView(DetailView):
    model = SchoolsModel
    fields = '__all__'
    template_name = 'school/detail.html'
    context_object_name = "school"


class SchoolUpdateView(UpdateView):
    model = SchoolsModel
    fields = '__all__'
    template_name = 'school/edit.html'
    success_url = "../index"


def school_update_status(request, pk):
    """"""
    school = SchoolsModel.objects.get(pk=pk)
    school.status = 'active'
    school.save()
    return redirect('../'+str(pk)+'/detail')


class SchoolNewListView(ListView):
    model = SchoolsModel
    queryset = SchoolsModel.objects.filter(status="new")
    fields = '__all__'
    template_name = 'school/new.html'
    context_object_name = "school_list"


class SchoolStatisticsView(TemplateView):
    template_name = 'school/statistic.html'


class WebsiteInfoCreateView(CreateView):
    model = WebsiteInfoModel
    form_class = WebsiteInfoForm
    template_name = 'website_info/create.html'
    success_url = "info/1/detail"


class WebsiteInfoDetailView(DetailView):
    model = WebsiteInfoModel
    fields = '__all__'
    template_name = 'website_info/detail.html'
    context_object_name = "school"


class WebsiteInfoUpdateView(UpdateView):
    model = WebsiteInfoModel
    form_class = WebsiteInfoForm
    template_name = 'website_info/edit.html'
    success_url = "detail"
