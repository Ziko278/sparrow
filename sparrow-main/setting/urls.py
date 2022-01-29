from django.urls import path
from .views import SessionCreateView, SessionListView, SessionDetailView, SessionUpdateView, SessionDeleteView, \
    SparrowSettingView, SchoolSettingView, SchoolAcademicSettingCreateView, SchoolAcademicSettingUpdateView, \
    SchoolAcademicSettingDetailView

urlpatterns = [
    path('', SparrowSettingView.as_view(), name='sparrow_admin_setting'),
    path('<int:pk>', SchoolSettingView.as_view(), name='school_admin_setting'),

    path('academic_setting/<int:pk>/create', SchoolAcademicSettingCreateView.as_view(), name='school_academic_setting_create'),
    path('academic_setting/<int:pk>/detail', SchoolAcademicSettingDetailView.as_view(), name='school_academic_setting_detail'),
    path('academic_setting/<int:pk>/edit', SchoolAcademicSettingUpdateView.as_view(), name='school_academic_setting_edit'),

    path('session/create', SessionCreateView.as_view(), name='admin_session_create'),
    path('session/index', SessionListView.as_view(), name='admin_session_index'),
    path('session/<int:pk>/detail', SessionDetailView.as_view(), name='admin_session_detail'),
    path('session/<int:pk>/edit', SessionUpdateView.as_view(), name='admin_session_edit'),
    path('session/<int:pk>/delete', SessionDeleteView.as_view(), name='admin_session_delete'),


]
