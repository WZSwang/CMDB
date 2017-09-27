from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def server(request):
    print("已接收到来自客户端的数据")
    server_dict = json.loads(request.body.decode('utf-8'))
    print(type(server_dict),server_dict)


    return HttpResponse("OK")