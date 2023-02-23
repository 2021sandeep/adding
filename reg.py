import  re
'''pattern="^a...s$"  # 5 charector string
test_result='abyss'   #5 charecter string
result=re.match(pattern,test_result)
if result:
    print("search successfully")
else:
    print("search unsucsessfully")


pattern="^a...s$"    # 5 charecter string
test_result="abysss" # 6 charecter string
result=re.match(pattern,test_result)
if result:
    print(" search succes fully ")
else:
    print("search unsucces fully")'''


input_str="thhhhe film titanic was released in 1998"
result=re.match(r"[abc]",input_str)
print(result)

