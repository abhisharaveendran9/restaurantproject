from django.shortcuts import render

# Create your views here.
from restaurantapp.models import menu_items
from rest_framework.views import APIView
from rest_framework.response import Response

class MenuItemsView(APIView):
    def get(self,request,*args,**kwargs):
        all_items=menu_items

        if "category" in request.query_params:
            category=request.query_params.get("category")
            all_items=[item for item in menu_items if item.get("category")==category]
        if "limit" in request.query_params:
            lim=int(request.query_params.get("limit"))
            all_items=all_items[:lim]

        return Response(data=all_items)

    def post(self,request,*args,**kwargs):
        dish=request.data
        menu_items.append(dish)
        return Response(data=dish)



class MenuDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        item=[item for item in menu_items if item["code"]==id].pop()
        return Response(data=item)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=[item for item in menu_items if item["code"]==id].pop()
        #data=request.data
        instance.update(request.data)
        return Response(data=instance)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=[item for item in menu_items if item["code"]==id].pop()
        menu_items.remove(instance)
        return Response(data=instance)