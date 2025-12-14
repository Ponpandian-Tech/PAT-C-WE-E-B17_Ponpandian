num = [10, 20, 30, 9]

for i in range(len(num)):
    for j in range(i+1, len(num)):
        for k in range(j+1, len(num)):
            if num[i] + num[j] + num[k] == 59:
                print(num[i], num[j], num[k])