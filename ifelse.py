#nested conditional blocks
matches_won=int(input())
goals=int(input())
if(matches_won>8):
    if(goals>20):
        print("hurray")
print("winner")


#nested condition in else block
a=2
b=2
c=5
is_a_greatest=(a>b) and (a>c)
if is_a_greatest:
    print(a)
else:
    is_b_greatest=(b>c)
    if is_b_greatest:
        print(b)
    else:
        print(c)

#############
num=int(input())
is_divisible_by_10=(num%10==0)
is_divisible_by_5=(num%5==0)
if is_divisible_by_10 :
    print("div by 10")
elif is_divisible_by_5 :
    print("div by 5")
else:
    print("not div by 10 and 5")

#write a program to print the digit in the one's place

n=input("enter any string")#n=int(input())
n1=n[-1:]
print(n1)

#num of days(N)as input.write a program to convert N to years Y weeks W and days D:1329=365 #+33 7+3
#write a program to which returns absolute difference the two given num
a=-99
print(abs(a))

######
n=int(input())
count=1
while count<n:
    print("hello")
    count+=1

#while
a=int(input())
counter=0
while counter<3:
    a=a+1
    print(a)
    counter=counter+1

##############
a=int(input())
condition=(counter<1)
while condition:
    a=a+1
    print(a)
    counter=counter+1
print("end")

#for loop
word="python"
for each_char in word:
    print(each_char)

#count of the word
word=input()
count=0
for i in range(len(word)) :
    count+=1
print(i+1)

#######
word="python"
for i in range(5,8):
  print(i)

#print solid square and rectangle

m=3 #m=int(input())
n=2 #n=int(input())
for i in range(0,m):
    for j in range(0,n):
        print("*",end=" ")
    print()
print("square pattern")

#print solid rightangle triangle

m=int(input())
for i in range(0,m):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
#print("\n")
print("rightangle triangle")

#leftangle triangle
n=int(input())
for i in range(n):
    for j in range(n-i+1):
        print(" ",end=" ")
    for k in range(i):
       print("*",end=" ")
    print()

#mirror leftangle triangle

n=4
for i in range(0,n):
    for j in range(0,n):
        if(j-i<=n):
         print("*",end=" ")
    print()

############

#sum of the given numbers
#l=[1,2,3,4,5]
n=int(input("enter any number"))
s=0
for i in range(0,n):
    s=s+i
print(s)

#product of given numbers
n=int(input())
s=1
for i in range(1,n):
    s=s*i
print(s)

#############
for i in range(2,-1):
    for j in range(2,i+j+1):
        print("*",end=" ")
    print()

