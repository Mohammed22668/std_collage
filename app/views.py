from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth import logout
from .models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def frontend(request):
    
    return HttpResponseRedirect('/backend/')


# Function to render with all Patients
@cache_control(no_cache=True , must_revalidate=True,no_store=True)
@login_required(login_url='login')
def backend(request):
    
    if 'q' in request.GET:
        q = request.GET['q']
        
        user = request.user.userprofile
        
        all_student_list = StudentDocument.objects.filter(
            Q(name__icontains=q) | Q(graduate_year=q) | Q(
                to=q) | Q(Dnumber=q)
        ).order_by('-created_at')
        all_student_list=all_student_list.filter(Dname=user.Dname,Cname=user.Cname,user=user.user)
        
    else:
        user = request.user.userprofile
        
        all_student_list = StudentDocument.objects.all().filter(user=user.user,Dname=user.Dname,Cname=user.Cname).order_by('-created_at')
    paginator = Paginator(all_student_list, 10)
    page = request.GET.get('page')
    all_students = paginator.get_page(page)
    context = {
        'studentDoc': all_students,
        'user': user,
    }
    return render(request, 'backend.html', context)


@cache_control(no_cache=True , must_revalidate=True,no_store=True)
@login_required(login_url='login')
def add_studentDoc(request):
    if request.method == 'POST':
        user = request.user.userprofile
        if request.POST.get('name') \
            and request.POST.get('user') \
            and request.POST.get('depart') \
            and request.POST.get('city') \
            and request.POST.get('year') \
            and request.POST.get('to') \
            and request.POST.get('Dnumber') \
            and request.POST.get('Ddate') \
                or request.POST.get('note'):
            studentDoc = StudentDocument()
            studentDoc.name = request.POST.get('name')
            studentDoc.user = request.POST.get('user')
            studentDoc.Dname = request.POST.get('depart')
            studentDoc.Cname = request.POST.get('city')
            studentDoc.graduate_year = request.POST.get('year')
            studentDoc.to = request.POST.get('to')
            studentDoc.Dnumber = request.POST.get('Dnumber')
            studentDoc.Ddate = request.POST.get('Ddate')
            studentDoc.note = request.POST.get('note')
            studentDoc.save()
            messages.success(request, 'تمت الاضافة بنجاح !')
            return HttpResponseRedirect('/backend/')
    else:
        user = request.user.userprofile
        context={
            'user':user,
        }
        return render(request, 'add_patients.html',context)


@cache_control(no_cache=True , must_revalidate=True,no_store=True)
@login_required(login_url='login')
def delete_studentDoc(request, std_id):
    studentDoc = StudentDocument.objects.get(id=std_id)
    studentDoc.delete()
    messages.success(request, 'تم الحذف ! ...')

    return HttpResponseRedirect('/backend/')



# fun for edit Patiesnts
@cache_control(no_cache=True , must_revalidate=True,no_store=True)
@login_required(login_url='login')
def studentDoc(request, std_id):
    user = request.user.userprofile
    studentDoc = StudentDocument.objects.get(id=std_id)
    if studentDoc != None:
        return render(request, 'edit.html', {'studentDoc': studentDoc,'user':user,})




@cache_control(no_cache=True , must_revalidate=True,no_store=True)
@login_required(login_url='login')
def edit_studentDoc(request):
    if request.method == 'POST':
        studentDoc=StudentDocument.objects.get(id=request.POST.get('id'))
        if studentDoc != None:
            studentDoc.name = request.POST.get('name')
            studentDoc.Dname = request.POST.get('depart')
            studentDoc.Cname = request.POST.get('city')
            studentDoc.graduate_year = request.POST.get('year')
            studentDoc.to = request.POST.get('to')
            studentDoc.Dnumber = request.POST.get('Dnumber')
            studentDoc.Ddate = request.POST.get('Ddate')
            studentDoc.note = request.POST.get('note')
            studentDoc.save()
            messages.success(request,'تم التعديل بنجاح !')
            return HttpResponseRedirect('/backend/')
        
        
        
