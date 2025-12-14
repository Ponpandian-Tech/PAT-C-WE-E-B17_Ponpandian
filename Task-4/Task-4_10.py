num = [4, 2, -3, 1, 6]

for i in range(len(num)):
    total = 0
    for j in range(i, len(num)):
        total += num[j]
        if total == 0:
            print("Sub-list with sum zero exists")
            exit()

print("No sub-list with zero sum")