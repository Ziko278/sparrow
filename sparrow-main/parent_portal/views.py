from django.shortcuts import render

# Create your views here.

# check = ResultModel.objects.filter(session=session, term=term, school=school,
#                                                student_class=student_class, student=student,
#                                                subject=subject)
#             if not check:
#                 student_complete_result = ResultModel(school=school, session=session, term=term,
#                                                       result = {subject_pk:student_result},
#                                                       assignment = assignment_list[num],
#                                                       first_test=first_tests[num],
#                                                       second_test=second_tests[num],
#                                                       third_test=third_tests[num],
#                                                       fourth_test=forth_tests[num],
#                                                       fifth_test=fifth_tests[num],
#                                                       sixth_test=sixth_tests[num],
#                                                       exam=exams[num],
#                                                       total=total_score,
#                                                       grade=grade,
#                                                       remark=remark,
#                                                       student_class=student_class, student=student)
#             else:
#                 print('just updated')
#                 student_complete_result = ResultModel.objects.filter(session=session, term=term, school=school,
#                                                                      student_class=student_class,
#                                                                      student=student).first()
#                 student_complete_result.result[subject_pk] = student_result
#                 # if assignment_list and len(assignment_list) == len(student_list):
#                 student_complete_result.assignment = assignment_list[num]
#                 # else:
#
#                 student_complete_result.first_test = first_tests[num]
#                 student_complete_result.second_test = second_tests[num]
#                 student_complete_result.third_test = third_tests[num]
#                 student_complete_result.forth_test = forth_tests[num]
#                 student_complete_result.fifth_test = fifth_tests[num]
#                 student_complete_result.sixth_test = sixth_tests[num]
#                 student_complete_result.exam = exams[num]
#                 student_complete_result.total = total_score
#                 student_complete_result.grade = grade
#                 student_complete_result.remark = remark
#             if student_complete_result:
#
#                 pass
#
#             else:
#                 student_complete_result = {}
#                 student_complete_result[subject_pk] = student_result
#                 student_complete_result = ResultModel.objects.create(session=session, term=term, school=school,
#                                                                      student_class=student_class, student=student,
#                                                                      result=student_complete_result)
#             student_complete_result.save()