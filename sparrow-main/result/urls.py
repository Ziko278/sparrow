from django.urls import path
from result.views import result_create_view, result_upload_view, result_check_view, result_index_view, \
    result_class_list_view, result_student_detail_view, result_student_sheet_view


urlpatterns = [
    path('create', result_create_view, name='school_admin_result_create'),
    path('upload', result_upload_view, name='school_admin_result_upload'),
    path('check', result_check_view, name='school_admin_result_check'),
    path('index', result_index_view, name='school_admin_result_index'),
    path('class_list', result_class_list_view, name='school_admin_result_class_list'),
    path('student/<int:pk>', result_student_detail_view, name='school_admin_result_student_detail'),
    path('student/sheet/<int:pk>', result_student_sheet_view, name='school_admin_result_student_sheet'),
]
