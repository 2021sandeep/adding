'''f=open('hello.txt',mode='r',buffering=10,encoding='utf-8')
if f:
    print("opend")
print(f)'''
f=open('mytext.txt',mode='r',encoding='utf-8')
print("file name is:",f.name)
print("encoding:",f.encoding)
print("mode",f.mode)
print("file close",f.closed)     # if not close file it shown false
f.close()
print("file close",f.closed)    #if closed it shown true
