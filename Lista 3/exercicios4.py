def calculate_age(current_year, born_year):
    age = current_year - born_year
    return age

current_year = 2024
born_year = int(input('Digite seu ano de nascimento: '))

age = calculate_age(current_year, born_year)
print(f"Sua idade é {age} anos.")
    