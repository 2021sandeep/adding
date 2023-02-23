birthdays = {"Meghana":"Feb 26","Keerthana":"Dec 3","Nandini":"Aug 24"}
option = 'y'
while(option == 'y'):
    name = input("Enter the name: ")
    if name in birthdays:
            print("{} birthday is on {}".format(name,birthdays[name]))
    else:
        print("{} is not present in the list".format(name))
        birthdays[name] = input("Please provide the birthdate: ")
        print("Updated birthdays data: ",birthdays)
    option = input("Do you want to continue press 'Y' or 'N' : ")