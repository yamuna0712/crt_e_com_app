import json
from http import HTTPStatus

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Emp_data


@csrf_exempt
def add_employee(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            emp_data = Emp_data.objects.create(
                emp_id=data.get("emp_id"),
                emp_name=data.get("emp_name"),
                emp_email=data.get("emp_email"),
                emp_salary=data.get("emp_salary"),
                emp_phone=data.get("emp_phone"),
                emp_address=data.get("emp_address"),
                emp_joindate=data.get("emp_joindate"),
                emp_gender=data.get("emp_gender"),
                emp_age=data.get("emp_age"),
                emp_dept=data.get("emp_dept"),
                emp_experience=data.get("emp_experience"),
            )

            return JsonResponse({
                "emp_id": emp_data.emp_id,
                "message": "Employee added successfully"
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST allowed"}, status=405)
def get_employee_details(request):
    emp_data = Emp_data.objects.all().values()
    response_data=list(emp_data)
    return JsonResponse({
        "data": response_data,
        "status": HTTPStatus.OK
    })
def get_employee_by_id(request, emp_id):
    '''takes id as
    input through url and returns
    the data of that user'''
    try:
        emp = Emp_data.objects.get(emp_id=emp_id)

        response_data = {
            "emp_id": emp.emp_id,
            "emp_name": emp.emp_name,
            "emp_email": emp.emp_email,
            "emp_salary": emp.emp_salary,
            "emp_phone": emp.emp_phone,
            "emp_address": emp.emp_address,
            "emp_joindate": emp.emp_joindate,
            "emp_gender": emp.emp_gender,
            "emp_age": emp.emp_age,
            "emp_dept": emp.emp_dept,
            "emp_experience": emp.emp_experience,
        }

        return JsonResponse({
            "data": response_data,
            "status": HTTPStatus.OK
        })

    except Emp_data.DoesNotExist:
        return JsonResponse({
            "error": "Employee not found"
        }, status=404)
@csrf_exempt
def delete_by_id(request, emp_id):
    emp=Emp_data.objects.get(emp_id=emp_id)
    emp.delete()
    return JsonResponse({
        "message": "Employee deleted successfully",
        "status": HTTPStatus.OK
    })