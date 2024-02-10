from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from DashboardApp.models import Category, Tag, Item
from DashboardApp.serializers import CategorySerializer, TagSerializer, ItemSerializer

from django.core.files.storage import default_storage


@csrf_exempt
def dashboardApi(request,id=0):
    if request.method=='GET':
        items = Item.objects.all()
        items_serializer=ItemSerializer(items,many=True)
        return JsonResponse(items_serializer.data,safe=False)
    elif request.method=='POST':
        item_data=JSONParser().parse(request)
        items_serializer=ItemSerializer(data=item_data)
        if items_serializer.is_valid():
            items_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        item_data=JSONParser().parse(request)
        item=Item.objects.get(ItemId=item_data['ItemId'])
        items_serializer=ItemSerializer(item,data=item_data)
        if items_serializer.is_valid():
            items_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        item=Item.objects.get(ItemId=id)
        item.delete()
        return JsonResponse("Deleted Successfully",safe=False)
