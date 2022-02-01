from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from result.models import *
from registration.models import StudentsModel, ClassesModel
from result.forms import ResultForm
from sparrow_admin.models import SchoolsModel
from basic.models import SubjectsModel
from setting.models import SchoolAdminAcademicSettingModel, SchoolAdminResultSettingModel


# Create your views here.
def result_upload_view(request):

    school_pk = request.session['user_school_id']
    user_school = SchoolsModel.objects.get(pk=school_pk)
    class_pk = request.session['result_class']
    student_class = ClassesModel.objects.get(pk=class_pk)
    subject_pk = request.session['result_subject']
    subject = SubjectsModel.objects.get(pk=subject_pk)
    student_list = StudentsModel.objects.filter(student_class=student_class)
    academic_setting = SchoolAdminAcademicSettingModel.objects.filter(school=user_school)[0]
    result_setting = SchoolAdminResultSettingModel.objects.filter(school=user_school)[0]
    tests = int(result_setting.tests)
    session = academic_setting.session
    term = academic_setting.term
    full_list = {}
    #
    # for num in range(len(student_list)):
    #     stud = student_list[num]
    #     print(stud,' : ', stud.id)

    if request.method == 'POST':
        result = {}
        student_list = request.POST.getlist('students[]')
        assignment_list = request.POST.getlist('assignments[]')
        first_tests = request.POST.getlist('first_tests[]')
        second_tests = request.POST.getlist('second_tests[]')
        third_tests = request.POST.getlist('third_tests[]')
        forth_tests = request.POST.getlist('forth_tests[]')
        fifth_tests = request.POST.getlist('fifth_tests[]')
        sixth_tests = request.POST.getlist('sixth_tests[]')
        exams = request.POST.getlist('exams[]')

        session = request.POST['session']
        term = request.POST['term']
        school_id = request.POST['school']
        school = SchoolsModel.objects.get(pk=school_id)
        class_pk = request.POST['student_class']
        student_class = ClassesModel.objects.get(pk=class_pk)

        total_scores = []
        for num in range(len(student_list)):
            student = StudentsModel.objects.get(pk=student_list[num])
            total_score = 0
            if assignment_list and len(assignment_list) == len(student_list):
                total_score += float(assignment_list[num])
            else:
                assignment_list.append(0)
                total_score += 0.00
            if first_tests and len(first_tests) == len(student_list):
                total_score += float(first_tests[num])
            else:
                first_tests.append(0)
                total_score += 0.00
            if second_tests and len(second_tests) == len(student_list):
                total_score += float(second_tests[num])
            else:
                second_tests.append(0)
                total_score += 0.00
            if third_tests and len(third_tests) == len(student_list):
                total_score += float(third_tests[num])
            else:
                third_tests.append(0)
                total_score += 0.00
            if forth_tests and len(forth_tests) == len(student_list):
                total_score += float(first_tests[num])
            else:
                forth_tests.append(0)
                total_score += 0.00
            if fifth_tests and len(fifth_tests) == len(student_list):
                total_score += float(second_tests[num])
            else:
                fifth_tests.append(0)
                total_score += 0.00
            if sixth_tests and len(sixth_tests) == len(student_list):
                total_score += float(third_tests[num])
            else:
                sixth_tests.append(0)
                total_score += 0.00
            if exams:
                total_score += float(exams[num])
            else:
                total_score += 0.00
            total_score = int(total_score)

            if total_score >= 70:
                grade, remark = 'A', 'EXCELLENT'
            elif (total_score >= 60) and total_score < 70:
                grade, remark = 'B', 'VERY GOOD'
            elif (total_score >= 50) and total_score < 60:
                grade, remark = 'C', 'GOOD'
            elif (total_score >= 45) and total_score < 50:
                grade, remark = 'D', 'FAIR'
            elif (total_score >= 40) and total_score < 45:
                grade, remark = 'E', 'POOR'
            elif total_score < 40:
                grade, remark = 'F', 'FAIL'
            else:
                grade, remark = '', ''

            total_scores.append(total_score)
            # student = StudentsModel.objects.get(pk=student_list[num])
            # student_id = student_list[num].id
            # stud = student_list[num]
            # print(stud, ' : ')
            print('student is :', student.student_result)
            # student = StudentsModel.objects.get(pk=student_list[num].id)

            student_complete_result = ResultModel.objects.filter(school=school, session=session, term=term,
                                                                 student_class=student_class, student=student).first()

            subject_pk = request.POST['subject']
            student_result = {
                'assignment': assignment_list[num],
                'first_test': first_tests[num],
                'second_test': second_tests[num],
                'third_test': third_tests[num],
                'forth_test': forth_tests[num],
                'fifth_test': fifth_tests[num],
                'sixth_test': sixth_tests[num],
                'exam': exams[num],
                'total': total_score,
                'grade': grade,
                'remark': remark
            }
            if student_complete_result:
                student_complete_result.result[subject_pk] = student_result
                # if assignment_list and len(assignment_list) == len(student_list):
                student_complete_result.assignment = assignment_list[num]
                # else:

                student_complete_result.first_test = first_tests[num]
                student_complete_result.second_test = second_tests[num]
                student_complete_result.third_test = third_tests[num]
                student_complete_result.forth_test = forth_tests[num]
                student_complete_result.fifth_test = fifth_tests[num]
                student_complete_result.sixth_test = sixth_tests[num]
                student_complete_result.exam = exams[num]
                student_complete_result.total = total_score
                student_complete_result.grade = grade
                student_complete_result.remark = remark
            else:
                student_complete_result = {}
                student_complete_result[subject_pk] = student_result
                student_complete_result = ResultModel.objects.create(session=session, term=term, school=school,
                                                                     student_class=student_class, student=student,
                                                                     result=student_complete_result)
            student_complete_result.save()

        highest_in_class = max(total_scores)
        lowest_in_class = min(total_scores)
        total_mark_obtained = sum(total_scores)
        number_of_students = len(student_list)

        complete_result_stat = ResultStatisticModel.objects.filter(school=school, session=session, term=term,
                                                                   student_class=student_class).first()
        result_stat = {
            'highest_in_class': highest_in_class,
            'lowest_in_class': lowest_in_class,
            'total_mark_obtained': total_mark_obtained,
            'number_of_students': number_of_students

        }

        if complete_result_stat:
            complete_result_stat.result_statistic[subject_pk] = result_stat
        else:
            complete_result_stat = {}
            complete_result_stat[subject_pk] = result_stat
            complete_result_stat = ResultStatisticModel.objects.create(session=session, term=term, school=school,
                                                                            student_class=student_class,
                                                                            result_statistic=complete_result_stat)
        complete_result_stat.save()

        if complete_result_stat.id:
            request.session['result_class'] = class_pk
            request.session['result_subject'] = subject_pk
            return redirect(reverse('school_admin_result_index'))
        return redirect('../create')

    for student in student_list:
        student_result = ResultModel.objects.filter(school=user_school, session=session, term=term,
                                                    student_class=student_class, student=student).first()
        if student_result:
            if student_result.result.get(subject_pk):
                student_result = student_result.result[subject_pk]
            else:
                student_result = {}
        else:
            student_result = {}

        full_list[student.id] = {
            'student': student,
            'result': student_result
        }

    context = {
        'user_school': user_school,
        'class': student_class,
        'subject': subject,
        'full_list': full_list,
        'academic_setting': academic_setting,
        'result_setting': result_setting,
        'tests': tests
    }
    return render(request, 'result/upload.html', context=context)


