from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Привет, чувак!'
    print(text)
    update.message.reply_text(text)

def get_answer(question, answers):
    answer = answers.get(question, "Я тебя не понял")
    return answer

def talk_to_me(bot, update):
    user_text = update.message.text
    # logging.info(user_text)
    reply = get_answer(user_text, answers)
    update.message.reply_text(reply)

def calc_to(bot, update):
    calc_exp = update.message.text
    calc_res = int(calc_exp)
    update.message.reply_text(str(calc_res))

answers = {"привет": "И тебе привет!", "как дела?": "нормуль", "чем занят": "питон ботаю"}

def main():
    updater = Updater("463877086:AAHCvtUEy-Jn4wv0flSkNdgH5-dddWNuccY")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("calc", calc_to))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    logging.info("Bot started")
    main()

# HI HOME!