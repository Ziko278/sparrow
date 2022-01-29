from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from registration.views import StaffCreateView, StaffListView, StaffDetailView, StaffUpdateView, StaffDeleteView,\
    ParentCreateView, ParentListView, ParentDetailView, ParentUpdateView, ParentDeleteView, StudentCreateView, \
    StudentListView, StudentDetailView, StudentUpdateView, StudentDeleteView, student_check_parent_view


urlpatterns = [
    path('staff/create', StaffCreateView.as_view(), name='school_admin_staff_create'),
    path('staff/index', StaffListView.as_view(), name='school_admin_staff_index'),
    path('staff/<int:pk>/detail', StaffDetailView.as_view(), name='school_admin_staff_detail'),
    path('staff/<int:pk>/edit', StaffUpdateView.as_view(), name='school_admin_staff_edit'),
    path('staff/<int:pk>/delete', StaffDeleteView.as_view(), name='school_admin_staff_delete'),

    path('parent/create', ParentCreateView.as_view(), name='school_admin_parent_create'),
    path('parent/index', ParentListView.as_view(), name='school_admin_parent_index'),
    path('parent/<int:pk>/detail', ParentDetailView.as_view(), name='school_admin_parent_detail'),
    path('parent/<int:pk>/edit', ParentUpdateView.as_view(), name='school_admin_parent_edit'),
    path('parent/<int:pk>/delete', ParentDeleteView.as_view(), name='school_admin_parent_delete'),

    path('student/check_parent', student_check_parent_view, name='school_admin_student_check_parent'),
    path('student/create/<int:parent_pk>', StudentCreateView.as_view(), name='school_admin_student_create'),
    path('student/index', StudentListView.as_view(), name='school_admin_student_index'),
    path('student/<int:pk>/detail', StudentDetailView.as_view(), name='school_admin_student_detail'),
    path('student/<int:pk>/edit', StudentUpdateView.as_view(), name='school_admin_student_edit'),
    path('student/<int:pk>/delete', StudentDeleteView.as_view(), name='school_admin_student_delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
