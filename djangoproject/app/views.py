from _mysql import result

from django.shortcuts import render
from app import models
from django.http import HttpResponse
import json

from app import JsonUtil, utils


def getData(request):
    query = 'select * from app_employee where age=12'
    data = models.Employee.objects.raw(raw_query=query)
    return HttpResponse(JsonUtil.toJson(12, data, False))
