#from scapy.all import *
'''a=IP(ttl=10) #ttl:time to live for 10sec
print(a)
print(a.src)'''

'''
a.dst="192.168.1.1"
print(a)
print(a.src)
#print(a.show())

del(a.ttl)
print(a.show())
b=IP()
print(b.show())
'''
'''c=IP()/TCP()
print(c.show())
d=Ether()/IP()/TCP()
print(d.show())
e=IP()/TCP()/"GET / HTTP/1.0\r\n\r\n" #GET is request
print(e.show())'''

'''j=a=Ether()/IP(dst="www.slashdot.org")/TCP()/"GET/index.html HTTP/1.0 \n\n"
#ether details are capturing ,ip is for source and destination and reading the dns,tcp-transforing the packet to the destination by the 'get' request
print(hexdump(j))'''

'''k=IP(dst="www.slashdot.org/40") #/30 is netmasking-->Netmasks. Netmasks (or subnet masks) are a shorthand for referring to ranges of consecutive IP addresses in the Internet Protocol. They used for defining networking rules in e.g. routers and firewalls.
dst=Net("www.slashdot.org/40")
print([p for p in k])'''

'''import pexpect
print(pexpect.run("echo hello"))
print('hello')

child=pexpect.spawn("echo")'''


'''
import psutil
import time
UPDATE_DELAY=1
def get_size(bytes):
    """
    returns a size of bytes in a nice format
    """
    for unit in ['','K','M','G','T','P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

        io=psutil.net_io_counters()
        bytes_sent,bytes_recv=io.bytes_sent,io.bytes_recv

while True:
    time.sleep(UPDATE_DELAY)
    io_2=psutil.net_io_counters()
    us,ds=io_2.bytes_sent,io_2.bytes_recv
    print(f"upload: {get_size(io_2.bytes_sent)}"
    f",Download:{get_size(io_2.bytes_recv)}"
    f",upload speed:{get_size(us/UPDATE_DELAY)}/s"
    f",Download speed:{get_size(ds/UPDATE_DELAY)}/s  ",end="\r")
    bytes_sent,bytes_recv=io_2.bytes_sent,io_2.bytes_recv'''





import psutil
import time
import os
import pandas as pd

UPDATE_DELAY = 1 # in seconds

def get_size(bytes):
    """
    Returns size of bytes in a nice format
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

# get the network I/O stats from psutil on each network interface
# by setting `pernic` to `True`
io = psutil.net_io_counters(pernic = True) #pernic :: per NIC

while True:
    # sleep for `UPDATE_DELAY` seconds
    time.sleep(UPDATE_DELAY)
    # get the network I/O stats again per interface
    io_2 = psutil.net_io_counters(pernic = True)
    # initialize the data to gather (a list of dicts)
    data = []
    for iface, iface_io in io.items() :
        # new - old stats gets us the speed
        upload_speed, download_speed = io_2[iface].bytes_sent - iface_io.bytes_sent, io_2[iface].bytes_recv - iface_io.bytes_recv
        data.append({
            "iface": iface, "Download": get_size(io_2[iface].bytes_recv),
            "Upload": get_size(io_2[iface].bytes_sent),
            "Upload Speed": f"{get_size(upload_speed / UPDATE_DELAY)}/s",
            "Download Speed": f"{get_size(download_speed / UPDATE_DELAY)}/s",
        })
    # update the I/O stats for the next iteration
    io = io_2
    # construct a Pandas DataFrame to print stats in a cool tabular style
    df = pd.DataFrame(data)
    # sort values per column, feel free to change the column
    df.sort_values("Download", inplace=True, ascending=False)
    # clear the screen based on your OS
    os.system("cls") if "nt" in os.name else os.system("clear")#display the each code line by line
    # print the stats
    print(df.to_string())





module ultraconfig - interfaces
    {

        yang - version 1.1;

    namespace
    "http://ultraconfig.com.au/ns/yang/ultraconfig-interfaces";

    prefix if;

    organization
    "Ultra Config Pty Ltd";

    contact
    "Support: <https://ultraconfig.com.au/contact/>";

    description
    "This YANG module has been created for the purpose of a tutorial.
    It
    defines
    the
    model
    for a basic ethernet interface";

    revision "2020-01-03" {
    description
    "Initial Revision";
    reference
    "Learn YANG - Full Tutorial for Beginners";
    }

    typedef dotted-quad {
    type string {
    pattern
    '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}'
    + '([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])';
    }
    description
    "Four octets written as decimal numbers and
    separated with the '.' (full stop) character.";
    }

    container interfaces {
    list interface {
    key "name";
    leaf name {
    type string;
    mandatory "true";
    description
    "Interface name. Example value: GigabitEthernet 0/0/0";
    }
    leaf address {
    type dotted-quad;
    mandatory "true";
    description
    "Interface IP address. Example value: 10.10.10.1";
    }
    leaf subnet-mask {
    type dotted-quad;
    mandatory "true";
    description
    "Interface subnet mask. Example value: 255.255.255.0";
    }
    leaf enabled {
    type boolean;
    default "false";
    description
    "Enable or disable the interface. Example value: true";
    }
    }
    list interface-state {
    config false;
    key "name";
    leaf name {
    type string;
    description
    "Interface name. Example value: GigabitEthernet 0/0/0";
    }
    leaf oper-status {
    type enumeration {
    enum up;
    enum down;
    }
    mandatory "true";
    description
    "Describes whether the interface is physically up or down";
    }
    }
    }
    }