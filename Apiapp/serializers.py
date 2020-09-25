from rest_framework import serializers
from .models import *

class EmployeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employees
        fields = '__all__'


class AuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Authority
        fields = '__all__'



class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'
