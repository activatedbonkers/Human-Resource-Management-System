# imports
from rest_framework import serializers
from .models import Department, Role, Employee, Attendance


class DepartmentSerializer(serializers.ModelSerializer):
    """
    Serializer for Department model.
    """
    class Meta:
        model = Department
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    """
    Serializer for Role model.
    """
    class Meta:
        model = Role
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer for Employee model, including nested serializers for department and role.

    Allows for department and role details to be included in the Employee serialization
    and supports writing by dept_id and role_id.
    """
    dept = DepartmentSerializer(read_only=True)
    dept_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Department.objects.all(), source='dept')
    role = RoleSerializer(read_only=True)
    role_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Role.objects.all(), source='role')

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'dept', 'dept_id',
                  'salary', 'bonus', 'role', 'role_id', 'phone', 'hire_date']


class AttendanceSerializer(serializers.ModelSerializer):
    """
    Serializer for Attendance model.
    """
    class Meta:
        model = Attendance
        fields = '__all__'
