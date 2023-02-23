list1=["apples","bananas","pineapple"]
shoping_list=["apples","apples","bananas","apples","pears","pineapple","pear","apples","bananas"]

list2=list1+shoping_list
print(list2)

list3={}
for i in list2:
    list3[i]=list2.count(i)
print(list3)


