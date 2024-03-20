# imports
from django import forms
from .models import Attendance, Employee


class AttendanceForm(forms.ModelForm):
    """
    Form for creating and updating Attendance records.

    Uses a ModelChoiceField for employee selection, ordered by first name, and custom widgets
    for date and time fields to enhance user interface.
    """
    employee = forms.ModelChoiceField(
        queryset=Employee.objects.all().order_by('first_name'))

    class Meta:
        model = Attendance
        fields = ['employee', 'date', 'in_time', 'out_time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'in_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'out_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control', 'required': False}),
        }
