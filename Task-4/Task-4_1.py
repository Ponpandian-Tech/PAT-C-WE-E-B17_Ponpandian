num = [10, 501, 22, 37, 100, 999, 87, 351]

even_list = []
odd_list = []

for n in num:
    if n % 2 == 0:
        even_list.append(n)
    else:
        odd_list.append(n)

print("Even numbers:", even_list)
print("Odd numbers:", odd_list)
