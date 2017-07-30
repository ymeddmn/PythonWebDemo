from django.shortcuts import render

'''
判断请求方法是否正确
'''


def checkRequestMethon(request, method):
    return request.method == method
