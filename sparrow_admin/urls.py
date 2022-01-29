from django.urls import path
from sparrow_admin.views import Dashboard, SchoolCreateView, SchoolListView, SchoolDetailView, SchoolNewListView, \
    SchoolStatisticsView, SchoolUpdateView, school_update_status, SchoolDashboard, WebsiteInfoUpdateView, \
    WebsiteInfoCreateView, WebsiteInfoDetailView

urlpatterns = [
    path('', Dashboard.as_view(), name='admin_dashboard'),
    path('<int:pk>', SchoolDashboard.as_view(), name='school_admin_dashboard'),
    path('schools/create', SchoolCreateView.as_view(), name='admin_register_school'),
    path('schools/index', SchoolListView.as_view(), name='admin_school_list'),
    path('schools/new', SchoolNewListView.as_view(), name='admin_new_school_list'),
    path('schools/<int:pk>/detail', SchoolDetailView.as_view(), name='admin_school_detail'),
    path('schools/<int:pk>/edit', SchoolUpdateView.as_view(), name='admin_school_edit'),
    path('schools/<int:pk>/activate', school_update_status,  name='admin_school_activate'),
    path('schools/statistics', SchoolStatisticsView.as_view(), name='admin_school_statistic'),

    path('website/info', WebsiteInfoCreateView.as_view(), name='admin_website_info_create'),
    path('website/info/<int:pk>/detail', WebsiteInfoDetailView.as_view(), name='admin_website_info_detail'),
    path('website/info/<int:pk>/edit', WebsiteInfoUpdateView.as_view(), name='admin_website_info_edit'),
]

