# def calculate_age(birth_year, birth_month, birth_day):
    
#     current_time = time.localtime()

#     age =  current_time.tm_year - birth_year - 1

#     if current_time.tm_mon > birth_month or (current_time.tm_mon == birth_month and current_time.tm_mday >= birth_day):
#         age += 1

#     return age 

# birth_day = int(input("ingrese el dia de su nacimiento: "))
# birth_month = int(input("ingrese el mes de su nacimiento: "))
# birth_year = int(input("ingrese el año de su nacimiento: "))

# age = calculate_age(birth_year, birth_month, birth_day)


# print(f"usted tiene {age} años.")
from datetime import datetime

def calculate_age(birthday):
    today = datetime.now()
    years_difference = today.year - birthday.year

    if today.month < birthday.month or (today.month == birthday.month and today.day < birthday.day):
        years_difference -= 1

    return years_difference

def main():
    try:
        day = int(input("Día: "))
        month = int(input("Mes: "))
        year = int(input("Año: "))

        birthday = datetime(year, month, day)
        age = calculate_age(birthday)

        print(f"Usted tiene {age} años.")

    except ValueError:
        print("Error: Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
