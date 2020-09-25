from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from  rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.decorators import api_view


class employeeList(APIView):
    def get(self,request):
        employees = Employees.objects.all()
        serializer = EmployeesSerializer(employees, many='True')
        return Response(serializer.data)



class authorityList(APIView):
    def get(self,request):
        authority = Authority.objects.all()
        serializer = AuthoritySerializer(authority,many='True')
        return Response(serializer.data)



class buyerList(APIView):
    def get(self,request):
        buyer = Buyer.objects.all()
        serializers = BuyerSerializer(buyer,many=True)

        return Response(serializers.data)

@api_view(['GET'])
def employeeDetails(request,pk):
    employee = Employees.objects.get(emp_id=pk)
    serializer = EmployeesSerializer(employee,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def SearchEmployee(request,pk):
    employee = Employees.objects.get(firstname=pk)
    serializer = EmployeesSerializer(employee,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def AddEmployee(request):
    serializer = EmployeesSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def UpdateEmployee(request,pk):
    employee = Employees.objects.get(emp_id=pk)
    serializer = EmployeesSerializer(instance=employee, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteEmployee(request,pk):
    employee = Employees.objects.get(emp_id=pk)
    employee.delete()

    return Response("Employee Successfully Deleted")


