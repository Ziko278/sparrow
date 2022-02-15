from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.exceptions import ObjectDoesNotExist  # , MultiValueDictKeyError
from result.models import *
from registration.models import StudentsModel, ClassesModel
from result.forms import ResultForm
from setting.forms import SchoolAdminAcademicSettingForm, SessionModel
from sparrow_admin.models import SchoolsModel
from basic.models import SubjectsModel
from home.models import WebsiteInfoModel
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

            if total_score > 100:
                student_result = ResultModel.objects.filter(school=user_school, session=session, term=term,
                                                            student_class=student_class, student=student,
                                                            subject=subject)
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

                messages.success(request, 'Incorrect value input for ', student)
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

            print('student is :', student.student_result)

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
            student_complete_result = ResultModel.objects.filter(school=school, session=session, term=term,
                                                                 student_class=student_class, student=student,
                                                                 subject=subject).first()
            if student_complete_result:
                print('old data update')
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
                print('New')
                student_complete_result = {}
                student_complete_result[subject_pk] = student_result
                student_complete_result = ResultModel.objects.create(school=school, session=session, term=term,
                                                                     result={subject_pk: student_result},
                                                                     assignment=assignment_list[num],
                                                                     first_test=first_tests[num],
                                                                     second_test=second_tests[num],
                                                                     third_test=third_tests[num],
                                                                     fourth_test=forth_tests[num],
                                                                     fifth_test=fifth_tests[num],
                                                                     sixth_test=sixth_tests[num],
                                                                     exam=exams[num],
                                                                     total=total_score,
                                                                     grade=grade,
                                                                     remark=remark,
                                                                     subject=subject,
                                                                     student_class=student_class, student=student)
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
        other_info = False
        try:
            term = request.POST['term']
            session = request.POST['session']
            other_info = True
        except:
            other_info = False

        if other_info:
            print('YES')
            request.session['session'] = session
            request.session['term'] = term
        else:
            print('NOOOO')
            request.session['session'] = None
            request.session['term'] = None

        subject = request.POST['subject']
        request.session['result_class'] = student_class
        request.session['result_subject'] = subject
        return redirect(reverse('school_admin_result_index'))

    school_pk = request.session['user_school_id']
    form_class = SchoolAdminAcademicSettingModel.objects.all()
    user_school = SchoolsModel.objects.get(pk=school_pk)
    class_list = ClassesModel.objects.filter(school=user_school)
    subject_list = SubjectsModel.objects.filter(school=user_school)

    context = {
        'user_school': user_school,
        'class_list': class_list,
        'subject_list': subject_list,
        'form': form_class,
    }
    return render(request, 'result/check.html', context=context)


def result_index_view(request):
    """"""
    school_pk = request.session['user_school_id']
    user_school = SchoolsModel.objects.get(pk=school_pk)
    academic_setting = SchoolAdminAcademicSettingModel.objects.filter(school=user_school)[0]
    result_setting = SchoolAdminResultSettingModel.objects.filter(school=user_school)[0]
    tests = int(result_setting.tests)
    print(request.session['session'])
    if request.session['session'] is not None:
        session = request.session['session']
    else:
        print('SESSION NOOO')
        session = academic_setting.session
    if request.session['session'] is not None:
        term = request.session['term']
    else:
        print('TERM NO')
        term = academic_setting.term
    class_pk = request.session['result_class']
    student_class = ClassesModel.objects.get(pk=class_pk)
    subject_pk = request.session['result_subject']
    subject = SubjectsModel.objects.get(pk=subject_pk)
    student_list = StudentsModel.objects.filter(student_class=student_class)
    full_list = {}
    print(term, ': ', session)
    student_result = ResultModel.objects.filter(school=user_school, session=session, term=term,
                                                student_class=student_class, subject=subject)
    for v in student_result.all():
        print(v.second_test)
    print('student_result', student_result)
    print('full_list', full_list)
    context = {
        'user_school': user_school,
        'class': student_class,
        'subject': subject,
        'full_list': full_list,
        'result_setting': result_setting,
        'student_result': student_result,
        'tests': tests,
    }
    # <button onclick='windows.print()'>Print this page<button> for printing a htmlpage
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
    sessions = SessionModel.objects.all()
    result_setting = SchoolAdminResultSettingModel.objects.filter(school=user_school)[0]
    class_list = ClassesModel.objects.filter(school=user_school)
    subject_list = SubjectsModel.objects.filter(school=user_school)
    tests = int(result_setting.tests)

    if request.method == 'POST':
        need_session = request.POST['session']
        term = request.POST['term']
        # subject = request.POST['subject']
        request.session['need_session'] = need_session
        request.session['term'] = term
        results = ResultModel.objects.filter(student=student, session=need_session, term=term)
        print(student, ' : ', need_session, ' :', term, ' : ', results)
        context = {
            'user_school': user_school,
            'class_list': class_list,
            'subject_list': subject_list,
            'sessions': sessions,
            'student': student,
            'results': results,
            'tests': tests,
            'term': term,
            'session': need_session
        }
        return render(request, 'result/check_student_result.html', context=context)

    context = {
        'user_school': user_school,
        'student': student,
        'sessions': sessions,
    }
    return render(request, 'result/student_detail.html', context=context)


