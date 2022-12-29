from netmiko import ConnectHandler
CSR={
    "device_type":"cisco_ios",
    "ip":"sandbox-iosxe-latest-1.cisco.com",
    #"port":22,
    "username":"developer",
    "password":"C1sco12345"
}
net_connect=ConnectHandler(**CSR)
hostname=net_connect.send_command('show run | i host')
hostname.split(" ")
hostname,device,*rest=hostname.split(" ")
print("Backing up" +device)
filename="C:/Users/user675/PycharmProjects/pythonProject/Capstone/SoftwareEngineers/Developers/devices.txt"
showrun=net_connect.send_command('show run')
showvlan=net_connect.send_command('show vlan')
showver=net_connect.send_command('show ver')
log_file=open(filename,"a")
log_file.write(showrun)
log_file.write("\n")
log_file.write(showvlan)
log_file.write("\n")
log_file.write(showver)
log_file.write("\n")
net_connect.disconnect()






'''import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(s)'''
#output= <socket.socket fd=500, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>

'''from getmac import get_mac_address as gma
print(gma())'''
#output= 00:50:56:bc:c9:1c

'''import uuid
print(hex(uuid.getnode()))'''
#output= 0x5056bcc91c


'''import uuid
print("the mac address in formated way is:",end="")
print(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))
'''#output= the mac address in formated way is:00:50:56:bc:c9:1c
