from django.contrib import admin
from .models import Course, Student, Student_course_grade
from django.contrib.auth.admin import UserAdmin
from .models import User

#admin.site.register(Course)
#admin.site.register(Student)


class StudentCourseInline(admin.TabularInline):
    model = Student_course_grade
    fields=["course"]
    readonly_fields = ['student', 'grade']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields = ["title","description","course_image"]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ["first_name","last_name","album","sex","student_image"]
    list_display = ["first_name","last_name","sex"]
    list_filter = ["last_name","first_name"]
    search_fields = ["last_name"]
    #exclude = ["id"]
    inlines = [StudentCourseInline,]

@admin.register(Student_course_grade)
class Student_course_gradeAdmin(admin.ModelAdmin):
    fields = ["course","student", "grade"]
    list_display = ["course","student", "grade"]

#admin.site.register(User, UserAdmin)



UserAdmin.fieldsets += ('Custom fields set', {'fields': ('is_student', 'is_teacher', 'student')}),
@admin.register(User)
class DziennikAdmin(UserAdmin):
    pass

