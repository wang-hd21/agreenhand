from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

import json
# Create your views here.


def index(request):
    resp = {}
    if 'msg' in request.GET:
        print(request.GET)
        resp['ans'] = 'whd'
    return JsonResponse(resp)