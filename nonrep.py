def find_non_repeated(lst):
    non_repeated = []
    for i in range(len(lst)):
        duplicate = False
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                duplicate = True
                break
        if not duplicate:
            non_repeated.append(lst[i])
    return non_repeated

lst = [1, 2, 3, 2, 4, 3, 5, 6, 7, 8, 9, 10, 9]
print(find_non_repeated(lst))
