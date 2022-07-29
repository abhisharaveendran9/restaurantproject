from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from productapi.models import Products
from productapi.serializers import ProductSerializer

# Create your views here.

class ProductsView(APIView):
    def get(selfself,request,*args,**kwargs):
        qs=Products.objects.all()
        #deserialzation
        serilazer=ProductSerializer(qs,many=True)
        return Response(data=serilazer.data)

    def post(self,request,*args,**kwargs):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            Products.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(date=serializer.errors)

class ProductDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Products.objects.get(id=id)
        serilaizer=ProductSerializer(qs)
        return Response(data=serilaizer.data)