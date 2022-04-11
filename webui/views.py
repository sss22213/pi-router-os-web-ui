from django.shortcuts import render
from django.http import HttpResponse
import json
import sys

sys.path.append('/root/pi-router-os-web-ui/pi-router-os-core/networkinfo/scripts')
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

def get_ip(request):
    res = {"name":"ip", "value":{}, "res":200}
    iface = request.POST.get('iface_name')
    if net.is_interface(iface) == True:
        try:
            ip = net.get_ip_addr(iface)
            res["value"] = ip
        except:
            res["res"] = 404
    else:
        res["res"] = 404

    return HttpResponse(json.dumps(res), content_type='application/json')

def get_netmask(request):
    res = {"name":"netmask", "value":{}, "res":200}
    iface = request.POST.get('iface_name')
    if net.is_interface(iface) == True:
        try:
            netmask = net.get_netmask(iface)
            res["value"] = netmask
        except:
            res["res"] = 404
    else:
        res["res"] = 404
    return HttpResponse(json.dumps(res), content_type='application/json')

def get_mac_address(request):
    res = {"name":"mac_address", "value":{}, "res":200}
    iface = request.POST.get('iface_name')
    if net.is_interface(iface) == True:
        try:
            mac_address = net.get_mac_address(iface)
            res["value"] = mac_address
        except:
            res["res"] = 404
    else:
        res["res"] = 404
    return HttpResponse(json.dumps(res), content_type='application/json')

def get_wireless_channel(request):
    res = {"name":"channel", "value":{}, "res":200}
    iface = request.POST.get('iface_name')
    if net.is_interface(iface) == True:
        try:
            if wire.is_wireless(iface) == True:
                try:
                    freq, channel = wire.get_freq_channel(iface)
                    res["value"] = channel
                except:
                    res["res"] = 404
            else:
                res["res"] = 404
        except:
            res["res"] = 404
    else:
        res["res"] = 404
    return HttpResponse(json.dumps(res), content_type='application/json')

def get_essid(request):
    res = {"name":"essid", "value":{}, "res":200}
    iface = request.POST.get('iface_name')
    if net.is_interface(iface) == True:
        try:
            if wire.is_wireless(iface) == True:
                try:
                    essid = wire.get_essid(iface)
                    res["value"] = essid
                except:
                    res["res"] = 404
            else:
                res["res"] = 404
        except:
            res["res"] = 404
    else:
        res["res"] = 404
    return HttpResponse(json.dumps(res), content_type='application/json')

def get_bitrate(request):
    res = {"name":"bitrate", "value":{}, "res":200}
    iface = request.POST.get('iface_name')
    if net.is_interface(iface) == True:
        try:
            if wire.is_wireless(iface) == True:
                try:
                    bitrate = wire.get_bitrate(iface)
                    res["value"] = bitrate
                except:
                    res["res"] = 404
            else:
                res["res"] = 404
        except:
            res["res"] = 404
    else:
        res["res"] = 404
    return HttpResponse(json.dumps(res), content_type='application/json')

def get_ap_mac_addr(request):
    res = {"name":"ap_mac_address", "value":{}, "res":200}
    iface = request.POST.get('iface_name')
    if net.is_interface(iface) == True:
        try:
            if wire.is_wireless(iface) == True:
                try:
                    ap_mac_address = wire.get_ap_mac_addr(iface)
                    res["value"] = ap_mac_address
                except:
                    res["res"] = 404
            else:
                res["res"] = 404
        except:
            res["res"] = 404
    else:
        res["res"] = 404
    return HttpResponse(json.dumps(res), content_type='application/json')

def get_quility(request):
    res = {"name":"get_quility", "value":{}, "res":200}
    iface = request.POST.get('iface_name')
    if net.is_interface(iface) == True:
        try:
            if wire.is_wireless(iface) == True:
                try:
                    get_quility = wire.get_quility(iface)
                    res["value"] = get_quility
                except:
                    res["res"] = 404
            else:
                res["res"] = 404
        except:
            res["res"] = 404
    else:
        res["res"] = 404
    return HttpResponse(json.dumps(res), content_type='application/json')