from rest_framework import serializers

# Register your serializers herre
from .models import *

class  EmployeeSerailizer(serializers.ModelSerializer):
    class Meta():
        model = Employee
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = '__all__'