def result_student_sheet_view(request, pk):
    school_pk = request.session['user_school_id']
    user_school = SchoolsModel.objects.get(pk=school_pk)
    student = StudentsModel.objects.get(pk=pk)
    site_info = WebsiteInfoModel.objects.all()[0]
    result_setting = SchoolAdminResultSettingModel.objects.get(school=user_school)
    academic_setting = SchoolAdminAcademicSettingModel.objects.get(school=user_school)
    term = academic_setting.term
    session = academic_setting.session
    tests = int(result_setting.tests)
    result = ResultModel.objects.filter(school=user_school, term=term, session=session, student=student)
    rezult = TermResult.objects.filter(session=session, term=term,
                                       student_class=student.student_class)
    student_rezult = None
    result_exists = False
    if rezult:
        for rez in rezult:
            print(student, ':', rez)
            try:
                student_rezult = StudentResult.objects.get(student=student, results=rez) or None
            except ObjectDoesNotExist:
                pass

            if student_rezult:
                print(student_rezult)
                result_exists = True
            else:
                student_rezult = None
                result_exists = False
                print('No student_rezult found . . .')
    else:
        print('No past student rezult............')
        result_exists = False
    if result_exists:
        context = {
            'user_school': user_school,
            'student': student,
            'result_list': result,
            'result_setting': result_setting,
            'tests': tests,
            'total': student_rezult.results.total,
            'average': student_rezult.results.average,
            'position': student_rezult.results.position,
            'result': student_rezult,
            'published': student.student_class.publish_result,
        }
    else:
        position = 'None'
        total = 0.00

        for tot in result:
            total += tot.total
        if total > 0:
            average = total / len(result)
        else:
            average = 0.00
        context = {
            'user_school': user_school,
            'student': student,
            'result_list': result,
            'result_setting': result_setting,
            'tests': tests,
            'total': total,
            'average': average,
            'position': position,
            'published': student.student_class.publish_result,
        }
    return render(request, 'result/templates/result_template_one.html', context=context)


