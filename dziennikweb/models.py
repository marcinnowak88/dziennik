
from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser



class Course(models.Model):
    title = models.CharField(max_length=64, blank=False)
    description = models.TextField(blank=True, default="")
    course_image = models.ImageField(upload_to="courses_image", null=True, blank=True)

    #students = models.ManyToManyField(Student2, blank=True, default="")

    def __str__(self):
        return self.title




class Student(models.Model):

    first_name = models.CharField(max_length=32, blank=False)
    last_name = models.CharField(max_length=32, blank=False)
    album = models.CharField(max_length=32, blank=True, default='007')

    courses = models.ManyToManyField(Course,through="Student_course_grade")
    #grades = models.ManyToManyField(Grade,blank=True, default="")

    SEX = (('M', 'Male'),('F','Female'))
    sex = models.CharField(max_length=1, choices=SEX, default='Male')

    student_image = models.ImageField(upload_to="students_image", null=True, blank=True)

    #grades = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Student_course_grade(models.Model):

    GRADE = {
        ('2.0', '2.0'),
        ('3.0', '3.0'),
        ('3.5', '3.5'),
        ('4.0', '4.0'),
        ('4.5', '4.5'),
        ('5.0', '5.0'),
    }

    #id = models.AutoField(primary_key=True)

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    #grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    grade = models.CharField(max_length=3, default=2.0, choices=GRADE)

    class Meta:
        unique_together = ['course', 'student']




class User(AbstractUser):
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)



"""
    def __str__(self):
        return self.course + " " + self.student+ " " + str(self.grade)

"""









"""



"""

"""




class Ocena(models.Model):

    recenzja = models.TextField(default="", blank=True)
    gwiazdki = models.PositiveSmallIntegerField(default=5)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)    #many to one
"""
