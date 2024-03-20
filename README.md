
## Human Resource Management System (HRMS)

This project is a web-based Human Resource Management System designed to manage various HR tasks within an organization. It allows for adding and removing employees, marking attendance, viewing employee and department reports, and accessing an admin portal for administrative functions.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
### Prerequisites

What you need to install the software and how to install them.

- Python 3.x installed on your system (verify with `python --version` or `python3 --version`).

### Installing

A step-by-step series of examples that tell you how to get a development environment running.

#### Setting Up a Virtual Environment

**For Windows Users:**

1. Open Command Prompt and navigate to your project directory (`kredily`):
    ```
    cd path\to\kredily
    ```
2. Create the virtual environment:
    ```
    python -m venv myenv
    ```
3. Activate the virtual environment:
    ```
    .\myenv\Scripts\activate
    ```
4. When you're done working, deactivate the virtual environment:
    ```
    deactivate
    ```

**For macOS (and Linux) Users:**

1. Open Terminal and navigate to your project directory (assuming it's named `kredily`):
    ```
    cd path/to/kredily
    ```
2. Create the virtual environment:
    ```
    python3 -m venv myenv
    ```
3. Activate the virtual environment:
    ```
    source myenv/bin/activate
    ```
4. To stop using the virtual environment, deactivate it:
    ```
    deactivate
    ```

### Installing Dependencies

With the virtual environment activated, you can install the required dependencies by running:

 `cd kredily_hrms_proj`

Make sure to replace the path that contains `requirements.txt` which consists of the list of packages needed for the project.

Now, run the command:

`pip install -r requirements.txt`

Once all the packages are installed, run:

`python manage.py runserver`

Your server should be up and running on:

`http://127.0.0.1:8000/`


### Project Structure

The project consists of several key HTML templates, each serving a distinct purpose within the HRMS. Below is a brief overview of each template and its function:

1. Home Page (`home.html`): The landing page of the HRMS, displaying a list of employees.

2. Add Employee (`add_employee.html`): A form to add a new employee to the system.
3. Delete Employee (`delete_employee.html`): A page to remove an existing employee from the HRMS.
4. Employee Details (`employee_details.html`): Displays detailed information about each employee.
5. Mark Attendance (`mark_attendance.html`): Allows marking attendance for employees.
6. Attendance Details (`attendance_details.html`): Shows attendance records for employees.
7. Departments Report (`departments_report.html`): Lists departments and their employee count.
8. Static Files: The `style.css` file for custom styles applied across the application.
Each page includes a navigation bar for easy access to all sections of the HRMS. The templates use Bootstrap for styling.

### API Functionality Overview:

API endpoints developed for managing employee information and their attendance records. These endpoints allow for adding new employees, listing all employees, marking attendance for employees, and retrieving attendance details for specific employees.

### API Endpoints

1. Adding a New Employee

Endpoint: `/api/employees/`

Method: `POST`

Description: Adds a new employee with basic information.

2. Retrieve List of All Employees

Endpoint: `/api/employees/`

Method: `GET`

Description: Retrieves a list of all employees with their basic information.


3. Mark Attendance for a Specific Employee

Endpoint: `/api/attendance/`

Method: `POST`

Description: Marks attendance for a specific employee on a given date, including in-time and out-time.

4. Retrieve Attendance Details for a Specific Employee

Endpoint: `/api/attendance/<employee_id>/`

Method: `GET`

Description: Retrieves attendance details for a specific employee.

### Additional Information

The HTML templates are designed to be integrated with a backend. The templates use Django templating language for dynamic content rendering, CSRF token for form submission security, and JavaScript fetch API for fetching and displaying data from the backend.

API endpoints in Django views ensure they return data in the correct format (e.g., JSON).


