list=[2,2.0,7,1,8]
print(list)
n=len(list)
for i in range(n-1):
  for j in range(0,n-i-1):
    if list[j]>list[j+1]:
      list[j],list[j+1]=list[j+1],list[j]
print(list)
for i in range(len(list)):
  print(list[i])
