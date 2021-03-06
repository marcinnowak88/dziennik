from django import forms
from django.forms import ModelForm
from .models import Course, Student, Student_course_grade

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title','description','course_image']

""""
class Student2Form(ModelForm):
    class Meta:
        model = Student2
        fields = ['first_name','last_name','sex','student_image']
"""

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name','last_name','album','sex','student_image']


class GradeForm(ModelForm):
    class Meta:
        model = Student_course_grade
        fields = ['course', 'student', 'grade']

"""
class CommentForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'special'})
        self.fields['comment'].widget.attrs.update(size='40')
"""

"""
class GradeForm(ModelForm):
    class Meta:
        model = Grade
        fields = ['grade']
"""


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)



class NewForm(forms.Form):
    GRADE = {
        ('2.0', '2.0'),
        ('3.0', '3.0'),
        ('3.5', '3.5'),
        ('4.0', '4.0'),
        ('4.5', '4.5'),
        ('5.0', '5.0'),
    }
    ocena = forms.ChoiceField(choices=GRADE)




"""
< select
class ="form-select" aria-label="Default select example" >
< option
selected > Ocena < / option >
< option
value = "1" > 2.0 < / option >
< option
value = "2" > 3.0 < / option >
< option
value = "3" > 3.5 < / option >
< option
value = "4" > 4.0 < / option >
< option
value = "5" > 4.5 < / option >
< option
value = "6" > 5.0 < / option >
< / select >
"""


# class StudentRegisterForm(forms.Form):
#     username = forms.CharField(label='Username', max_length=20)
#     password = forms.CharField(widget=forms.PasswordInput)
#     email = forms.EmailField(label='Email', max_length=50)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)
#     first_name = forms.CharField(label='First Name', max_length=20)
#     last_name = forms.CharField(label='Last Name', max_length=20)
#     student_id = forms.IntegerField(label='Student ID')
#
#
# class TeacherRegisterForm(forms.Form):
#     username = forms.CharField(label='Username', max_length=20)
#     password = forms.CharField(widget=forms.PasswordInput)
#     email = forms.EmailField(label='Email', max_length=50)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)
#     first_name = forms.CharField(label='First Name', max_length=20)
#     last_name = forms.CharField(label='Last Name', max_length=20)