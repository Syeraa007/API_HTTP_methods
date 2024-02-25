from django.shortcuts import render

# Create your views here.
from App.serializers import *
from App.models import *
from rest_framework.views import APIView
from rest_framework.response import Response

class Boom(APIView):
    def get(self, request, pid):
        PD = Product.objects.all()
        JSD = ProductSerializer(PD, many = True)
        return Response(JSD.data)
    
    def post(self, request, pid):
        JSD1 = ProductSerializer(data = request.data)
        if JSD1.is_valid():
            JSD1.save()
            return Response({'Message':'Insertion is Done'})
        return Response({'Message':'Insertion is Invalid'})

    def put(self, request, pid):
        id = request.data['pid']
        PO = Product.objects.get(pid = id)
        UPO = ProductSerializer(PO, data = request.data)
        if UPO.is_valid():
            UPO.save()
            return Response({'Message':'Data is Updated'})
        return Response({'Message':'Data is not Update'})
    
    def patch(self, request, pid):
        id = request.data['pid']
        PO = Product.objects.get(pid = id)
        UPO = ProductSerializer(PO, data = request.data, partial = True)
        if UPO.is_valid():
            UPO.save()
            return Response({'Message':'Data is Partially Updated'})
        return Response({'Message':'Data Updation is not Done'})
    
    def delete(self, request, pid):
        PO = Product.objects.get(pid = pid)
        PO.delete()
        return Response({'Message':'Data Deletion is Done'})