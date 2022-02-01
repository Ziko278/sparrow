from django.urls import path
from home.views import *

urlpatterns = [
    path('', WebsiteHome.as_view(), name='website_homepage'),
    path('about', WebsiteAbout.as_view(), name='website_about_page'),
    path('contact-us', send_message, name='website_contact_us_page'),
    path('our-products', WebsiteProduct.as_view(), name='website_our_product_page'),
    path('our-services', WebsiteService.as_view(), name='website_our_service_page'),


    path('schools/register', SchoolsRegister.as_view(), name='school_register'),
    path('schools/registration/successful', SchoolsRegisterSuccess.as_view(), name='school_register_success'),
    path('schools/admin', SchoolsDashboard.as_view(), name='school_admin_dashboard'),
]
