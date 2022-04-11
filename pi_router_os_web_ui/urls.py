"""pi_router_os_web_ui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webui.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('get_sensor_update_time', get_interface_list),
    path('get_ip', get_ip),
    path('get_netmask', get_netmask),
    path('get_mac_address', get_mac_address),
    path('get_wireless_channel', get_wireless_channel),
    path('get_essid', get_essid),
    path('get_bitrate', get_bitrate),
    path('get_ap_mac_addr', get_ap_mac_addr),
    path('get_quility', get_quility),
]
