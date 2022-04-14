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

    // Get mode of radio
    function get_wireless_radio_mode() {
        $.ajax({
            url: '/get_radio_mode',
            data : {radio_num: "2", csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
            type: 'post',
            success: function(data) {
                if (data["value"] == "sta") {
                    $("#wireless_mode").html("Station");
                } else if (data["value"] == "ap") {
                    $("#wireless_mode").html("AP");
                }
                
            },
        });  
    }

    // Get dhcp client
    function get_dhcp_client_list() {
        $.ajax({
            url: '/get_dhcp_client_list',
            data : {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
            type: 'post',
            success: function(data) {
                information = "";
                /**
                 *      <tr>
                        <th scope="row">1</th>
                        <td>Mark</td>
                        <td>Otto</td>
                        <td>@mdo</td>
                        </tr>
                 */
                $('#table tbody').empty();
                count = 1
                data["value"].forEach(function(item, index) {
                    information = "";
                    information += "<tr>";
                    information += "<th scope='row'>"+ count +"</th>";
                    information += "<td>"+ item["name"] +"</td>";
                    information += "<td>"+ item["timestamp"] +"</td>";
                    information += "<td>"+ item["mac_address"] +"</td>";
                    information += "<td>"+ item["ip"] +"</td>";
                    information += "</tr>";
                    $('#table tbody').append(information);
                    count = count + 1;
                });

            },
        });
    }

    // Hardware
    function get_model_name() {
        $.ajax({
            url: '/get_model_name',
            data : {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
            type: 'post',
            success: function(data) {
                $("#mode_name").html(data["value"]);
            },
        });  
    }

    function get_pi_sn() {
        $.ajax({
            url: '/get_pi_sn',
            data : {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
            type: 'post',
            success: function(data) {
                $("#serial_number").html(data["value"]);
            },
        });  
    }

    function get_cpu_core() {
        $.ajax({
            url: '/get_cpu_core',
            data : {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
            type: 'post',
            success: function(data) {
                $("#core_count").html(data["value"]);
            },
        });  
    }

    function get_linux_infomation() {
        $.ajax({
            url: '/get_linux_infomation',
            data : {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
            type: 'post',
            success: function(data) {
                $("#linux_version").html(data["value"]);
            },
        });  
    }
    
    function get_pi_router_os_version() {
        $.ajax({
            url: '/get_pi_router_os_version',
            data : {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
            type: 'post',
            success: function(data) {
                $("#pi_router_os_version").html(data["value"]);
            },
        });
    }

    function get_cpu_usage_percent() {
        $.ajax({
            url: '/get_cpu_usage_percent',
            data : {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value},
            type: 'post',
            success: function(data) {
                $("#cpu_usage_percent").html(data["value"]+"%");
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
        get_wireless_radio_mode();
        get_dhcp_client_list();
        get_model_name();
        get_pi_sn();
        get_cpu_core();
        get_linux_infomation();
        get_pi_router_os_version();
        get_cpu_usage_percent();
    }

    setInterval(update, 1000);
});