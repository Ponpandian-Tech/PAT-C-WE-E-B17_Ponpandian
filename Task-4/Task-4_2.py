num = [10, 501, 22, 37, 100, 999, 87, 351]

prime_list = []

for n in num:
    if n > 1:
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(n)

print("Prime numbers:", prime_list)
print("Count:", len(prime_list))
