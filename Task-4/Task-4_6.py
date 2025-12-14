list1 = [1, 2, 3, 4]
list2 = [3, 4, 5]
list3 = [4, 6, 7]

duplicates = []

for n in list1:
    if n in list2 and n in list3:
        duplicates.append(n)

print("Duplicates in all lists:", duplicates)
