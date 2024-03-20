# imports
from django.db import models


class Department(models.Model):
    """
    Represents a department within an organization.

    Attributes:
        name (CharField): Name of the department.
        location (CharField): Location of the department.
    """
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(models.Model):
    """
    Represents an employee's role in the organization.

    Attributes:
        name (CharField): Name of the role.
    """
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """
    Represents an employee.

    Attributes:
        first_name (CharField): Employee's first name.
        last_name (CharField): Employee's last name.
        dept (ForeignKey): Department employee belongs to.
        salary (IntegerField): Employee's salary.
        bonus (IntegerField): Employee's bonus.
        role (ForeignKey): Employee's role.
        phone (IntegerField): Employee's phone number.
        hire_date (DateField): Employee's hire date.
    """
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name,)


class Attendance(models.Model):
    """
    Represents an employee's attendance record.

    Attributes:
        employee (ForeignKey): The employee this record belongs to.
        date (DateField): The date of the attendance.
        in_time (DateTimeField): The clock-in time.
        out_time (DateTimeField): The clock-out time, optional.

    Constraints:
        unique_together: Ensures unique attendance entries per employee per day.
    """
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    in_time = models.DateTimeField()
    out_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('employee', 'date')

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.date}"