def update_result(request, pk):
    school_pk = request.session['user_school_id']
    user_school = SchoolsModel.objects.get(id=school_pk)
    class_pk = request.session['result_class']
    student_class = ClassesModel.objects.get(id=class_pk)
    subject_pk = request.session['result_subject']
    subject = SubjectsModel.objects.get(id=subject_pk)
    # student_list = StudentsModel.objects.filter(student_class=student_class)
    academic_setting = SchoolAdminAcademicSettingModel.objects.filter(school=user_school)[0]
    result_setting = SchoolAdminResultSettingModel.objects.filter(school=user_school)[0]
    tests = int(result_setting.tests)
    session = academic_setting.session
    term = academic_setting.term
    full_list = {}
    rez = ResultModel.objects.get(pk=pk)
    student = rez.student
    print(student)

    if request.method == 'POST':
        result = {}
        assignment_list = request.POST.get('assignments[]')
        first_tests = request.POST.get('first_tests[]')
        second_tests = request.POST.get('second_tests[]')
        third_tests = request.POST.get('third_tests[]')
        forth_tests = request.POST.get('forth_tests[]')
        fifth_tests = request.POST.get('fifth_tests[]')
        sixth_tests = request.POST.get('sixth_tests[]')
        exams = request.POST.get('exams[]')

        session = request.POST['session']
        term = request.POST['term']
        school_id = request.POST['school']
        school = SchoolsModel.objects.get(pk=school_id)
        class_pk = request.POST['student_class']
        student_class = ClassesModel.objects.get(pk=class_pk)

        # total_scores = []
        total_score = 0
        if assignment_list:
            total_score += float(assignment_list)
        else:
            assignment_list = 0.00
            total_score += 0.00
        if first_tests:
            total_score += float(first_tests)
        else:
            first_tests = 0.00
            total_score += 0.00
        if second_tests:
            total_score += float(second_tests)
        else:
            second_tests = 0.00
            total_score += 0.00
        if third_tests:
            total_score += float(third_tests)
        else:
            third_tests = 0.00
            total_score += 0.00
        if forth_tests:
            total_score += float(first_tests)
        else:
            forth_tests = 0.00
            total_score += 0.00
        if fifth_tests:
            total_score += float(second_tests)
        else:
            fifth_tests = 0.00
            total_score += 0.00
        if sixth_tests:
            total_score += float(third_tests)
        else:
            sixth_tests = 0.00
            total_score += 0.00
        if exams:
            total_score += float(exams)
        else:
            exams = 0.00
            total_score += 0.00
        total_score = int(total_score)

        if total_score > 100:
            student_result = ResultModel.objects.filter(school=user_school, session=session, term=term,
                                                        student_class=student_class, student=student, subject=subject)
            context = {
                'user_school': user_school,
                'class': student_class,
                'subject': subject,
                'full_list': full_list,
                'academic_setting': academic_setting,
                'result_setting': result_setting,
                'student_result': student_result,
                'tests': tests
            }
            messages.success(request, 'Incorrect value input for ', student)
            return render(request, 'result/update_student_result.html', context=context)

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

        student_complete_result = ResultModel.objects.get(school=school, session=session, term=term,
                                                          student_class=student_class,
                                                          student=student, subject=subject)

        subject_pk = request.POST['subject']
        student_result = {
            'assignment': assignment_list,
            'first_test': first_tests,
            'second_test': second_tests,
            'third_test': third_tests,
            'forth_test': forth_tests,
            'fifth_test': fifth_tests,
            'sixth_test': sixth_tests,
            'exam': exams,
            'total': total_score,
            'grade': grade,
            'remark': remark
        }
        if student_complete_result:
            student_complete_result.result[subject_pk] = student_result
            # if assignment_list and len(assignment_list) == len(student_list):
            student_complete_result.assignment = assignment_list
            # else:

            student_complete_result.first_test = first_tests
            student_complete_result.second_test = second_tests
            student_complete_result.third_test = third_tests
            student_complete_result.forth_test = forth_tests
            student_complete_result.fifth_test = fifth_tests
            student_complete_result.sixth_test = sixth_tests
            student_complete_result.exam = exams
            student_complete_result.total = total_score
            student_complete_result.grade = grade
            student_complete_result.remark = remark
        else:
            student_complete_result = {}
            student_complete_result[subject_pk] = student_result
            student_complete_result = ResultModel.objects.create(session=session, term=term, school=school,
                                                                 student_class=student_class,
                                                                 student=student,
                                                                 result=student_complete_result)
        student_complete_result.save()

        student_class.publish_result = False
        student_class.save()

    student_result = ResultModel.objects.filter(school=user_school, session=session, term=term,
                                                student_class=student_class, student=student, subject=subject)
    context = {
        'user_school': user_school,
        'class': student_class,
        'subject': subject,
        'full_list': full_list,
        'academic_setting': academic_setting,
        'result_setting': result_setting,
        'student_result': student_result,
        'tests': tests
    }
    return render(request, 'result/update_student_result.html', context=context)


