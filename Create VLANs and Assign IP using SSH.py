from netmiko import ConnectHandler
iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.20',
    'username': 'cisco',
    'password': 'cisco',
    'secret' : 'cisco',
}
net_connect = ConnectHandler(**iosv_l2)
net_connect.enable()
output = net_connect.send_command("show ip int br")
print(output)
config_commands = ['int vlan 5', 'ip add 5.5.5.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print(output)
for n in range (10, 20):
    print("Creating VLAN " + str(n))
    config_commands = ['vlan ' + str(n), 'name DevOps_VLAN ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print(output)