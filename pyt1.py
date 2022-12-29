##write a program to read n inputs and prints a list containing the first and last three inputs
list_n=1,2,3,4,5,6,7,8,9
list_n1=list_n[0:3]+list_n[6:9]
print(list_n1)
#swap cases input=PyThOn
n=input("enter the string")
is_upper=n[0:1].isupper()
print(is_upper)
print(n.lower())
#convert dd-mm-yy format to dd/mm/yy
a="dd-mm-yy"
print(a.replace("-","/"))
#palindrome
n=input("enter any string")
if (n==n[::-1]):
    print("yes")
else:
    print("no")
#valid password or not.psw should contain atleast one lower,upper,special char,digit
psw=input("enter any password")
if psw:
    print("valid")
else:
    print("invalid")

#slicing
a="waterfall"
part=a[0:7:2]
print(part)

#isdigit
is_digit="456".isdigit()
print(is_digit)

#strip
mobile=" 9876 54321 "
mobile=mobile.strip()  # for removing space b/w num : mobile=mobile.replace(" ","")
print(mobile)

name=",..,,ravi,,..."
name=name.strip(",.")
print(name)

#replace

sentence="teh cat and teh dog"
sentence=sentence.replace("teh","the")
print(sentence)

#startswith
url="https://onthegomodal.com"
is_secure_url=url.startswith("https://")
print(is_secure_url)

#endswith
gmail_id="yasmin786@gmail.com"
is_gmail=gmail_id.endswith("@gmail.com")
print(is_gmail)

#write a program to print the given N inputs in reverse order
name="hello world"  #
rev=name[::-1]      #
print(rev)          #

#take a list,your program should creat new list with all the elements in existing list that are greater than given num
l1=[6,8,9,5,24,12,42,34]
n=int(input())
for i in l1:
    if(n<i):
        print(i)

#valid password or not

p="Pass@word1"
a=False
b=False
c=False
d=False
for i in p:
    if i.isdigit():
       a=True
    if i.isupper():
          b= True
    if i.islower():
             c=True
    if i=='@':
      d=True
if a and b and c and d:
    print("valid")
else:
    print("invalid")






