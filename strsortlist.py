list1=["biscuit","bread","cupcake","pancake","pastry"]

n=len(list1)
for i in range(n-1):
  for j in range(0,n-i-1):
    if list1[j]>list1[j+1]:
      list1[j],list1[j+1]=list1[j+1],list1[j]
print(list1)
####################################################
lis =[]
for ele in list1:
    num='p'

    if(ele[0]==num):
        lis.append(ele)
for i in list1:
    if i not in lis:
        lis.append(i)

print(lis)
###################################################
liso=[]
for ele in lis:
    num1='b'
    if(ele[0]==num1):
        liso.append(ele)
lis.extend(liso)
print(lis)








