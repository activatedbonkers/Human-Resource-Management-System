# imports
from django.contrib import admin
from .models import Employee, Role, Department, Attendance

# Register the Employee, Role, and Department models to make them available in the Django admin interface.
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)


class AttendanceAdmin(admin.ModelAdmin):
    """
    Custom admin interface for the Attendance model.

    Configures the display of Attendance records in the Django admin interface, including customizing
    the columns shown in the list display, adding filters for easier navigation, and enabling search
    functionality to quickly find attendance records based on employee name or date.
    """
    # Customize the columns displayed in the admin list view.
    list_display = ('employee', 'date', 'in_time', 'out_time')

    # Add filters to the side panel for narrowing down the search by employee or date.
    list_filter = ('employee', 'date')
    search_fields = ('employee__first_name',
                     'employee__last_name', 'date')


# Register the Attendance model along with its custom admin interface configuration.
admin.site.register(Attendance, AttendanceAdmin)
