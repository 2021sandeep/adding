strings = ["hello", "world"]

for i in range(len(strings)):
    first_letter = chr(ord(strings[i][0]) - 32)
    rest_of_string = strings[i][1:]
    strings[i] = first_letter + rest_of_string

print(strings)



strings = ["hello", "world"]

for i in range(len(strings)):
    strings[i] = strings[i][1:].capitalize() + strings[i][0].upper() + strings[i][1:]

print(strings)

