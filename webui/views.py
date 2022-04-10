from django.shortcuts import render
from django.http import HttpResponse
import json
import sys

sys.path.append('../pi-router-os-core/networkinfo/scripts')
import netdevice
import wireless

net = netdevice.netdevice()
wire = wireless.wireless()

# Create your views here.
def homepage(request):
    return render(request,'html/index.html')

def get_interface_list(request):
    res = {"name":"interface_name_list", "value":[], "res":200}
    for iface in net.get_interface_name():
        res["value"].append(iface)
    return HttpResponse(json.dumps(res))