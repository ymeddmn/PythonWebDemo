from django.shortcuts import render
from django.http import HttpResponse
from app import utils, JsonUtil


def getCode(request):
    code = 200
    des = ''
    success = True;
    item = {}
    body = []
    if utils.checkRequestMethon(request, 'POST'):
        phone = request.POST.get('phone')
        resCode = phone[0:4]
        print(resCode)
        item.setdefault('checkCode', resCode)
        body.append(item)
        print(body)
    else:
        success = False
        code = 0
        des = '请求方法错误'
    if success:
        return HttpResponse(JsonUtil.toResultJson(code, body, '成功').encode('utf-8'))
    else:
        return HttpResponse(JsonUtil.toResultJson(code, body, des).encode('utf-8'))
