#install pip ifaddr

'''import ifaddr
adapters=ifaddr.get_adapters()
for adapter in adapters:
    print("IP of network adapter"+adapter.nice_name)
    for ip in adapter.ips:
        print("%s%s"%(ip.ip,ip.network_prefix))'''
import psutil as psutil
from scapy.layers.l2 import Ether

'''from SoftwareEngineers.Developers.python_networking1 import IP


import ifaddr
adapters=ifaddr.get_adapters(include_unconfigured=True)
for adapter in adapters:
    print("IP of network adapter"+adapter.nice_name)
    for ip in adapter.ips:
        print("%s%s"%(ip.ip,ip.network_prefix))
    else:
        print("no IPs configured")'''


'''import psutil
result01=psutil.cpu_times()
result02=psutil.cpu_stats()
result03=psutil.cpu_freq()
result04=psutil.disk_partitions()
result05=psutil.net_io_counters(pernic=True)#or (pernic= false ) or empty
print(result01)
print(result02)
print(result03)
print(result04)
print(result05)'''


'''import psutil
network_stats=psutil.net_io_counters(pernic=False)
bytes_sent=getattr(network_stats,'bytes_sent')
bytes_recv=getattr(network_stats,'bytes_recv')
print("bytes_sent ={0} | bytes_recv={1}".format(bytes_sent,bytes_recv))'''


'''import socket
import subprocess
import sys
from datetime import datetime
#subprocess.call('clear',shell=True)
remoteserver=input("enter a remote host to scan:")
remoteserverIP=socket.gethostbyname(remoteserver)
print("_"*60)
print("please wait,scanning remote host",remoteserverIP)
print("_"*60)
t1=datetime.now()
try:
    for port in range (1,5000):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result=sock.connect_ex((remoteserverIP,port))
        if result==0:
            print("port{}:     open".format(port()))
            sock.close()
except KeyboardInterrupt:
    print("you pressed ctrl+c")
    sys.exit()
except socket.gaierror:
    print("hostname could not be resolved.existing")
    sys.exit()
except socket.error:
    print("could'n connect to server")
    sys.exit()'''



'''import scapy.all as scapy
request =scapy.ARP()
print(request.show())'''
#print(request.summary())

'''from scapy.all import *
ip = IP ()
print(ip)
print(ip.show())

from scapy.all import *
my_frame=Ether() / IP() # ARP() OR ICMP() also can use
print(my_frame)
print(my_frame.show())'''

from scapy.all import *
s=IP(dst="google.com")/ICMP()  # ***
print(s.show())
