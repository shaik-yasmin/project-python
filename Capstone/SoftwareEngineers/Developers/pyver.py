import sys
print(sys.version)


import socket
print(socket.gethostname())

import socket
hostname=socket.gethostname()
print(hostname)

ipadd=socket.gethostbyname(hostname)
print(ipadd)

import os
with open("ip_list.txt") as file:
    park = file.read()
    park = park.splitlines()
    print(" {park} \n")
    # ping for each ip in the file
for ip in park:
    response = os.popen(f"pinng {ip}").read()
    # saving some ping output details to output file
    if("reuest timed out." or "unreachable") in response:
        print(response)
        f=open("info_output.txt","a")
        f.Write(str(ip)+'link is down'+'\n')
        f.close()
    else:
        print(response)
        f = open("info_output.txt","a")
        f.Write(str(ip)+'is up '+'\n')
        f.close()
with open("ip_output.txt") as file:
    output = file.read()
    f.close()
    print(output)
with open("info_output.txt","w") as file:
    pass



import os,ipaddress
os.system('cls') #os.system will clear the console at the start of the execution
while True:
    ip=input("Enter ip address")
    try:
        print(ipaddress.ip_address(ip))
        print("ip valid")
    except:
        print('-'*50)
        print("ip is not valid")
    finally:
        if ip=='mango':
            print("script finished")
            break


import os
print(os.system("ipconfig"))


import socket
s=socket.socket()
print("socket successfully created")
port=40674
s.bind(('',port))
print("socket binded to %s"%(port))
s.listen(5)
print("socket is listening")
while True:
    c,addr=s.accept()
    #print(c)
    print("got connection from",addr)
    print(c)
    c.send(b"thank you for connecting")
    print(c)
    c.close()



import socket
#creat a socket object
s=socket.socket()
port=40674
s.connect(('127.0.0.1',port))
print(s.recv(1024))
s.close()




