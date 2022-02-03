# import django_filters
# from django_filters import DateFilter, CharFilter
# from .models import *
# from books.models import OfflineBook, Ebook, BorrowedBook
#
#
# class StudentFilter(django_filters.FilterSet):
#     # search = CharFilter(lookup_expr='icontains')
#     # icontains means ignore case sensetivity
#
#     class Meta:
#         model = Student
#         fields = ['lib_no', 'lib_status', 'dept', 'school_fee']
#
#
# class StaffFilter(django_filters.FilterSet):
#     # search = CharFilter(lookup_expr='icontains')
#     # icontains means ignore case sensetivity
#
#     class Meta:
#         model = SchoolsModel
#         fields = ['name', 'type']
#
#
# class SchoolFilter(django_filters.FilterSet):
#     # search = CharFilter(lookup_expr='icontains')
#     # icontains means ignore case sensetivity
#     name = CharFilter(field_name='name', lookup_expr='icontains')
#
#     class Meta:
#         model = SchoolsModel
#         fields = ['name', 'type']
#
#
# class StaffAttendanceFilter(django_filters.FilterSet):
#     # search = CharFilter(lookup_expr='icontains')
#     # icontains means ignore case sensetivity
#     # lib_no = CharFilter(field_name='user.lib_no', lookup_expr='icontains')
#
#     class Meta:
#         model = StaffAttendance
#         fields = ['user__lib_no']
#
#
# class BookFilter(django_filters.FilterSet):
#
#     # icontains means ignore case sensetivity
#     title = CharFilter(field_name='title', lookup_expr='icontains')
#     other_contributors = CharFilter(field_name='other_contributors', lookup_expr='icontains')
#     author = CharFilter(field_name='author', lookup_expr='icontains')
#
#     class Meta:
#         model = OfflineBook
#         fields = ['call_no',]
#
#
# class EbookFilter(django_filters.FilterSet):
#     # search = CharFilter(lookup_expr='icontains')
#     # icontains means ignore case sensetivity
#     title = CharFilter(field_name='title', lookup_expr='icontains')
#     other_contributors = CharFilter(field_name='other_contributors', lookup_expr='icontains')
#     author = CharFilter(field_name='author', lookup_expr='icontains')
#
#     class Meta:
#         model = Ebook
#         fields = ['call_no',]
#
#
# class BorrowFilter(django_filters.FilterSet):
#     # icontains means ignore case sensetivity
#     title = CharFilter(field_name='title__title', lookup_expr='icontains')
#
#     class Meta:
#         model = BorrowedBook
#         fields = []
#
