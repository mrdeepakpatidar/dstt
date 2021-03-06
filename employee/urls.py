from django.urls import path
from . import views

urlpatterns = [
    # path('employee/',views.AllEmployeeView.as_view(),name='employee' ),
    # path('registeremployee/',views.RegisterEmployeeView,name='registeremployee' ),
    # path('allemployee/',views.AllEmployeeview,name='allemployee' ),
    # path('update_employees/<int:id>',views.UpdateEmployeesview,name='update_employees' ),
    path('employee_profile/',views.Employees_Profile_View,name='employee_profile' ),
    path('employee_dashboard/',views.EmployeeDashboardView.as_view(),name='employee_dashboard' ),
    path('holiday/',views.HolidayCreateView.as_view(),name='holiday' ),
    path('HolidayRemove/<int:id>',views.HolidayRemoveView.as_view(),name='HolidayRemove' ),
    path('leaves_admin/',views.LeavesAdminView.as_view(),name='leaves_admin' ),
    path('leaves_employee/',views.LeavesEmployeeView.as_view(),name='leaves_employee' ),
    path('leaves_settings/',views.LeavesSettingsView.as_view(),name='leaves_settings' ),
    path('attendance_admin/',views.AttendanceAdminView.as_view(),name='attendance_admin' ),
    path('attendance_employee/',views.AttendanceEmployeeView.as_view(),name='attendance_employee' ),
# -------------------------------------------Departments-----------------------------------------------------------
    path('departments/',views.DepartmentCreateView.as_view(),name='departments' ),
    path('department_list/',views.DepartmentList.as_view(),name='department_list'),
    path('department_remove/<int:id>',views.DepartmentRemove.as_view(),name='department_remove' ),
    path('department_manage/<int:pk>',views.ManageDepartment.as_view(),name='department_manage' ),
# -------------------------------------------/Departments-----------------------------------------------------------

# -------------------------------------------designation-----------------------------------------------------------
    path('designation/',views.DesignationCreateView.as_view(),name='designation' ),
    path('designations_remove/<int:id>',views.DesignationRemove.as_view(),name='designations_remove' ),
    # path('designation_manage/',views.DesignationManage.as_view(),name='designation_manage' ),
    # path('designations_list/',views.DesignationListView.as_view(),name='designations_list' ),
# -------------------------------------------designation-----------------------------------------------------------
    
    path('timesheet/',views.TimesheetView.as_view(),name='timesheet' ),
    path('overtime/',views.OvertimeView.as_view(),name='overtime' ),   
]