#Author: A.Batmazov
#21/11/2017
#Функция сравнивает строки

def compare_string(string1, string2):
    if string1 == string2:
        return 1
    elif string1 != string2 and len(string1) > len(string2):
        return 2
    elif string1 != string2 == "learn":
        return 3

# string1 = input("Введите строку 1")
# string2 = input("Введите строку 2")
# x = compare_string(string1, string2)
# print(x)