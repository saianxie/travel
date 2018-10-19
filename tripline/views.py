from django.shortcuts import render
import json
from datetime import datetime, timedelta
from django.http import HttpResponse, JsonResponse, response
from tripline import models

# Create your views here.

def show(request):
    pass




# 向chau表中插入这个洲的国家数据
def add(request):
    if request.method == 'POST':
        try:
            country = json.loads(request.body)
            print(type(country))
            for i in country:
                res = models.tripline.objects.filter(title=i['title']).update(img=i['img'])
                # res = models.tripline.objects.create(acount=i['account'],label=i['label'],title=i['title'],price=i['present_price'])
            return JsonResponse({"code": "800"})
        except Exception as ex:
            print(ex)
            return JsonResponse({"code": "408"})
    else:
        return JsonResponse({"code": "408"})

