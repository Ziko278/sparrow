from django.urls import path
from .views import *


urlpatterns = [
    path('create', result_create_view, name='school_admin_result_create'),
    path('upload', result_upload_view, name='school_admin_result_upload'),
    path('check', result_check_view, name='school_admin_result_check'),
    path('index', result_index_view, name='school_admin_result_index'),
    path('update/<int:pk>', update_result, name='school_admin_result_update'),
    path('check/<int:pk>', single_student_result_view, name='school_admin_check_result_view'),
    path('class_list', result_class_list_view, name='school_admin_result_class_list'),
    path('class_result/<pk>', class_result, name='school_admin_class_result'),
    path('student/<int:pk>', result_student_detail_view, name='school_admin_result_student_detail'),
    path('student/sheet/<int:pk>', result_student_sheet_view, name='school_admin_result_student_sheet'),
    path('publish/<int:pk>', publish_result, name='school_admin_publish_result'),
]
