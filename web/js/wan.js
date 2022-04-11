$(function() {
    // Wireless
    function get_wireless_ip() {
        $.ajax({
            url: '/get_ip',
            data : {iface_name: "wlan2", csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
            type: 'post',
            success: function(data) {
                $("#wireless_ip_address").html(data["value"]);
            },
        }); 
    }

    function get_wireless_channel() {
        $.ajax({
            url: '/get_wireless_channel',
            data : {iface_name: "wlan2", csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
            type: 'post',
            success: function(data) {
                $("#wireless_channel").html(data["value"]);
            },
        }); 
    }

    function get_wireless_essid() {
        $.ajax({
            url: '/get_essid',
            data : {iface_name: "wlan2", csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
            type: 'post',
            success: function(data) {
                $("#client").html(data["value"]);
            },
        }); 
    }

    function get_wireless_bitrate() {
        $.ajax({
            url: '/get_bitrate',
            data : {iface_name: "wlan2", csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
            type: 'post',
            success: function(data) {
                $("#wireless_bitrate").html(data["value"]+"bps");
            },
        }); 
    }

    function get_wireless_ap_mac_addr() {
        $.ajax({
            url: '/get_ap_mac_addr',
            data : {iface_name: "wlan2", csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
            type: 'post',
            success: function(data) {
                $("#wireless_mac_address").html(data["value"]);
            },
        }); 
    }

    function get_wireless_quility() {
        $.ajax({
            url: '/get_quility',
            data : {iface_name: "wlan2", csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
            type: 'post',
            success: function(data) {
                $("#wireless_quility").html(data["value"]);
            },
        }); 
    }

    function get_wireless_netmask() {
        $.ajax({
            url: '/get_netmask',
            data : {iface_name: "wlan2", csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
            type: 'post',
            success: function(data) {
                $("#wireless_netmask").html(data["value"]);
            },
        }); 
    }

    // Ethernet
    function get_ethernet_ip() {
        $.ajax({
            url: '/get_ip',
            data : {iface_name: "br-lan", csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
            type: 'post',
            success: function(data) {
                $("#ethernet_ip_address").html(data["value"]);
            },
        }); 
    }

    function get_ethernet_mac_address() {
        $.ajax({
            url: '/get_mac_address',
            data : {iface_name: "br-lan", csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
            type: 'post',
            success: function(data) {
                $("#ethernet_mac_address").html(data["value"]);
            },
        }); 
    }

    function get_ethernet_netmask() {
        $.ajax({
            url: '/get_netmask',
            data : {iface_name: "br-lan", csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
            type: 'post',
            success: function(data) {
                $("#ethernet_netmask").html(data["value"]);
            },
        }); 
    }

    // Update
    function update() {
        get_wireless_ip();
        get_wireless_channel();
        get_wireless_essid();
        get_wireless_bitrate();
        get_wireless_ap_mac_addr();
        get_wireless_quility();
        get_wireless_netmask();
        get_ethernet_ip();
        get_ethernet_mac_address();
        get_ethernet_netmask();
        
    }

    setInterval(update, 1000);
});