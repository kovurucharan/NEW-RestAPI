from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employees
from .serializers import employeesSerializer
from rest_framework.decorators import api_view


# class EmployeeList(APIView):
#     def get(self, request):
#         employee= Employees.objects.all()
#         serilizer = employeesSerializer(employee, many=True)
#         return Response(serilizer.data)
#
#         def post(self):
#             pass
@api_view(['GET'])
def Emplist(request):
    emp=Employees.objects.all()
    serializer=employeesSerializer(emp,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Emp_details(request,id):
    emp=Employees.objects.get(id=id)
    serializer=employeesSerializer(emp,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def Emp_create(request):
    serializer=employeesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def Emp_update(request,id):
    emp=Employees.objects.get(id=id)
    serializer=employeesSerializer(instance=emp,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def Emp_delete(request,id):
    emp=Employees.objects.get(id=id)
    emp.delete()
    return Response("Deleted SuccessFully")












