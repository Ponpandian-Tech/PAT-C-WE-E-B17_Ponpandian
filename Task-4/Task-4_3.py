num = [10, 501, 22, 37, 100, 999, 87, 351]

def is_happy(n):
    seen = []
    while n != 1 and n not in seen:
        seen.append(n)
        total = 0
        for digit in str(n):
            total += int(digit) ** 2
        n = total
    return n == 1

count = 0
for n in num:
    if is_happy(n):
        count += 1

print("Total Happy Numbers:", count)
