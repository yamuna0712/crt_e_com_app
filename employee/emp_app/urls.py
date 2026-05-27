from django.urls import path
from .views import add_employee, get_employee_details, get_employee_by_id, delete_by_id

urlpatterns = [
    path("add_emp/", add_employee),
    path("get_data/", get_employee_details),
    path("get_emp/<int:emp_id>/", get_employee_by_id),
    path("delete_by_id/<int:emp_id>", delete_by_id)
]