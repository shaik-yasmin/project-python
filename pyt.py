# print addition of two numbers
print(667+87+54)
#print length of string
a='string'
print(len(a))
#print "python is amazing",use tab space and new line characters
print("python is amazing")
#read two strings in two different variables,concat them and print
print("shaik"+"yasmin")
print(type(2))
print(type(9.5))
print(type(2+2j))
a=[5,6]
print(type(a))
#############################################################
alpha = 'abcdefghijklmnopqrstuvwxyz'
print(list(alpha))
print(tuple(alpha))
print(set(alpha))
print("python is \namazing   ")
#######################################################
s1='hi'
s2='hlo'
s3=s1+s2
print(len(s3))
################################################################
a=20
b=6
print(a/b)
print(a//b)
print(id("hello"))
#referring the same object
list_a = [1,2,3,4]
list_b = [1,2,3,4]
print(id(list_a))
print(id(list_b))
list_b[0] = 5
print((list_a))
print((list_b))
a= (9,9)
a += (8.9,"hi")
print(a)
#compound assignment example
list_a = [1,2]
list_b = list_a
list_a = list_a+[6,7]
print(str(list_a))
print(str(list_b))
list_a = [1,2]
list_b = [3,list_a]
list_a[1] = 4
print((list_a))
print((list_b))
#splitting a string
numbers="1 2 3  4"
num_list = numbers.split()
print(num_list);
#slicing and indexing strings
string_1 = "program"
string_2 = string_1[6:0:-2]
print(string_2)
list_a = [1,2,3,4]
list_b = [1,2,3,4]
list_a = list_a[-1:4:1]
print(list_a)
#take two integers m and n ,write a program to create a list with element m repeated by n times
m=[3]
n=5

list_n="1,2,3,4,5,6,7,8,9"
x=m*n
print(x)
#write a program to read n inputs and prints a list containing the first and last three inputs
list_n1=list_n[2]+list_n[6:9]
print(list_n1)

#check if the first three char of a string are same or not
a= "ApPle"
b= "application"
if (a[:3] == b[:3]):
    print("same")
else:
    print("not same")
#####
a=input("enter first string")
b=input("enter second string")
if (a[:3] == b[:3]):
   print("same")
else:
   print("not same")

#write a program two 3 digit numbers and check if the first digit of A is less than last digit of B

A=input("enter first three digits")
B=input("enter second three digits")
if (A[:1] > B[-1:21:1]):#B[2]
    print("the first digit of A is big")
else:
    print("the last digit of B is big")

#
#write a program to read the marks in M P C.check if any of the conditions is satisfied.M>=70 and p>=60 and c>=60   M+p+C>=180
M=78
N=54
C=34
if(M>=70 and N>=60 and C>=60 or M+N+C>=180):
    print("satisfied")
else:
    print("not sat")
##################################
#to know the system version and info
import sys
print("python version")
print(sys.version)
print("version info")
print(sys.version_info)










