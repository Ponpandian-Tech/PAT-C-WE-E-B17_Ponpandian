num = [4, 5, 1, 2, 1, 4, 2]

for n in num:
    if num.count(n) == 1:
        print("First non-repeating:", n)
        break