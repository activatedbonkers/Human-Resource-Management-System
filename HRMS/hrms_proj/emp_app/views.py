# imports
from .models import Employee, Department, Role, Attendance
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import HttpResponse
from django.db.models import Count
from rest_framework import viewsets
from .serializers import DepartmentSerializer, RoleSerializer, EmployeeSerializer, AttendanceSerializer
from datetime import datetime
from .forms import AttendanceForm


def home(request):
    """
    View for the home page.
    """
    return render(request, 'home.html')


def employee_details(request):
    """
    View for displaying employee details.
    """
    return render(request, 'employee_details.html')


def attendance_details(request):
    """
    View for displaying attendance details.
    """
    return render(request, 'attendance_details.html')


def add_employee(request):
    """
    View for adding a new employee. On POST, saves a new Employee instance.
    On GET, displays the employee addition form.
    """
    if request.method == 'POST':

        # Create and save new Employee instance from POST data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept_id = int(request.POST['dept'])
        role_id = int(request.POST['role'])

        # Retrieve department and role objects
        dept = Department.objects.get(pk=dept_id)
        role = Role.objects.get(pk=role_id)

        # Create new Employee instance with department and role objects
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary,
                           bonus=bonus, phone=phone, dept=dept, role=role, hire_date=datetime.now())
        new_emp.save()
        return redirect('home')

        # Render the form for adding a new employee
    elif request.method == 'GET':

        # Fetch department names and roles for rendering the form
        departments = Department.objects.all()
        roles = Role.objects.all()
        context = {
            'departments': departments,
            'roles': roles,
        }
        return render(request, 'add_employee.html', context)
    else:
        return HttpResponse("An Exception Occurred! Employee Has Not Been Added")


def delete_employee(request):
    """
    View for deleting an employee. On POST, deletes the specified Employee instance.
    """
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        employee = get_object_or_404(Employee, id=employee_id)
        employee.delete()
        # Redirect to the home page or any other appropriate URL
        return redirect('home')

    employees = Employee.objects.all()
    return render(request, 'delete_employee.html', {'employees': employees})


def mark_attendance(request):
    """
    View for marking attendance. On POST, saves a new Attendance record.
    On GET, displays the attendance form.
    """
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AttendanceForm()
    return render(request, 'mark_attendance.html', {'form': form})


def department_employee_report(request):
    """
    View for generating a report of employee counts by department.
    """
    # Aggregate employee counts by department
    department_counts = Employee.objects.values(
        'dept__name').annotate(count=Count('dept')).order_by('-count')
    return render(request, 'departments_report.html', {'department_counts': department_counts})

class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing department instances.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class RoleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A viewset for viewing role instances.
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    A viewset for CRUD operations on attendance instances. Supports filtering by employee_id.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    """
        Optionally restricts the returned attendances to a given employee,
        by filtering against a `employee_id` query parameter in the URL.
        """
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        employee_id = self.request.query_params.get('employee_id', None)
        if employee_id is not None:
            queryset = queryset.filter(employee__id=employee_id)
        return queryset
