from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import student
from .models import teacher
from .models import complaints
from .models import reply

# Create your views here.
def index(request):
    return render(request, 'index.html')

# registration
def student_registration(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        course=request.POST.get('course')
        year=request.POST.get('year')
        department=request.POST.get('department')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        email=request.POST.get('email')
        password=request.POST.get('password')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        email=request.POST.get('email')
        password=request.POST.get('password')
        exists=student.objects.filter(email=email).exists()
        if exists:
            return render(request,'useralreadytaken.html')
        else:
            reg=student.objects.create(name=name,course=course,year=year,department=department,phone=phone,address=address,email=email,password=password,image=fs)
            reg.save()
            return render(request,'index.html',{'msg':'user registered successfully'})
        
    return render(request,'student_registration.html')


def teacher_registration(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        # course=request.POST.get('course')
        # year=request.POST.get('year')
        department=request.POST.get('department')
        phone=request.POST.get('phone')
        # address=request.POST.get('address')
        email=request.POST.get('email')
        password=request.POST.get('password')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        email=request.POST.get('email')
        password=request.POST.get('password')
        exists=teacher.objects.filter(email=email).exists()
        if exists:
            return render(request,'useralreadytaken.html')
        else:
            reg=teacher.objects.create(name=name,department=department,phone=phone,email=email,password=password,image=fs)
            reg.save()
            return render(request,'index.html',{'msg':'user registered successfully'})
        
    return render(request,'teacher_registration.html')

#Login/Logout
def login(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    if student.objects.filter(email=email,password=password).exists():
        sdt_details=student.objects.get(email=request.POST['email'],password=password)
        if sdt_details.password==request.POST['password']:
            request.session['sid'] = sdt_details.id
            request.session['sname'] = sdt_details.name
            request.session['email'] = email
            request.session['student'] = 'student'
    
            return render(request,'index.html')
    
    elif teacher.objects.filter(email=email,password=password).exists():
        tc_details=teacher.objects.get(email=request.POST['email'],password=password)
        if tc_details.password==request.POST['password']:
            request.session['tid'] = tc_details.id
            request.session['tname'] = tc_details.name
            request.session['email'] = email
            request.session['teacher'] = 'teacher'
    
            return render(request,'index.html')

    else:
        return render(request,'login.html',{'status':'Invalid username or password'})


def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(index)

#profile
def student_profile(request):
    tem=request.session['sid']
    vpro=student.objects.get(id=tem)
    return render(request,'student_profile.html',{'result':vpro})


def teacher_profile(request):
    tem=request.session['tid']
    vpro=teacher.objects.get(id=tem)
    return render(request,'teacher_profile.html',{'result':vpro})


def view_student(request):
    dict_sc={
        'sc':student.objects.all()
    }
    return render(request,'student_profile.html',dict_sc)


def view_teacher_list(request):
    dict_tc={
        'tc':teacher.objects.all()
    }
    return render(request,'view_teacher_list.html',dict_tc)

#complaint code

def complaint_registration(request,id):
    tem=request.session['sid']
    reg=student.objects.get(id=tem)
    treg=teacher.objects.get(id=id)
    return render(request,'complaint_registration.html',{'result':reg,'res':treg})


def complaintreg(request,id):
    tem=request.session['sid']
    if request.method=="POST":
        std_name = student.objects.get(id=tem)
        tchr_name = teacher.objects.get(id=id)
        description = request.POST.get('description')
        regsave = complaints(s_name=std_name,t_name=tchr_name,description=description,id=id)
        regsave.save()
    return render(request,'complaint_successful.html')

# reply code

def complaint_reply(request,id):
    tem=request.session['tid']
    reg=teacher.objects.get(id=tem)
    treg=complaints.objects.get(id=id)
    return render(request,'complaint_reply.html',{'result':reg,'res':treg})


def replyreg(request,id):
    tem=request.session['tid']
    if request.method=="POST":

        teacher_instance = teacher.objects.get(id=tem)
        complaint_instance = complaints.objects.filter(t_name=teacher_instance).first()
        std_instance = complaints.objects.get(id=id)
        message = request.POST.get('message')
        regsave = reply(s_name=std_instance,t_name=complaint_instance,message=message)
        regsave.save()
    return render(request,'complaint_successful.html')


# student edit and update code

def regeditstd(request):
    return render(request,'regeditstd.html')


def editstd(request,id):
    upt = student.objects.get(id=id)
    return render(request,'regeditstd.html',{'result':upt})


def stdupdateext(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        course=request.POST.get('course')
        year=request.POST.get('year')
        department=request.POST.get('department')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        email=request.POST.get('email')
        password=request.POST.get('password')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        reg=student(name=name,course=course,year=year,department=department,phone=phone,address=address,email=email,password=password,image=fs,id=id)
        reg.save()
        return render(request,'index.html',{'msg':'user registered successfully'})
        
    return redirect(student_profile)


def stddlt(request,id):
    member = student.objects.get(id=id)
    member.delete()
    return redirect(student_registration)
# --------------end--------------

# teacher edit and delete code

def regedittchr(request):
    return render(request,'regedittchr.html')


def edittchr(request,id):
    upt = teacher.objects.get(id=id)
    return render(request,'regedittchr.html',{'result':upt})


def tchrupdateext(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        department=request.POST.get('department')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        image=request.FILES['image']
        f=FileSystemStorage()
        fs=f.save(image.name,image)
        reg=teacher(name=name,department=department,phone=phone,email=email,password=password,image=fs,id=id)
        reg.save()
        return redirect(teacher_profile)


def tchrdlt(request,id):
    member = teacher.objects.get(id=id)
    member.delete()
    return redirect(teacher_registration)

# --------------end code-------------------------------
              #complaint code
def teacher_view_complaint_list(request):
    tem=request.session['tid']
    teacher_instance = teacher.objects.get(id=tem)
    cmplnt_name = complaints.objects.filter(t_name=teacher_instance)
    return render(request,'teacher_view_complaint_list.html',{'result':cmplnt_name})


def student_view_reply(request):
    tem=request.session['sid']
    student_instance = student.objects.get(id=tem)
    reply_name = complaints.objects.filter(s_name=student_instance)
    rply_name = reply.objects.filter(s_name__in=reply_name)
    
    return render(request,'student_view_reply.html',{'result':rply_name})






