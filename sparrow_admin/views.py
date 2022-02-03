from django.conf import settings
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .utils import token_generator
from django.contrib import messages
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import SchoolsModel
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


def random_int():
    random_ref = randint(0, 9999999999)
    uid = random_ref
    return uid


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

    def get_context_data(self, **kwargs):
        school=SchoolsModel.objects.all()
        context = super().get_context_data(**kwargs)
        try:
            context['school_filter'] = SchoolFilter(self.request.GET, queryset=school)
        except WebsiteInfoModel.DoesNotExist:
            context['school_filter'] = None
        return context


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
    # school.status = 'active'
    # school.save()
    email = school.email

    exists = False
    try:
        email = school.email
        exists = True
    except ObjectDoesNotExist:
        pass
    if exists:
        # user.is_active = False
        # user.save()
        domain = get_current_site(request).domain
        uidb68 = urlsafe_base64_encode(force_bytes(school.pk))
        link = reverse('s_admin:activate', kwargs={'uidb64': uidb68, 'token': token_generator.make_token(school)})
        activate_url = 'http://' + domain + link
        print(activate_url)
        email_subject = "Activate your account"
        fro = settings.EMAIL_HOST_USER
        email_body = "Hi " + school.applicant_name + " please use this link to verify your account " + activate_url
        # print(email_body)
        email = EmailMessage(
            email_subject,
            email_body,
            # email_body,
            fro,
            [email],
        )
        email.send(fail_silently=False)

        # inactive_user = send_verification_email(request,form)
        messages.success(request, 'Account was created for ' + school + ' proceed to your email to activate')

        return redirect('admin_school_list')
    else:
        messages.success(request, 'This school email has already been registered, try another email')

        return redirect('admin_new_school_list')


class VerificationView(View):
    def get(self, request, uidb64, token):
        uid = urlsafe_base64_decode(uidb64).decode()
        school = SchoolsModel.objects.get(pk=uid)
        if school is not None and token_generator.check_token(school, token):
            school.status = 'active'
            school.save()
            login(request, school)
            messages.success(request, 'Thank you for your email confirmation. '
                                      'Now your school account has been activated, '
                                      'you can start using the platform. Thanks')
            return redirect('user:login')
        else:
            messages.success(request, 'Activation link is invalid!')
            return redirect("user:login")


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


# def send_message(request):
#     if request.method == "POST":
#         message_name = request.POST['message-name']
#         if request.user.is_authenticated:
#             message_email = request.user.email
#         else:
#             message_email = request.POST['message-email']
#         message = request.POST['message']
#         fro = settings.EMAIL_HOST_USER
#         name = f"{request.user.first_name} {request.user.last_name}"
#         to = ['leoklems@aol.com']
#
#         vars = {
#             'message': message,
#             'email': message_email,
#             'name': name,
#         }
#         html_content = render_to_string('contact_us_message.html', vars)
#
#         send_mail(
#             subject=message_name,  # subject
#             message=message,  # message
#             from_email=fro,  # from email
#             recipient_list=to,  # to email or emails
#             html_message=html_content,
#
#         )
#         messages.success(request, 'Thanks ' + message_email + ',\n We received your mail and will respond shortly')
#         depts = Department.objects.all()
#
#         context = {
#             'depts': depts,
#         }
#
#         return render(request, 'contact-us.html', context)
#     else:
#         depts = Department.objects.all().order_by('name')
#
#         context = {
#             'depts': depts,
#         }
#
#         return render(request, 'contact-us.html', context)
#
# def activate():
#     if form.is_valid():
#         user = form.save(commit=False)
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password1')
#         email = form.cleaned_data.get('email')
#         exists = False
#         try:
#             has = User.objects.get(email=email)
#             exists = True
#         except ObjectDoesNotExist:
#             pass
#         if exists:
#             messages.success(request, 'This email has already been registered, try another email', form.errors)
#             context = {
#                 'form': form,
#             }
#             return render(request, 'forms/registration.html', context)
#         else:
#             user.is_active = False
#             user.save()
#             domain = get_current_site(request).domain
#             uidb68 = urlsafe_base64_encode(force_bytes(user.pk))
#             link = reverse('user:activate', kwargs={'uidb64': uidb68, 'token': token_generator.make_token(user)})
#             activate_url = 'http://' + domain + link
#             email_subject = "Activate your account"
#             fro = settings.EMAIL_HOST_USER
#             email_body = "Hi " + user.username + " please use this link to verify your account " + activate_url
#             # print(email_body)
#             email = EmailMessage(
#                 email_subject,
#                 email_body,
#                 # email_body,
#                 fro,
#                 [email],
#             )
#             email.send(fail_silently=False)
#
#             # inactive_user = send_verification_email(request,form)
#             messages.success(request, 'Account was created for ' + username + ' proceed to your email to activate')
#
#             return redirect('user:login')
