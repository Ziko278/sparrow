from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from result.models import ResultModel, ResultStatisticModel
from registration.models import StudentsModel, ClassesModel
from result.forms import ResultForm
from sparrow_admin.models import SchoolsModel
from basic.models import SubjectsModel
from setting.models import SchoolAdminAcademicSettingModel


# Create your views here.
def result_upload_view(request):
    if request.method == 'POST':
        result = {}
        student_list = request.POST.getlist('students[]')
        assignment_list = request.POST.getlist('assignments[]')
        first_tests = request.POST.getlist('first_tests[]')
        second_tests = request.POST.getlist('second_tests[]')
        third_tests = request.POST.getlist('third_tests[]')
        exams = request.POST.getlist('exams[]')

        session = request.POST['session']
        term = request.POST['term']
        school_id = request.POST['school']
        school = SchoolsModel.objects.get(pk=school_id)
        class_pk = request.POST['student_class']
        student_class = ClassesModel.objects.get(pk=class_pk)

        total_scores = []
        for num in range(len(student_list)):
            total_score = 0
            if assignment_list[num]:
                total_score += float(assignment_list[num])
            if first_tests[num]:
                total_score += float(first_tests[num])
            if second_tests[num]:
                total_score += float(second_tests[num])
            if third_tests[num]:
                total_score += float(third_tests[num])
            if exams[num]:
                total_score += float(exams[num])
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
            student = StudentsModel.objects.get(pk=student_list[num])

            student_complete_result = ResultModel.objects.filter(school=school, session=session, term=term,
                                                                 student_class=student_class, student=student).first()

            subject_pk = request.POST['subject']
            student_result = {
                'assignment': assignment_list[num],
                'first_test': first_tests[num],
                'second_test': second_tests[num],
                'third_test': third_tests[num],
                'exam': exams[num],
                'total': total_score,
                'grade': grade,
                'remark': remark
            }
            if student_complete_result:
                student_complete_result.result[subject_pk] = student_result
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

    school_pk = request.session['user_school_id']
    user_school = SchoolsModel.objects.get(pk=school_pk)
    class_pk = request.session['result_class']
    student_class = ClassesModel.objects.get(pk=class_pk)
    subject_pk = request.session['result_subject']
    subject = SubjectsModel.objects.get(pk=subject_pk)
    student_list = StudentsModel.objects.filter(student_class=student_class)
    academic_setting = SchoolAdminAcademicSettingModel.objects.filter(school=user_school)[0]
    session = academic_setting.session
    term = academic_setting.term
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
        'academic_setting': academic_setting
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
        'full_list': full_list
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
