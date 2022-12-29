#None has its own data type
var=None
print(var)
print(type(var))

#Tuple is ordered sequence of items.
#Tuple is immutable object
#tuple concatenation
a=2
tuple_a=(5,"six",a,8.2)
print(tuple_a)
tuple_b=("hi",5,10.22,"hola!")
print(tuple_b)
print(tuple_a + tuple_b)

#access tuple value
print(tuple_a[2])

#string to tuple
color="red"
tuple_a=tuple(color)
print(tuple_a)
#list to tuple
list_a=[1,2,3]
tuple_a=tuple(list_a)
print(tuple_a)

#sequence to tuple
tuple_a=tuple(range(1,5))
print(tuple_a)
#in and notin
tuple_a=(1,2,3,4)
is_part=4 in tuple_a
print(is_part)

tuple_a=(2,3,4)
is_part=5 not in tuple_a
print(is_part)

list_a=[1,2,3,4]
is_part=3 in list_a
print(is_part)

word="python"
is_part='py' in word
print(is_part)

#unpacking
tuple_a=('r','e','d')
(s_1,s_2)=tuple_a
print(s_1)
print(s_2)

#packing
tuple_a=('r','e')
(s_1,s_2)=tuple_a  #s_1,s_2
print("s_1:",s_1)
print("s_2:",s_2)
##########
a=1,2,3
print(type(a))
print(a)

#no dublicates
set_a={1,3,4,3}
print(set_a)

#immmutable items
set_a={"a",["a","c"]}
print(set_a)

#creat an empty set
set_a=set()
print(type(set_a))
print(set_a)

#set conversion
set_a=set([1,2,3])
print(type(set_a))
print(set_a)

#string to set
set_a=set("python")
print(type(set_a))
print(set_a)

#tuple to set
set_a=set((2,3,4))
print(type(set_a))
print(set_a)

#as items are not ordered
set_a={1,2,3}
print(set_a[1])
print(set_[1:3])# error because set is unordered type

#add items
set_a={1,2,3,4}
set_a.add(5)
print(set_a)
set_a.update([7,6])
print(set_a)

#remove specific item
set_a={2,4,5}
set_a.remove(2)
print(set_a)

#clear a set
set_a={1,2,3}
set_a.clear()
print(set_a)

#length of set
set_a={1,2,3,4}
print(len(set_a))

#union and intersection
set_a={1,2,3}
set_b={4,5,6}
union=set_a | set_b
print(union)

###
set_a={1,2,3}
set_b={4,3}
intersection=set_a & set_b
print(intersection)

set_a={1,2,3}
list_b=[2,3]
intersection=set_a.intersection(list_b)
print(intersection)

#difference-all the elements in the first set but not in second
set_a={1,2,3}
tuple_b=(3,4,6)
diff=set_a.difference(tuple_b)
print(diff)

#symmetric -diff -->elements the two sets except common elements
set_a={1,2,3}
set_b={2,4}
symmetric_diff=set_a^set_b #symmetric_diff=set_a.symmetric_difference(set_b)
print(symmetric_diff)

#remove dublicate elements in the list
list_a=[1,2,3,4,4]
set_a=set(list_a)
print(set_a)

#to remove a list of numbers if present in the set..read inputs as comma seperated
set_a={1,2,3}
set_b={3,4,5}
diff=set_a - set_b
print(diff)

#given two lines of comma seperated integer,write a program to print the numbers that are present in both the lines
l1={1,2,3,4}
l2={3,4,5}
intersection=l1 & l2
print(intersection)

#remove the elements other than numbers in the list.ex:1,2,3,#,5,2,@,5,7,#,^
#list_a=['1','2','3','#','5','2','@','5','7','#','^']
list_a=input()
for i in list_a:
    if i.isdigit():
     print(i,end=' ')

#to check superset,subset,disjoint set
s_1={1,2,3,4,5,6}
s_2={1,2,6}
s_3={7,8,9}
is_superset=s_1.issuperset(s_2)
is_subset=s_2.issubset(s_1)
is_disjoint=s_1.isdisjoint(s_3)
print(is_superset)
print(is_subset)
print(is_disjoint)

#to print common elements in 3 sets
s_1={1,2,3}
s_2={2,4,6}
s_3={2,7,8}
intersection=s_1 & s_2 & s_3
intersection=s_1.intersection(s_2,s_3)
print(intersection)
print(intersection)

#first line contains comma separated integer.the second line of input will contain an integer(k)."5,3,7,9,5,6,2,1,8"k is 9
l_1=list(map(int,input("enter:").split(",")))
k=int(input("enter:"))
l_2=[]
for i in range(len(l_1)):
    for j in range(i+1,len(l_1)):
        if (l_1[i]+l_1[j]==k):
            l_3=[l_1[i],l_1[j]]
            l_2.append(l_3)
print(l_2)

#rotate the list d times to the left
li_a=list(map(int,input().split(" ")))
n=int(input())
for i in range(n):
    t=li_a[0]
    li_a.remove(t)
    li_a.append(t)
    print(li_a)

#rotate the list d times to the right
l_a=input()
l1=list(l_a)
#l1=list(map(int,input("enter elements:").split(" ")))
n=int(input())
for i in range(n):
    t=l1[-1]
    l1.remove(t)
    l1.insert(0,t)
    print(l1)

#read n lines of input and create a nested list each lines as a list
l1=list(map(int,input().split(" ")))
l2=list(map(int,input().split(" ")))
l3=[l1]+[l2]
l4=tuple(l3)
print(l4)


#read n lines of input and print them as list of tuples

'''character freq.the input string will contain only alphabets and whitespaces.ignore casevsensitive."Pop Up"
0:1 p:3 u:1 ,tic tac toe'''
str_a=input()
str_1=str_a.lower()
list_1=list(str_1)
setstr=set(list_1)
for i in setstr:
    if i!=' ':
        print(i+":",end="")
        print(list_1.count(i),end=" ")




#min and max values of list of tuples
#l1=(1,2,3,4,5)
l1=[(1,2,3),(4,5,6)]
l2=l1[0]+l1[1]
print(l2)
print(min(l2))
print(max(l2))

#square of keys using dictionary
#num=[2,4,6,8]
num=list(map(int,input("enter keys:").split(" ")))
dict1={}
for i in num:
    dict1[i]=i**2
print(dict1)

#perfect square
m=int(input("starts from:"))
n=int(input("ends with:"))
b=[]
for i in range(m,n):
    a=i**2
    if (a<n):
        b.append(a)
print(b)



