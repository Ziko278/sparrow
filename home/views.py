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


def send_message(request):
    if request.method == "POST":
        message_name = request.POST['name']
        if request.user.is_authenticated:
            message_email = request.user.email
        else:
            message_email = request.POST['email']
        message = request.POST['message']
        subject = request.POST['subject']
        fro = settings.EMAIL_HOST_USER
        name = f"{request.user.first_name} {request.user.last_name}"
        to = ['leoklems@aol.com']

        vars = {
            'message': message,
            'email': message_email,
            'name': name,
        }
        html_content = render_to_string('contact_us_message.html', vars)

        send_mail(
            subject=message_name,  # subject
            message=message,  # message
            from_email=fro,  # from email
            recipient_list=to,  # to email or emails
            html_message=html_content,

        )
        messages.success(request, 'Thanks ' + message_email + ',\n We received your mail and will respond shortly')
        try:
            site = WebsiteInfoModel.objects.get(pk=1)
            email = site.site_info
        except WebsiteInfoModel.DoesNotExist:
            email = None

        context = {
            'email': email,
        }

        return render(request, 'contact_us.html', context)
    else:
        try:
            site = WebsiteInfoModel.objects.get(pk=1)
            email = site.site_info
        except WebsiteInfoModel.DoesNotExist:
            email = None

        context = {
            'email': email,
        }
        return render(request, 'contact_us.html', context)


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

    def get(self, *args, **kwargs):
        school = SchoolsModel.objects.get(pk=self.request.user.id)
        # slides = Slide.objects.all()
        # depts = Department.objects.all().order_by('name')
        # announcements = Announcement.objects.all()
        # events = Event.objects.all()

        context = {
            # 'posts': posts,
            # 'slides': slides,
            # 'depts': depts,
            # 'announcements': announcements,
            # 'events': events,
        }

        return render(self.request, 'school/school_admin_dashboard.html', context)


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
    template_name = 'school/school_register_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['site_info'] = WebsiteInfoModel.objects.get(pk=1)
        except WebsiteInfoModel.DoesNotExist:
            context['site_info'] = None
        return context