def result_create_view(request):
    if request.method == 'POST':
        school_id = request.POST['school']
        student_class = request.POST['class']
        subject = request.POST['subject']
        request.session['result_class'] = student_class
        request.session['result_subject'] = subject
        return redirect(reverse('school_admin_result_upload'))

    school_pk = request.session['user_school_id']
    user_school = SchoolsModel.objects.get(pk=school_pk)
    class_list = ClassesModel.objects.filter(school=user_school)
    subject_list = SubjectsModel.objects.filter(school=user_school)

    context = {
        'user_school': user_school,
        'class_list': class_list,
        'subject_list': subject_list,
    }
    return render(request, 'result/create.html', context=context)


def result_check_view(request):
    """"""
    if request.method == 'POST':
        school_id = request.POST['school']
        student_class = request.POST['class']
        subject = request.POST['subject']
        request.session['result_class'] = student_class
        request.session['result_subject'] = subject
        return redirect(reverse('school_admin_result_index'))

    school_pk = request.session['user_school_id']
    user_school = SchoolsModel.objects.get(pk=school_pk)
    class_list = ClassesModel.objects.filter(school=user_school)
    subject_list = SubjectsModel.objects.filter(school=user_school)

    context = {
        'user_school': user_school,
        'class_list': class_list,
        'subject_list': subject_list
    }
    return render(request, 'result/check.html', context=context)


