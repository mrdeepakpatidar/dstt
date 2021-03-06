from django.contrib.auth.models import Group
from django.http.response import HttpResponseRedirect
from account.models import User
from django.shortcuts import  redirect, render,HttpResponse
from django.views import generic
from django.views.generic import View,TemplateView,CreateView,UpdateView
from django.views.generic.edit import UpdateView
from .models import Employee
from django.db import IntegrityError
from django.contrib import messages
from django.views.generic import TemplateView,CreateView,ListView
from .models import Employee,Department,Designation,Holiday
from .forms import DepartmentForm,DesignationForm ,EmployeeForm, HolidayForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from datetime import datetime
# Create your views here.

def Employees_Profile_View(request):
    print(request.user)
    employee = Employee(request.GET)
    MyProfile = Employee.objects.filter(employee_email=request.user)
    print(MyProfile)
    return render(request,'employee/profile.html',{'myprofile':MyProfile})

# -------------------------------------all employee for admin--------------------------------
# @login_required(login_url='/')
# def RegisterEmployeeView(request):
#     if request.method =="POST":
#             employee_first_name = request.POST['employee_first_name']
#             employee_last_name = request.POST['employee_last_name']
#             employee_email = request.POST['employee_email']
#             employee_joining_date = request.POST['employee_joining_date']
#             employee_department = request.POST['employee_department']
#             employee_password = request.POST['employee_password']
#             employee_confirm_password = request.POST['employee_confirm_password']
#             employee_id = request.POST['employee_id']
#             employee_phone = request.POST['employee_phone']
#             # employee_role = Group.objects.get(name=request.POST['employee_role'])
#             try:
                
#                 user = User.objects.create_user(email=employee_email,password=employee_password)
#                 user.is_staff=False
#                 user.full_name = employee_first_name+' '+employee_last_name
#                 user.is_active=True
#                 user.is_employee=True
#                 user.save()
#                 register_employee = Employee(user=user,employee_first_name=employee_first_name,employee_last_name=employee_last_name,employee_email=employee_email,employee_joining_date=employee_joining_date,employee_department=employee_department,employee_id=employee_id,employee_phone=employee_phone)
#                 register_employee.save()
#                 messages.success(request,"Employee Registered Successfully!")
#             except IntegrityError as e:
#                 messages.error(request,"Email Already Registered!")
            
            
#             return redirect('/employee/allemployee')
#     else:
#         groups=Group.objects.all()
#         return render(request,'administration/employees.html',{'groups':groups})
            

# # ------------------------all employees for Administration ------------------------
# @login_required(login_url='/')

# def AllEmployeeview(request):
#     employee = Employee(request.GET)
#     AllEmployee = Employee.objects.all()
#     print(AllEmployee)
#     return render(request,'administration/employees.html',{'Employee':AllEmployee})




# @login_required(login_url='/')

# def UpdateEmployeesview(request,id):
#     employee_update = Employee.objects.get(id=id)  
#     if request.method == "POST":
#         employee_update.employee_department = request.POST.get('employee_department','')
#         employee_update.employee_designation = request.POST.get('employee_designation','')
#         employee_update.employee_phone = request.POST.get('employee_phone','')
#         employee_update.employee_address = request.POST.get('employee_address','')
#         employee_update.employee_state = request.POST.get('employee_state','')
#         employee_update.employee_country = request.POST.get('employee_country','')
#         employee_update.employee_pincode = request.POST.get('employee_pincode','')
#         employee_update.employee_reports_to = request.POST.get('employee_reports_to','')
#         if "employee_image" in request.FILES:   
#             img=request.FILES["employee_image"]
#             employee_update.employee_image =img
#         employee_update.save()
#         # return HttpResponse("done")
#     return render(request,"employee/employee_profile.html",{'employee_update':employee_update})

class EmployeeDashboardView(TemplateView):
    template_name = "employee/employee_dashboard.html"



class LeavesAdminView(TemplateView):
    template_name = "employee/leaves_admin.html"

class LeavesEmployeeView(TemplateView):
    template_name = "employee/leaves_employee.html"

class LeavesSettingsView(TemplateView):
    template_name = "employee/leaves_settings.html"

class AttendanceAdminView(TemplateView):
    template_name = "employee/attendance_admin.html"

class AttendanceEmployeeView(TemplateView):
    template_name = "employee/attendance_employee.html"
# ----------------------------------------Department----------------------------------------------------------------------------------
class DepartmentCreateView(generic.CreateView):
    model = Department
    fields = ('department_name',)
    template_name = "employee/departments.html"
    success_url = ('/employee/department_list')

class DepartmentList(generic.ListView):
    model = Department
    template_name ="employee/departments.html"
    context_object_name = "department_list"
    success_url = ('/employee/departments')

class DepartmentRemove(View):
    def get(self,request,id):
            department=Department.objects.get(id=id)          
            department.delete()
            messages.success(request,f"{department} deleted successfully")
            return HttpResponseRedirect('/employee/department_list') 

class ManageDepartment(UpdateView):
    model = Department
    fields = ['department_name']
    context_object_name = "department_update"
    template_name = "employee/department_manage.html"             
    success_url = ("/employee/department_list/")
 
# ----------------------------------------/Department----------------------------------------------------------------------------------

# ----------------------------------------/Designation----------------------------------------------------------------------------------
class DesignationCreateView(View):
    def post(self,request):
        form = DesignationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect('/employee/designation')
            except:
                pass
    def get(self,request):
        form = DesignationForm()
        designation = Designation.objects.all()
        return render(request,'employee/designations.html',{'form':form,'designation':designation})

class DesignationRemove(View):
    def get(self,request,id):
            designation=Designation.objects.get(id=id)          
            designation.delete()
            messages.success(request,f"{designation} deleted successfully")
            return HttpResponseRedirect('/employee/designation')  

# class DesignationManage(UpdateView):
#     model = Designation
#     fields = ['Designation_Name','Department_Name']
#     context_object_name = "designation_manage"
#     template_name = "employee/designation_manage.html"             
#     success_url = ("/employee/department_list/")
# ----------------------------------------/Designation----------------------------------------------------------------------------------


class HolidayCreateView(View):
    def post(self,request):
        form = HolidayForm(request.POST)
        if form.is_valid():
            Holiday_Date =  form.cleaned_data['Holiday_Date'] 
            print(Holiday_Date|weekday) 
            form.save()
            return HttpResponseRedirect('/employee/holiday')
           
    def get(self,request):
        form = HolidayForm()
        Holidays = Holiday.objects.all()
        return render(request,'employee/holidays.html',{'form':form,'Holiday':Holidays})


class HolidayRemoveView(View):
    def get(self,request,id):
            holiday=Holiday.objects.get(id=id)          
            holiday.delete()
            messages.success(request,f"{holiday} deleted successfully")
            return HttpResponseRedirect('/employee/holiday') 

class TimesheetView(TemplateView):
    template_name = "employee/timesheet.html"   

class OvertimeView(TemplateView):
    template_name = "employee/overtime.html"