############## Add states for students #####################
@cache_control(no_cache=True , must_revalidate=True,no_store=True)
@login_required(login_url='login')
def add_studentState(request):
    if request.method == 'POST':
        user = request.user.userprofile
        if request.POST.get('name') \
            and request.POST.get('user') \
            and request.POST.get('depart') \
            and request.POST.get('city') \
            and request.POST.get('year') \
            and request.POST.get('stage') \
            and request.POST.get('study') \
            and request.POST.get('state') \
                or request.POST.get('note'):
            studentState = StudentStatus()
            studentState.name = request.POST.get('name')
            studentState.user = request.POST.get('user')
            studentState.Dname = request.POST.get('depart')
            studentState.Cname = request.POST.get('city')
            studentState.year = request.POST.get('year')
            studentState.stage = request.POST.get('stage')
            studentState.study = request.POST.get('study')
            studentState.state = request.POST.get('state')
            studentState.note = request.POST.get('note')
            studentState.save()
            messages.success(request, 'تمت الاضافة بنجاح !')
            return HttpResponseRedirect('/backendState/')
    else:
        user = request.user.userprofile
        context={
            'user':user,
        }
        return render(request, 'students_status/add_state.html', context)
    
    
############################## Backend for add state page ##########################
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def backendState(request):

    if 'q' in request.GET:
        q = request.GET['q']

        user = request.user.userprofile
        all_student_list = StudentStatus.objects.filter(
            Q(name__icontains=q) | Q(state=q) | Q(
                stage=q) | Q(study=q) 
        ).order_by('-created_at')
        all_student_list=all_student_list.filter(Dname=user.Dname,Cname=user.Cname,user=user.user)
        
    else:
        user = request.user.userprofile
        all_student_list = StudentStatus.objects.all().filter(
            user=user.user, Dname=user.Dname, Cname=user.Cname).order_by('-created_at')
        
    paginator = Paginator(all_student_list, 5)
    page = request.GET.get('page')
    all_students_state = paginator.get_page(page)
    context = {
        'stdState': all_students_state,
        'user': user,
    }
    return render(request, 'students_status/backend-state.html', context)


############## Edit state for students ###########
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def edit_studentState(request):
    if request.method == 'POST':
        studentState = StudentStatus.objects.get(id=request.POST.get('id'))
        if studentState != None:
            studentState.name = request.POST.get('name')
            studentState.user = request.POST.get('user')
            studentState.Dname = request.POST.get('depart')
            studentState.Cname = request.POST.get('city')
            studentState.year = request.POST.get('year')
            studentState.stage = request.POST.get('stage')
            studentState.study = request.POST.get('study')
            studentState.state = request.POST.get('state')
            studentState.note = request.POST.get('note')
            studentState.save()
            messages.success(request, 'تم التعديل بنجاح !')
            return HttpResponseRedirect('/backendState/')


################
@cache_control(no_cache=True , must_revalidate=True,no_store=True)
@login_required(login_url='login')
def studentState(request, std_id):
    user = request.user.userprofile
    studentState = StudentStatus.objects.get(id=std_id)
    if studentState != None:
        return render(request, 'students_status/edit-state.html', {'stdState': studentState,'user':user,})
    
    
############## Delete state ############
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='login')
def delete_studentState(request, std_id):
    studentDoc = StudentStatus.objects.get(id=std_id)
    studentDoc.delete()
    messages.success(request, 'تم الحذف ! ...')

    return HttpResponseRedirect('/backendState/')


##################### Notifications #########################

def notification(request):
    if 'q' in request.GET:
        q = request.GET['q']

        user = request.user.userprofile
        all_post = Notifications.objects.filter(
            Q(title__icontains=q) | Q(get_from=q) | Q(
                note=q) | Q(year=q) 
        ).order_by('-created_at')
        dname = Department.objects.all().filter(Dname="الكل")
        cname = City.objects.all().filter(Cname="الكل")
        all_post = all_post.filter(Dname__in=[user.Dname, dname[0]], Cname__in=[user.Cname, cname[0]])
        
    else:
        user = request.user.userprofile
        dname = Department.objects.all().filter(Dname="الكل")
        cname = City.objects.all().filter(Cname="الكل")
        all_post = Notifications.objects.all().filter(
            Dname__in=[user.Dname, dname[0]], Cname__in=[user.Cname, cname[0]]).order_by('-created_at')
        
    paginator = Paginator(all_post, 5)
    page = request.GET.get('page')
    all_students_state = paginator.get_page(page)
    context = {
        'all_post': all_students_state,
        'user': user,
    }
    
    return render(request,'notifications/notfications.html',context)