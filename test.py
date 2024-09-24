print("Введите тип операции: ")
str = input()
print("Введите значение для первой переменной: ")
a = int(input())
print("Введите значение для второй переменной: ")
b = int(input())
if str == "+":
    print(a+b)
elif str == "-":
    print(a-b)
elif str == "/" or str == ":":
    print(a / b)
else: print("Выбрана не та операция")