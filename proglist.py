numbers = [5, 12, 7, 3, 20]

def show_list():
    print("Список:", numbers)

def add_number():
    number = int(input("Введіть число: "))
    numbers.append(number)
    print("Число додано!")

def find_max():
    print("Найбільше число:", max(numbers))

def calculate_sum():
    print("Сума елементів:", sum(numbers))


while True:
    print("\n--- МЕНЕДЖЕР СПИСКУ ---")
    print("1. Переглянути список")
    print("2. Додати число")
    print("3. Знайти найбільше число")
    print("4. Обчислити суму")
    print("5. Вийти")

    choice = input("Оберіть дію: ")

    if choice == "1":
        show_list()
    elif choice == "2":
        add_number()
    elif choice == "3":
        find_max()
    elif choice == "4":
        calculate_sum()
    elif choice == "5":
        print("Завершення програми.")
        break
    else:
        print("Неправильний вибір!")
