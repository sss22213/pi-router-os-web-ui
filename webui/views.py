from django.shortcuts import render
from django.http import HttpResponse
import json
import sys
import os

sys.path.append('/root/pi-router-os-web-ui/pi-router-os-core/networkinfo/scripts')
import netdevice
import wireless
import wireless_uci
import dhcp_list
import hw_info

net = netdevice.netdevice()
wire = wireless.wireless()
wire_uci = wireless_uci.wireless_uci()
dhcp_client_list = dhcp_list.dhcp_list()
hardware_info = hw_info.raspi_hw_info()

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

def get_radio_mode(request):
    res = {"name":"get_radio_mode", "value":{}, "res":200}
    radio_num = request.POST.get('radio_num')
    if wire_uci.get_wireless_mode(int(radio_num)) == "-1":
        res["res"] = 400
    else:
        res["value"] = wire_uci.get_wireless_mode(int(radio_num))
    return HttpResponse(json.dumps(res), content_type='application/json')


def get_dhcp_client_list(request):
    res = {"name":"get_dhcp_client_list", "value":{}, "res":200}
    res["value"] = dhcp_client_list.get_dhcp_list()
    return HttpResponse(json.dumps(res), content_type='application/json')

'''
def get_sys_infomation(request):
    res = {"name":"get_sys_infomation", "value":{}, "res":200}
    process = os.popen('cat /proc/cpuinfo')
    preprocessed = process.read()
    print(preprocessed)
    process.close()
    return HttpResponse(json.dumps(res), content_type='application/json')
'''


# Hardware
def get_model_name(request):
    res = {"name":"get_model_name", "value":{}, "res":200}
    res["value"] = hardware_info.get_model_name()
    return HttpResponse(json.dumps(res), content_type='application/json')

def get_cpu_core(request):
    res = {"name":"get_cpu_core", "value":{}, "res":200}
    res["value"] = hardware_info.get_cpu_core()
    return HttpResponse(json.dumps(res), content_type='application/json')

def get_pi_sn(request):
    res = {"name":"get_pi_sn", "value":{}, "res":200}
    res["value"] = hardware_info.get_pi_sn()
    return HttpResponse(json.dumps(res), content_type='application/json')

def get_cpu_core(request):
    res = {"name":"get_cpu_core", "value":{}, "res":200}
    res["value"] = hardware_info.get_cpu_core()
    return HttpResponse(json.dumps(res), content_type='application/json')

def get_linux_infomation(request):
    res = {"name":"get_linux_infomation", "value":{}, "res":200}
    res["value"] = hardware_info.get_linux_infomation()
    return HttpResponse(json.dumps(res), content_type='application/json')

def get_pi_router_os_version(request):
    res = {"name":"get_pi_router_os_version", "value":{}, "res":200}
    res["value"] = hardware_info.get_pi_router_os_version()
    return HttpResponse(json.dumps(res), content_type='application/json')

def get_cpu_usage_percent(request):
    res = {"name":"get_cpu_usage_percent", "value":{}, "res":200}
    res["value"] = hardware_info.get_cpu_usage_percent()
    return HttpResponse(json.dumps(res), content_type='application/json')
    