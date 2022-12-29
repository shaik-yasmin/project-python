file=open('Dummy.txt','r')
print(file.read())
print(file)
print(file.name)
file.close()

file=open('Dummy.txt','r')
print(file.readline())
print(file)
print(file.name)
file.close()

#context manager
with open('Dummy.txt','r') as file:
    print(file.readline(),end="")
    print(file.readline(),end="")
    print(file.tell())
    #print(file.readlines)

#with for loop
with open('Dummy.txt','r') as file:
    for i in file:
        print(i,end='')

with open('Dummy.txt','r') as file:
    file_content=file.read(10)
    print(file_content,end='')
    file_content=file.readline()
    print(file_content,end='')
    print(file.tell()) #tells the position in file

with open('Dummy.txt','r') as file:
    size_to_read=20
    file_contents=file.read(size_to_read)
    while len(file_contents)>0:
        print(file_contents,end='*')
        file_contents=file.read(size_to_read)

#append:it can add the data to the existing file
with open('Text.txt','a') as file:
    file.write('hi')

sampleFile=open("Text.txt",'a')
sampleFile.write("\n this should append to a file")
sampleFile.close()

#write:it can over write to the existing data
sampleFile=open("Text.txt",'w')
sampleFile.write("this should write to files")
sampleFile.close()

#creat(x):shold creat new file which is not equal to existing file
file=open('newone.txt','x')
file.write('file operations')
file.close()

file1=open('Dummy1.txt','r') as file:
file2=open('Dummy2.txt',"copying the file")

with open('Dummy1.txt','r') as file1,open ('Dummy2.txt','a') as file2:
    for i in file1:
        file2.write(i)

file1=open("Dummy1.txt",'r')
file2=open("Dummy2.txt",'a')
for i in file1:
    temp=str(i)
    file2.write(temp)
file1.close()
file2.close()

#readlines:it reads the file line by line
file=open("Dummy.txt",'r')
print(file.readlines())

#read(n):specified length of charecters
file=open("Dummy.txt",'r')
print(file.read(20))

file=open('new1.txt','r+')
file.write('Line1\n')
file.write('Line2\n')
file.close()

