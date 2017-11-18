def get_answer(question, answers):
    answer = answers.get(question, "Я тебя не понял")
    return(answer)

answers = {"привет": "И тебе!", "как дела?": "Ниче так", "чем занят": "С тобой базарю"}

print("Для выхода введите Q")
while True:
    question = input("Вы:").lower()
    if question == "q":
        break
    else:
        val = get_answer(question, answers)
        print("Бот:" + val)