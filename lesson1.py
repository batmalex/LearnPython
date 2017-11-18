import json
def get_answer(question, answers):
    answer = answers.get(question, "Я тебя не понял")
    return(answer)

def learn_bot(new_name, new_answer):
    answers[new_name] = new_answer

answers = {"привет": "И тебе!", "как дела?": "Ниче так", "чем занят": "питон ботаю"}

print(json.dumps(answers, ensure_ascii=False))

with open("answers.json", "r", encoding='utf-8') as f:
    print(json.loads(f.read()))
    # f.write(json.dumps(answers, ensure_ascii=False))

# print("Для выхода введите Q")
# while True:
#     question = input("Вы:").lower()
#     if question == "q":
#         break
#     elif question == "/new":
#         new_name = input("Новый вопрос: ")
#         new_answer = input("Новый ответ: ")
#         learn_bot(new_name, new_answer)
#     else:
#         val = get_answer(question, answers)
#         print("Бот:" + val)
