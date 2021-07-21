from django.urls import path
from dziennikweb.views import all_courses, new_course, edit_course, delete_course
from dziennikweb.views import all_students, new_student, edit_student, delete_student, new_grade, edit_grade, delete_grade
from dziennikweb.views import student, edit_student_course,course_list_of_student, login_view, main_view, average, test, new_form


urlpatterns = [
    path('all/', all_courses, name="all_courses"),
    path('new/', new_course, name="new_course"),
    path('edit/<int:id>', edit_course, name="edit_course"),
    path('delete/<int:id>', delete_course, name="delete_course"),

    path('all_students/', all_students, name="all_students"),
    path('new_student/', new_student, name="new_student"),
    path('edit_student/<int:id>', edit_student, name="edit_student"),
    path('delete_student/<int:id>', delete_student, name="delete_student"),


    path('edit_student_course/<int:id>', edit_student_course, name="edit_student_course"),
    path('course_list_of_student/<int:id>', course_list_of_student, name="course_list_of_student"),

    path('new_grade/', new_grade, name="new_grade"),
    path('edit_grade/<int:id>', edit_grade, name="edit_grade"),
    path('delete_grade/<int:id>', delete_grade, name="delete_grade"),



    path('auth/login', login_view, name="login_view"),




    path('abc/', student, name="student"),
    path('average/', average, name="average"),
    path('test/', test, name="test"),
    path('new_form/', new_form, name="new_form"),

]
