people = [
    {"name": "Ram", "age": 20},
    {"name": "Sam", "age": 16},
    {"name": "Ravi", "age": 25}
]

adults = list(filter(lambda p: p["age"] >= 18, people))
names = list(map(lambda p: p["name"], adults))

print(names)