def result_index_view(request):
    """"""
    school_pk = request.session['user_school_id']
    user_school = SchoolsModel.objects.get(pk=school_pk)
    academic_setting = SchoolAdminAcademicSettingModel.objects.filter(school=user_school)[0]
    result_setting = SchoolAdminResultSettingModel.objects.filter(school=user_school)[0]
    tests = int(result_setting.tests)
    session = academic_setting.session
    term = academic_setting.term
    class_pk = request.session['result_class']
    student_class = ClassesModel.objects.get(pk=class_pk)
    subject_pk = request.session['result_subject']
    subject = SubjectsModel.objects.get(pk=subject_pk)
    student_list = StudentsModel.objects.filter(student_class=student_class)
    full_list = {}
    for student in student_list:
        student_result = ResultModel.objects.filter(school=user_school, session=session, term=term,
                                                    student_class=student_class, student=student).first()
        if student_result:
            if student_result.result.get(subject_pk):
                student_result = student_result.result[subject_pk]
            else:
                student_result = {}
        else:
            student_result = {}

        full_list[student.id] = {
            'student': student,
            'result': student_result
        }

    context = {
        'user_school': user_school,
        'class': student_class,
        'subject': subject,
        'full_list': full_list,
        'result_setting': result_setting,
        'tests': tests,
    }
    return render(request, 'result/index.html', context=context)


def result_class_list_view(request):
    """"""
    term = '1st term'
    session = 4
    school_pk = request.session['user_school_id']
    user_school = SchoolsModel.objects.get(pk=school_pk)
    class_pk = request.POST['class']
    student_class = ClassesModel.objects.get(pk=class_pk)
    student_list = StudentsModel.objects.filter(student_class=student_class)

    context = {
        'user_school': user_school,
        'class': student_class,
        'student_list': student_list
    }
    return render(request, 'result/class_list.html', context=context)


def result_student_detail_view(request, pk):
    school_pk = request.session['user_school_id']
    user_school = SchoolsModel.objects.get(pk=school_pk)
    student = StudentsModel.objects.get(pk=pk)

    context = {
        'user_school': user_school,
        'student': student
    }
    return render(request, 'result/student_detail.html', context=context)


def result_student_sheet_view(request, pk):
    school_pk = request.session['user_school_id']
    user_school = SchoolsModel.objects.get(pk=school_pk)
    student = StudentsModel.objects.get(pk=pk)
    term = '1st term'
    session = request.session['user_school_id']
    result = ResultModel.objects.filter(school=user_school, term=term, session=session, student=student).first()

    context = {
        'user_school': user_school,
        'student': student,
        'result_list': result
    }
    return render(request, 'result/templates/result_template_one.html', context=context)
