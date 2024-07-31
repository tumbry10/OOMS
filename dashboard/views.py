from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'dashboard/home.html')

def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')

def manage_admin(request):
    return render(request, 'admin/manage_admin.html')

def add_admin(request):
    return render(request, 'admin/add_admin.html')