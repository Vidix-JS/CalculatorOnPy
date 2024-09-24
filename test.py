print("Введите тип операции: ")
str = input()
a = int(input())
b = int(input())
if str == "+":
    print(a+b)
elif str == "-":
    print(a-b)
else: print("Выбрана не та операция")