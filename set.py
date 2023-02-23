'''L=[1,2,2,3,4,5,4,4,5,5,6,7]
L1=set(L)
print(list(L1))

L= ['aaa','red','round','ccc','road','orange']
L1=[]
for i in L:
    if len(i)>=3 and i.startswith('r'):
        L1.append(i)
print(L1)'''
def remove_adjacent(nums):
    nums1 = list()
    nums1.append(nums[0])
    for item in nums:
        if item != nums1[-1]:
            nums1.append(item)
    return nums1
nums=[1,2,3,4,4,5,5,5]