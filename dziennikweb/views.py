from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Student, Student_course_grade
from .forms import CourseForm, StudentForm, StudentForm, GradeForm, LoginForm, NewForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied
from django.views.defaults import permission_denied
from django.db.models import Avg, Count, Max, Min

def all_courses(request):
    all = Course.objects.all
    return render(request, 'courses.html',{'courses': all})

@login_required
def new_course(request):
    is_new = True
    form = CourseForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(all_courses)

    return render(request, 'course_form.html', {'form': form, 'new': is_new})


@login_required
def edit_course(request, id):
    is_new = False
    course = get_object_or_404(Course, pk=id)
    form = CourseForm(request.POST or None, request.FILES or None, instance = course)

    if form.is_valid():
        form.save()
        return redirect(all_courses)
        
    return  render(request, 'course_form.html', {'form': form, 'new': is_new})

@login_required
def delete_course(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        course.delete()
        return redirect(all_courses)

    return render(request, 'confirm.html', {'course': course})


@login_required
def all_students(request):
    all = [request.user.student]

    if request.user.has_perm('applications.admin_access'):
        all = Student.objects.all
        return render(request, 'students.html', {'students': all})

    else:
        return render(request, 'students2.html',{'students': all})


"""
@login_required
def all_students(request):
    all = [request.user.student]

    if request.user.has_perm('applications.admin_access'):
        all = Student.objects.all

    return render(request, 'students.html',{'students': all})
"""

"""
@login_required
def all_students2(request):
    all = [request.user.student]

    if request.user.has_perm('applications.admin_access'):
        all = Student.objects.all

    return render(request, 'students2.html',{'students': all})

"""




@login_required
def new_student(request):

    if not request.user.has_perm('applications.admin_access'):
        return redirect(all_students)

    is_new = True
    form = StudentForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(all_students)

    return render(request, 'student_form.html', {'form': form, 'new': is_new})



@login_required
def edit_student(request, id):
    is_new = False
    student = get_object_or_404(Student, pk=id)
    form = StudentForm(request.POST or None, request.FILES or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect(all_students)

    return render(request, 'student_form.html', {'form': form, 'new': is_new})


@login_required
def delete_student(request, id):
    student = get_object_or_404(Student, pk=id)

    if request.method == "POST":
        student.delete()
        return redirect(all_students)

    return render(request, 'confirm3.html', {'student': student})




def student(request,id):
    student_list = Student.objects.filter(pk=id)
    #student_list = Student.objects.filter(last_name='Malinowski')
    student_list = {'student_list':student_list}
    return render(request, 'abc.html', student_list)


def student(request):
    student_list = Student.objects.all().order_by('-id')
    #student_list = Student.objects.filter(last_name='Malinowski')
    student_list = {'student_list':student_list}
    return render(request, 'abc.html', student_list)



@login_required
def edit_student_course(request, id):

    q = Student_course_grade.objects.filter(student=id)
    c = Student.objects.get(pk=id)

    l = []
    for x in q:
        l.append(float(x.grade))
    if len(l) > 0:
        m = sum(l) / len(l)
    else:
        m = "brak ocen"

    if request.user.has_perm('applications.admin_access'):

        return render(request, 'def.html', {'q': q, 'student': c, 'm': m})

    else:
        return render(request, 'mno.html', {'q': q, 'student': c, 'm': m})

"""

@login_required
def all_students(request):
    all = [request.user.student]

    if request.user.has_perm('applications.admin_access'):
        all = Student.objects.all
        return render(request, 'students.html', {'students': all})

    else:
        return render(request, 'students2.html',{'students': all})



@login_required
def edit_student_course(request, id):

    q = Student_course_grade.objects.filter(student=id)
    c = Student.objects.get(pk=id)

    l=[]
    for x in q:
        l.append(float(x.grade))

    if len(l)>0:
        m = sum(l)/len(l)

    else:
        m = "brak ocen"
    return render(request, 'def.html', {'q': q, 'student': c, 'm': m})

"""






"""
    student = get_object_or_404(Student, pk=id)
    #Student.objects.filter(pk=id)

    return render(request, 'def.html', {'student': student})
"""

@login_required
def course_list_of_student(request, id):

    q = Student_course_grade.objects.filter(course=id)
    z = Student_course_grade.objects.get(pk=id)
    xx = Student_course_grade.objects.filter(course=id).get(pk=id)
    c = Course.objects.get(pk=id)
    form3 = GradeForm(request.POST or None, request.FILES or None, instance=z)
    form2 = NewForm()


    l=[]
    for x in q:
        l.append(float(x.grade))

    if len(l)>0:
        m = sum(l)/len(l)

    else:
        m = "brak ocen"

    return render(request, 'ghi.html', {'q': q, 'z': z, 'xx': xx, 'course': c, 'm': m, 'form2': form2, 'form3': form3})



@login_required
def new_grade(request):
    is_new = True
    form = GradeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(all_courses)

    return render(request, 'grade_form.html', {'form': form, 'new': is_new})


@login_required
def edit_grade(request, id):

    is_new = False
    grade = Student_course_grade.objects.get(pk=id)
    form = GradeForm(request.POST or None, request.FILES or None, instance=grade)

    if form.is_valid():
        form.save()
        return redirect(all_courses)

    return render(request, 'grade_form.html', {'form': form, 'new': is_new})
    return render(request, 'ghi.html', {'form': form, 'new': is_new})



@login_required
def delete_grade(request, id):

    grade = Student_course_grade.objects.get(pk=id)
    c = grade.course
    d = grade
    if request.method == "POST":
        grade.delete()
        return redirect(all_students)

    return render(request, 'confirm2.html', {'grade': d})

def main_view(request):

    if request.user.has_perm('applications.admin_access'):

        return render(request, 'index.html')
    else:
        return render(request, 'student_view.html')




def login_view(request):

    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(main_view)

        else:
            raise PermissionDenied

    else:
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})




