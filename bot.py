from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
# import ephem as ep


def greet_user(bot, update):
    text = 'Привет, чувак!'
    print(text)
    update.message.reply_text(text)


def new_function():
    answer = '555'
    talk_to_me(answer)
    # return answer
#


def talk_to_me(bot, update, questioon):
    # question = update.message.text
    # logging.info(user_text)
    # reply = get_answer(question, answers)
    update.message.reply_text(questioon)


answers = {"привет": "И тебе привет!", "как дела?": "нормуль", "чем занят": "питон ботаю"}


# Показывает созвездие в котором находится планета в настоящий момент

# planets = {"mars": ep.Mars(ep.now())}
#
# def planet_info(bot, update, args):
#     print(args)
#     # start_text = "Введите название планеты"
#     # update.message.reply_text(start_text)
#     planet = update.message.text
#     planet = planet[len("/planet "):]
#     print(planet)
#     update.message.reply_text(ep.constellation(planets[planet[1]]))

# def wordcount(bot, update):
#     users_input = update.message.text
#     users_input = users_input[len('/wordcount'):].lstrip()
#     print(users_input)
#     count = 0
#     string_start = 0
#     word_start = 0
#
#     for word in users_input:
#         if word in ('"', '«', '“') and string_start == 0:
#             string_start = 1
#         elif word in ('"', '»', '”') and string_start == 1:
#             string_start = 0
#             word_start = 0
#         else:
#             if not word.isspace() and string_start == 1:
#                 if word_start == 0:
#                     word_start = 1
#                     count += 1
#                 elif word_start == 1:
#                     pass
#             if word.isspace() and string_start == 1:
#                 if word_start == 1:
#                     word_start = 0
#     update.message.reply_text(count)

def main():
    updater = Updater("463877086:AAHCvtUEy-Jn4wv0flSkNdgH5-dddWNuccY")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    # dp.add_handler(CommandHandler("planet", planet_info, pass_args=True))
    # dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_args))

    updater.start_polling()
    updater.idle()

    new_function()


if __name__ == "__main__":
    logging.info("Bot started")
    main()