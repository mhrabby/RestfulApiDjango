"""myapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Apiapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/',views.employeeList.as_view()),
    path('authority/',views.authorityList.as_view()),
    path('buyer/',views.buyerList.as_view()),
    path('employeeDetails/<str:pk>/',views.employeeDetails,name="employDetials"),
    path('search/<str:pk>/',views.SearchEmployee,name="SearchEmployee"),
    path('addEmployee',views.AddEmployee,name="AddEmployee"),
    path('updateEmployee/<str:pk>',views.UpdateEmployee,name="UpdateEmployee"),
    path('deleteEmployee/<str:pk>',views.DeleteEmployee,name="DeleteEmployee"),



]