def average(request):
    list_of_grades = Student_course_grade.objects.filter(student=1)

    return render(request, 'jkl.html', {'list_of_grades': list_of_grades})



def test(request):

    c = Student.objects.all().annotate(number=Count('courses'))
    d = c[1].number
    b = [1,2,3,4]
    a = sum(b)/len(b)

    f = Student_course_grade.objects.filter(student=1)

    l=[]
    for x in f:
        l.append(float(x.grade))

    m = sum(l)/len(l)

    g = Student.objects.get(pk=1)

    return render(request, 'test.html', {'a': a, 'b': b, 'd': d, 'f': f, 'l': l, 'm': m, 'g': g})


# to nie jest wyswietlane nigdzie:
"""
def new_form(request, id):

    #form = NewForm()
    is_new = False
    grade = Student_course_grade.objects.get(pk=id)
    if request.method == "POST":
        form = NewForm(request.POST or None, request.FILES or None, instance=grade)

        if form.is_valid():
            form.save()
            return redirect(all_courses)
    else:
        form = NewForm()

    return render(request, 'new_form.html',{'form':form, 'new': is_new})
"""
def new_form(request):

    if request.method == "POST":
        form2 = NewForm(request.POST)

        if form2.is_valid():
            print('form is valid')
    else:
        form2 = NewForm()

    return render(request, 'new_form.html',{'form2': form2})
    return render(request, 'ghi.html',{'form2': form2})



"""
@login_required
def course_list_of_student(request, id):

    q = get_object_or_404(Student_course_grade, pk=id)

    return render(request, 'ghi.html', {'q': q})
"""

"""
@login_required
def edit_student_course(request, id):
    is_new = False
    student = get_object_or_404(Student, pk=id)
    form = StudentForm(request.POST or None, request.FILES or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect(all_students)

    return render(request, 'student_course_form.html', {'form': form, 'new': is_new})
"""