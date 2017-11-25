#1. Валера
# guys = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
# for guy in guys:
#     if guy == "Валера":
#         print("Валера нашелся")
#         break
# else:
#     print("Тут нет Валеры")

#2. Поиск по имени
# def find_person(name, guys):
#     for guy in guys:
#         if guy == name:
#             print(name, " нашелся")
#             break
#     else:
#         print("В списке нет имени ", name)
#
# guys = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
# find_person("Валера", guys)

#3. Как дела - Хорошо
# def ask_user():
#     while True:
#         answer = input("Как дела? ")
#         if answer == "Хорошо":
#             break
# ask_user()

#4. Как дела - Пока

def get_answer():
    while True:
        answer = input("Ответ: ")
        return answer

def ask_user():
    while True:
        try:
            ask = input("Вопрос: ")
            if ask == "Пока!":
                break
            answer = get_answer()
        except KeyboardInterrupt:
            print("Bye-bye")
ask_user()




