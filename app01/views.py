import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from app01.GenData.GenData import *


def genRealTimeFollowRecord(request):
    ret = {}
    ret['data'] = GenRealTimeFollowData()
    ret['msg'] = 'success'
    # print(ret)

    return JsonResponse(ret)


def genVideoRecord(request):
    if request.method == 'POST':
        ret = {}
        ret["msg"] = "success"
        data = []
        param_b = request.body.decode(encoding='utf-8')
        date = json.loads(param_b)["date"]
        # print(date)
        for i in range(20):
            item = {}
            item["line"] = json.dumps(GenVideoData(date=date))
            data.append(item)
        ret["data"] = data
        return JsonResponse(ret)

def genUserActiveData(request):
    if request.method == 'POST':
        ret = {}
        ret["msg"] = "success"
        data = []
        param_b = request.body.decode(encoding='utf-8')
        date = json.loads(param_b)["date"]
        # print(date)
        for i in range(20):
            item = {}
            item["line"] = json.dumps(GenUserActiveData(date=date))
            data.append(item)
        ret["data"] = data
        return JsonResponse(ret)
