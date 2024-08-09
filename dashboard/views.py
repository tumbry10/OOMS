from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from dashboard.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from dashboard.models import CustomUser

# Create your views here.
def home(request):
    return render(request, 'dashboard/home.html')

def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')

def manage_admin(request):
    return render(request, 'admin/manage_admin.html')

def add_admin(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password, user_type=1)
            user.save()
            messages.success(request, 'Admin Successfully Added')
            return redirect('add_admin')
        except:
            messages.error(request, 'Failed To Add Admin, Retry Again')
            return redirect('add_admin')
    else:
        return render(request, 'admin/add_admin.html')

def user_login(request):
    if request.method != 'POST':
        return render(request, 'dashboard/user_login.html')
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Invalid Login Details')
            return redirect('user_login')
        
def user_logout(request):
    logout(request)
    return redirect('user_login')

def manage_staff(request):
    return render(request, 'admin/manage_staff.html')

def add_staff(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')

        try:
            user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password, user_type=2)
            user.salesrep.gender=gender
            user.save()
            messages.success(request, 'Sales Rep Successfully Added')
            return redirect('add_staff')
        except:
            messages.error(request, 'Failed To Add Sales Rep, Retry Again')
            return redirect('add_staff')
    else:
        return render(request, 'admin/add_staff.html')