def single_student_result_view(request, pk):
    """"""
    school_pk = request.session['user_school_id']
    user_school = SchoolsModel.objects.get(pk=school_pk)
    academic_setting = SchoolAdminAcademicSettingModel.objects.filter(school=user_school)[0]
    result_setting = SchoolAdminResultSettingModel.objects.filter(school=user_school)[0]
    tests = int(result_setting.tests)
    student = StudentsModel.objects.get(pk=pk)
    # result = ResultModel.objects.get(student=student)
    form_class = SessionModel.objects.all()
    class_list = ClassesModel.objects.filter(school=user_school)
    subject_list = SubjectsModel.objects.filter(school=user_school)

    # print(form_class.session.dash_format)
    if request.method == 'POST':
        need_session = request.POST['session']
        term = request.POST['term']
        # subject = request.POST['subject']
        request.session['need_session'] = need_session
        request.session['term'] = term
        results = ResultModel.objects.filter(student=student, session=need_session, term=term)
        print(student, ' : ', need_session, ' :', term, ' : ', results)
        context = {
            'user_school': user_school,
            'class_list': class_list,
            'subject_list': subject_list,
            'form': form_class,
            'student': student,
            'results': results,
            'tests': tests,
            'term': term,
            'session': need_session
        }
        return render(request, 'result/check_student_result.html', context=context)

    context = {
        'user_school': user_school,
        'class_list': class_list,
        'subject_list': subject_list,
        'form': form_class,
        'student': student,
    }
    return render(request, 'result/check_student_result_view.html', context=context)


