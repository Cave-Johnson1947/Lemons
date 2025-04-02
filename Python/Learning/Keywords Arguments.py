def hello(greeting, title, first, last):
    print(f'{greeting}, {title} {first} {last}!')

hello('Hello', title='Mr.', last='John', first='Smith')

for x in range(1, 11):
    print(x, end=' ')

print("1", "2", "3", "4", "5", sep=' - ')

def get_phone(county, area, first, last):
    return f"{county}-{area}-{first}-{last}"

phone_number = get_phone(county='1', area='555', first='452', last='9024')

print(phone_number)