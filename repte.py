'''def print_duplicates(lst):
    seen = {}
    duplicates = []
    for item in lst:
        if item in seen:
            duplicates.append(item)
        else:
            seen[item] = True
    return duplicates

lst = [1, 2, 3, 2, 4, 3, 5, 6, 7, 8, 9, 10, 9]
print(print_duplicates(lst))'''
#########################################################
list1=[1,2,3,5,3,2]
#print(list1)
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]==list1[j]:
            
          print(list1[i])



