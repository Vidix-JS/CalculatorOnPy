import math
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
elif str == "*":
    print(a*b)
elif str == "^":
    print(int(math.pow(a, b)))
elif str == "log":
    print(int(math.log(a,b)))
else: print("Выбрана недопустимая операция")