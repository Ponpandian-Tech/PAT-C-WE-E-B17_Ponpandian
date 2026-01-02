numbers = [1, 2, 3, 4, 5, 6]

even_squares = [x*x for x in numbers if (lambda n: n % 2 == 0)(x)]

print(even_squares)