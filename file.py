#write mode
'''age=input("enter age:")

f=open("data.txt","w")
f.write(age)
f.close()

# read mode

f=open("data.txt","r")
print(f.read())
f.close()

f=open("hello.txt","w")
if f:
    print("hello its meeee")
print(type(f))
f.close()
f=open("hello.txt","w+")
if f.readable():
    print('hello its mee')
f.close()


f=open("helloo.txt")
f.close()'''

import os
print(os.path.isfile("hello.txt"))

