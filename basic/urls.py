from django.urls import path
from basic.views import SubjectCreateView, SubjectListView, SubjectDetailView, SubjectUpdateView, SubjectDeleteView, \
                        SubjectStatisticsView, ClassCreateView, ClassListView, SubjectAssignTeachersView, \
                        ClassDetailView, ClassUpdateView, ClassDeleteView, ClassAssignSubjectsView, ClassAssignTeacherView


urlpatterns = [
    path('subject/create', SubjectCreateView.as_view(), name='school_admin_subject_create'),
    path('subject/index', SubjectListView.as_view(), name='school_admin_subject_index'),
    path('subject/<int:pk>/detail', SubjectDetailView.as_view(), name='school_admin_subject_detail'),
    path('subject/<int:pk>/edit', SubjectUpdateView.as_view(), name='school_admin_subject_edit'),
    path('subject/<int:pk>/delete', SubjectDeleteView.as_view(), name='school_admin_subject_delete'),
    path('subject/<int:pk>/assign_teachers', SubjectAssignTeachersView.as_view(), name='school_admin_subject_assign_teacher'),
    path('subject/statistics', SubjectStatisticsView.as_view(), name='school_admin_subject_statistic'),

    path('class/create', ClassCreateView.as_view(), name='school_admin_class_create'),
    path('class/index', ClassListView.as_view(), name='school_admin_class_index'),
    path('class/<int:pk>/detail', ClassDetailView.as_view(), name='school_admin_class_detail'),
    path('class/<int:pk>/edit', ClassUpdateView.as_view(), name='school_admin_class_edit'),
    path('class/<int:pk>/delete', ClassDeleteView.as_view(), name='school_admin_class_delete'),
    path('class/<int:pk>/assign_subjects', ClassAssignSubjectsView.as_view(), name='school_admin_class_assign_subjects'),
    path('class/<int:pk>/assign_teacher', ClassAssignTeacherView.as_view(), name='school_admin_class_assign_teacher'),



]
