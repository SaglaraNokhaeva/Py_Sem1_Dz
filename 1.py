# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
x=int(input("Введите день недели: "))
if x==6 or x==7:
    print ("да")
else:
    print ("нет")