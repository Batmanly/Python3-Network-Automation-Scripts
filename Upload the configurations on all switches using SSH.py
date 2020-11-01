from netmiko import ConnectHandler
switch1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.21',
    'username': 'cisco',
    'password': 'cisco',
    'secret' : 'cisco',
}
switch2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.22',
    'username': 'cisco',
    'password': 'cisco',
    'secret' : 'cisco',
}
switch3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.23',
    'username': 'cisco',
    'password': 'cisco',
    'secret' : 'cisco',
}
switches = [switch1, switch2, switch3]
with open('config_change.txt') as f:
    lines = f.read().splitlines()
    print(lines)
    for devices in switches:
        net_connect = ConnectHandler(**devices)
        net_connect.enable()