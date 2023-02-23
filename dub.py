birthday={"harini":"aprial13","srivani":"oct21","ravi":"oct"}
n=(input("enter a name"))

for i in birthday:
    if i==n:
        print("birthdayis",birthday.get(n))
        break
    else:
        print("not matched than update")


        birthday.update({n:""})
month=input("enter mont")
birthday.update({n:month})
print(birthday)