def publish_result(request, pk):
    global old_position
    school_pk = request.session['user_school_id']
    user_school = SchoolsModel.objects.get(pk=school_pk)
    academic_setting = SchoolAdminAcademicSettingModel.objects.filter(school=user_school)[0]
    result_setting = SchoolAdminResultSettingModel.objects.filter(school=user_school)[0]
    tests = int(result_setting.tests)
    session = academic_setting.session
    term = academic_setting.term
    student_class = ClassesModel.objects.get(pk=pk)
    class_result_dict = {}
    class_result_dict_total = {}
    class_result_dict_avg = {}
    class_result_dict_position = {}
    class_results = ResultModel.objects.filter(student_class=student_class,
                                               school=user_school, session=session, term=term)
    students = []
    for result in class_results:
        # print(class_result_dict)
        if str(result.student) not in class_result_dict:
            students.append(result.student)
            # print('new', result.student)
            class_result_dict[str(result.student)] = [result.total]
        else:
            class_result_dict[str(result.student)].append(result.total)
        # if str(result.student) not in class_result_dict:
        #     students.append(result.student)
        #     # print('new', result.student)
        #     class_result_dict[str(result.student)] = [result.total]
        # else:
        #     class_result_dict[str(result.student)].append(result.total)
    # print(class_result_dict)
    # print(students)
    for k, v in class_result_dict.items():
        class_result_dict_total[k] = sum(v)
    # print(class_result_dict_total)
    for k, v in class_result_dict.items():
        class_result_dict_avg[k] = [sum(v), sum(v) / len(v)]
    # print(class_result_dict_avg)
    sorted_scores = sorted(class_result_dict_avg.items(), key=lambda x: x[1][1], reverse=True)
    print('sorted_scores :', sorted_scores)
    position = 1
    local_max = None
    # return  va
    for i in sorted_scores:
        if i not in class_result_dict_position.items():
            for stud in students:
                # print('stud',stud,'i',i[0])
                if str(stud) == i[0]:
                    student = stud
            # student =
            student_result = ResultModel.objects.filter(student_class=student_class,
                                                        school=user_school, session=session, term=term, student=student)
            # print('student model :',student_result.student)
            if i[1] != local_max:
                # print(i[0])
                if float(i[1][1]) >= 70:
                    grade, remark = 'A', 'EXCELLENT'
                elif (i[1][1] >= 60) and i[1][1] < 70:
                    grade, remark = 'B', 'VERY GOOD'
                elif (i[1][1] >= 50) and i[1][1] < 60:
                    grade, remark = 'C', 'GOOD'
                elif (i[1][1] >= 45) and i[1][1] < 50:
                    grade, remark = 'D', 'FAIR'
                elif (i[1][1] >= 40) and i[1][1] < 45:
                    grade, remark = 'E', 'POOR'
                elif i[1][1] < 40:
                    grade, remark = 'F', 'FAIL'
                else:
                    grade, remark = '', ''

                class_result_dict_position[i[0]] = [i[1][0], i[1][1], position, grade, remark, student_result, student]
                local_max = i[1]
                old_position = position
                position += 1
                # print('student in student', student)
            else:
                if float(i[1][1]) >= 70:
                    grade, remark = 'A', 'EXCELLENT'
                elif (i[1][1] >= 60) and i[1][1] < 70:
                    grade, remark = 'B', 'VERY GOOD'
                elif (i[1][1] >= 50) and i[1][1] < 60:
                    grade, remark = 'C', 'GOOD'
                elif (i[1][1] >= 45) and i[1][1] < 50:
                    grade, remark = 'D', 'FAIR'
                elif (i[1][1] >= 40) and i[1][1] < 45:
                    grade, remark = 'E', 'POOR'
                elif i[1][1] < 40:
                    grade, remark = 'F', 'FAIL'
                else:
                    grade, remark = '', ''

                class_result_dict_position[i[0]] = [i[1][0], i[1][1], old_position, grade, remark, student_result,
                                                    student]
                # print('student in student', student)
    # print(class_result_dict_position)
    result_exists = False
    f = 0
    s = 0
    for k, v in class_result_dict_position.items():
        f += 1
        print('f ==== ', f)
        st = v[-1]
        print('student', st)
        rezult = TermResult.objects.filter(session=academic_setting.session, term=academic_setting.term,
                                           student_class=student_class)
        student_rezult = None
        if rezult:

            # student_rezult = StudentResult.objects.get(student=v[-1], results=[r.id for r in rezult])
            # print(student_rezult)
            for rez in rezult:
                s += 1
                print('s ==== ', s)
                print(v[-1], ':', rez)
                try:
                    student_rezult = StudentResult.objects.get(student=v[-1], results=rez) or None
                except ObjectDoesNotExist:
                    pass

                if student_rezult:
                    print(student_rezult)
                    result_exists = True
                else:
                    student_rezult = None
                    result_exists = False
                    print('No student_rezult found . . .')
                # try:
                #     # print(v[-1],':',rez)
                #     student_rezult = StudentResult.objects.get(student=v[-1], results=rez.id)
                #
                #     result_exists = True
                #     if student_rezult:
                #         print(student_rezult.results.position)
                # except ObjectDoesNotExist:
                #     print('No past student result...')
                #     # result_exists = False
                # except:
                #     print('an unknown exception occured . . . . .')
        else:
            print('No past student rezult............')
            result_exists = False
        print(result_exists)
        if result_exists:

            student_rezult.results.total = v[0]
            student_rezult.results.average = v[1]
            student_rezult.results.position = v[2]
            student_rezult.results.grade = v[3]
            student_rezult.results.remark = v[4]
            student_rezult.results.result.set(v[-2])
            print('result updated for ', student_rezult, ':', student_rezult.results.position)
            student_rezult.results.save()
        else:
            # return va
            term_result = TermResult.objects.create(
                session=academic_setting.session,
                term=academic_setting.term,
                student_class=student_class,
                total=v[0],
                average=v[1],
                position=v[2],
                grade=v[3],
                remark=v[4]
            )
            term_result.result.set(v[-2])
            # term_result.save()
            # print(term_result.term,':', academic_setting.term)
            # print(lambda x: student_class.class_student.name)
            student_rezult = StudentResult.objects.create(
                student=v[-1],
                results=term_result
            )
            # student_rezult.save()
            # print('student_rezult ',student_rezult.results)

    student_class.publish_result = True
    student_class.save()

    return redirect("school_admin_class_detail", pk=pk)
    # return reverse('school_admin_class_detail', kwargs={'pk': pk})


def class_result(request, pk):
    school_pk = request.session['user_school_id']
    user_school = SchoolsModel.objects.get(pk=school_pk)
    # student_list = StudentsModel.objects.filter(student_class=student_class)

    academic_setting = SchoolAdminAcademicSettingModel.objects.filter(school=user_school)[0]
    result_setting = SchoolAdminResultSettingModel.objects.filter(school=user_school)[0]
    tests = int(result_setting.tests)
    # session = academic_setting.session
    # term = academic_setting.term
    student_class = ClassesModel.objects.get(pk=pk)

    results = TermResult.objects.filter(session=academic_setting.session, term=academic_setting.term,
                                        student_class=student_class).order_by('position')
    for r in results:
        for s in r.result.all():
            print(s.student.image)
            print(s.student)

    context = {
        'user_school': user_school,
        'class': student_class,
        # 'student_list': student_list,
        'results': results,
        'test': tests,
    }
    return render(request, 'result/class_result.html', context=context)
