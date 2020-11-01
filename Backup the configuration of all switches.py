import getpass
import telnetlib

user = input("Enter your username: ")
password = getpass.getpass()

f = open("switches.txt")

for IP in f:
    print("Taking backup of Switch " + (IP))
    tn = telnetlib.Telnet(IP)
    tn.read_until(b"Username: ")
    tn.write(user.encode("ascii") + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"terminal length 0\n")
    tn.write(b"show run\n")
    tn.write(b"exit\n")
    output = tn.read_all()
    config = open("SW"+IP,"w")
    config.write(output.decode("ascii"))
    config.write("\n")
    config.close()
    print(tn.read_all().decode("ascii"))
