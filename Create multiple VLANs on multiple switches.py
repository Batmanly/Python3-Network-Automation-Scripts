import getpass
import telnetlib

user = input("Enter your username :")
password = getpass.getpass()
f = open("switches.txt")
for IP in f:
    print("Configuring Switch " + IP)
    tn = telnetlib.Telnet(IP)
    tn.read_until(b"Username: ")
    tn.write(user.encode("ascii") + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"conf t\n")
    for n in range(2, 10):
        tn.write(b"vlan " + str(n).encode("ascii") + b"\n")
        tn.write(b"name DATA_VLAN_" + str(n).encode("ascii") + b"\n")
    tn.write(b"end\n")
    tn.write(b"show vlan br\n\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode("ascii"))
