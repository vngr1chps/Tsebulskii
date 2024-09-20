import random
a = int(input('Введите первое число '))
b = int(input('Введите второе число '))

random_choice = random.randint(1, 4)

if random_choice == 1:
    print(a + b)
elif random_choice == 2:
    print(a - b)
elif random_choice == 3:
    print(a * b)
else:
    print(a / b)