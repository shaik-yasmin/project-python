########
def greetings():
    print("hello")
greetings()

name=input()
greetings()
print(name)
#############
def greet(word):
    msg="hello"+" "+word
    print(msg)
name=input()
greet(word=name)
############
def greet(word):
    msg="hello "+word
    print(msg)
    return msg
greet("world")
#some built-in functions print(),int(),str(),len()
def get_list(string_a):
    list_a=string_a.split(',')
    len_list_a=len(list_a)
    for i in range(len_list_a):
        list_a[i]=int(list_a[i])
    return list_a
string_a=input()
numbers_list=get_list(string_a)
print(numbers_list)
###########
def greet(arg_1,arg_2):
    print(arg_1+""+arg_2)
greeting=input()
name=input()
###########
#return the given arguments
def ret_arg(word):
    msg="hi"+word
    print(msg)
    return msg
ret_arg("hello")

#the prefilled code contain a function.write a program to concate  the msg "welcome"followed by name --"welcome hcl"
def pre_code(word):
    msg="welcome"+word
    print(msg)
    return msg
pre_code("hcl")

#wap that accepts string1,2,3,4 and it splits into list and returns square of
# each no[1,4,9,16]
'''def string_split(string):
    for i in range (len(list_a)):
        list_b=i**2
        print(list_b)
        return list_b
string_split(input)'''
def greet():
    str=input()
    l1=[]
    for i in str:
        if i.isdigit():
            l1.append(int(i)*int(i))
    print(l1)
greet()

#write the function to return second character in the word
def alpha():
    word=input()
    msg=""
    for i in range (len(word)):
        if (word[i].isalpha()):
            msg+=word[i]
    print(msg[3])
alpha()

#write a function to check if the num is divisible by 7.return true or false
def f():
    a = int(input())
    if (a%7==0):
        print("{} is div by 7".format(a))
    else:
        print("false")
f()

#write a function to return no.of lower and upper case letters in a string
def lu_case():
    lower=0
    upper=0
    a=input()
    for i in range(len(a)):
        if (a[i].islower()):
            lower+=1
        elif(a[i].isupper()):
            upper+=1
    print("upper cases are:",upper,"lower cases are:",lower)
lu_case()

#find area and parimeter of square using function
def area_perimeter_square():
    a=int(input())
    area=a**2
    perimeter=4*a
    print("area:",area)
    print("perimeter",perimeter)
area_perimeter_square()

'''write a function that takes no.of wins,draws and losses and calculate the no.of points
win=4,draws=2,loss=-1'''
def matches(win_s,low_s,draw_s):
    print(win_s,low_s,draw_s)
string_a=input()
string_b=list(string_a)
win_s=0
low_s=0
draw_s=0
for i in string_b:
    if i=='w':
        win_s+=1*4
    elif i=='1':
        low_s-=-1
    elif i=='d':
        draw_s+=1*2
total=(win_s+draw_s)+low_s
matches(win_s,low_s,draw_s)
########
def match():
    m,n,p=map(int,input("enter no.of wins,draws and loss").split(","))
    g,b,L=m*4,n*2,p*1
    total=(g+b)-L
    print(total)
match()

#if a no is is div by 3 it should return macro,if div by 5 (polo), if both 3and 5
# (macropolo or just return num)
def div_3and5():
    num=int(input())
    if num%3==0 and num%5!=0:
        print("macro")
    elif num%5==0 and num%3!=0:
        print("polo")
    elif num%3==0 and num%5==0:
        print("macropolo")
    else:
        print(num)
div_3and5()

#wap to extract the numbers in a given string and print sum,min,max of those num
#ex:c0d1n8--sum=9,min=0,max=8
def sum_min_max():
    string_s=input()
    list_a=list(string_s)
    l1=[]
    for i in list_a:
        if i.isdigit():
            l1.append(int(i))
    print(min(l1))
    print(max(l1))
    print(sum(l1))
sum_min_max()
#factorial of a num using recursion

#identify sum of first n natural numbers

#take a prefillid list.wap to remove all the occurences of the given number(N)
#in alist..print list after removing those numbers.

#write function which accepts bill amount.if bill amount is <500,discount should
#be 5% if >=500 and <2500 discount is 10%,if >=2500 discount 20%..print actual amount and discount aamount.













