
# imports
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, RoleViewSet, EmployeeViewSet, AttendanceViewSet
from . import views

# Setup the DefaultRouter viewsets.
router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'attendance', AttendanceViewSet)

urlpatterns = [

    # Homepage URL.
    path('', views.home, name='home'),

    # Include all api URLs from the router.
    path('api/', include(router.urls)),

    # Additional app-specific URLs.
    path('employee_details', views.employee_details, name='employee_details'),
    path('add_employee', views.add_employee, name='add_employee'),
    path('delete_employee/', views.delete_employee, name='delete_employee'),
    path('attendance_mark/', views.mark_attendance, name='mark_attendance'),
    path('attendance_details/', views.attendance_details,
         name='attendance_details'),
    path('departments_report/', views.department_employee_report,
         name='departments_report'),
]
