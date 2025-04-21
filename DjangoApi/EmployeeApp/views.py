from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Departments, Employees
from .serializers import DepartmentSerializer, EmployeeSerializer

#for files default storage
from django.core.files.storage import default_storage

# Create your views here.


@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added record Successfully", safe=False)
        return JsonResponse("Failed to Add a record", safe=False)
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer = DepartmentSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Update record Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Record Deleted Successfully", safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)

# REST API Implementation for Employees

@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = DepartmentSerializer(Departments, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data=Employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added record Successfully", safe=False)
        return JsonResponse("Failed to Add a record", safe=False)
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Departments.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer = EmployeeSerializer(employee, data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Update record Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        employee = Departments.objects.get(DepartmentId=id)
        employee.delete()
        return JsonResponse("Record Deleted Successfully", safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)



