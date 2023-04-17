import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from telegram import ReplyKeyboardMarkup
from TOKEN import BOT_TOKEN

import datetime as dt

reply_keyboard = [["/movie", "/series"]]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

GENRE_MESSAGES = {"/action": 'action', "/adventure": 'adventure', "/comedy": 'comedy',
                  "/drama": 'drama', "/fantasy": 'fantasy', "/horror": 'horror',
                  "/musicals": 'musicals', "/romance": 'romance', "/science_fiction": 'science_fiction',
                  "/thriller": 'thriller'}

COUNTRY_MESSAGES = {"/USA": 'USA', "/Russia": 'Russia', "/Canada": 'Canada',
                    "/Spain": 'Spain', "/France": 'France', "/Italy": 'Italy',
                    "/China": 'China', "/Japan": 'Japan'}

CHOICE = {'genre': [], 'country': [], 'year': []}


async def start(update, context):
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Я - бот, который поможет Вам подобрать отличный фильм или сериал! Что хотите посмотреть?",
        reply_markup=markup
    )


async def movie(update, context):
    reply_keyboard = [
        ["/yes"],
        ["/no"],
    ]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text("Вы хотите выбрать необходимые критерии?", reply_markup=markup)


async def series(update, context):
    reply_keyboard = [
        ["/yes"],
        ["/no"],
    ]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text("Вы хотите выбрать необходимые критерии?", reply_markup=markup)


async def no(update, context):
    await update.message.reply_text("Хорошо, тогда я предоставлю Вам любой фильм.", reply_markup=markup)


async def yes(update, context):
    #real_chose = 'genre'
    chat_id = update.message.text
    reply_keyboard = [
        ["/action"],
        ["/adventure"],
        ["/comedy"],
        ["/drama"],
        ["/fantasy"],
        ["/horror"],
        ["/musicals"],
        ["/romance"],
        ["/science_fiction"],
        ["/thriller"],
        ["/reset"],
    ]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text("Выберите жанр:", reply_markup=markup)


'''real_chose = 'genre'


async def add_genre(update, context):
    global real_chose
    cnt = 0
    reply_keyboard = [
        ["/yes"],
        ["/next_criterion"],
    ]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    message = update.message.text
    is_genre = GENRE_MESSAGES.get(message)
    if update.message.text == reply_keyboard[1][0] or real_chose == 'country':
        real_chose = ''
        await update.message.reply_text(f'Поехали дальше!')
        await country(update, context)
        cnt += 1
    elif cnt == 1:
        exit()
    elif real_chose == 'genre':
        CHOICE["genre"].append(is_genre)
        await update.message.reply_text(f'Вы выбрали жанр {is_genre}. Хотите выбрать ещё один жанр или перейти на следующий критерий?', reply_markup=markup)
        real_chose = 'genre'


async def ask_add_genre(update, context):
    chat_id = update.message.chat_id
    await update.message.reply_text('Хотите выбрать еще жанр?', reply_markup=markup)
    reply_keyboard = [["/да"], ["/нет"]] 
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text('Ок', reply_markup=markup)'''


async def country(update, context):
    #real_chose = 'country'
    chat_id = update.message.chat_id
    reply_keyboard = [
        ["/USA"],
        ["/Russia"],
        ["/Canada"],
        ["/Spain"],
        ["/France"],
        ["/Italy"],
        ["/China"],
        ["/Japan"],
        ["/reset"],
    ]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text("Выберите страну:", reply_markup=markup)


'''async def add_country(update, context):
    message = update.message.text
    is_country = COUNTRY_MESSAGES.get(message)
    await update.message.reply_text(f'Вы выбрали страну {is_country}.')
    CHOICE["country"].append(is_country)'''


'''async def ask_add_country(update, context):
    chat_id = update.message.chat_id
    await update.message.reply_text('Хотите выбрать еще страну?', reply_markup=markup)
    reply_keyboard = [["/да"], ["/нет"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text('Ок', reply_markup=markup)'''


async def year(update, context):
    await update.message.reply_text("Введите год:", reply_markup=markup)


async def reset(update, context):
    chat_id = update.message.chat_id
    reply_keyboard = [["/movie"], ["/series"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text('Вы вернулись в меню', reply_markup=markup)


'''def Isdigit(message):
    if 1927 <= int(message) <= 2022:
        return True
    else:
        return False'''


'''async def would_like_year(update, context):
    reply_keyboard = [["/да"], ["/нет"]]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text('Хотите выбрать еще?', reply_markup=markup)
    ms = update.message.text
    if ms == '/да':
        return True
    else:
        return False'''


async def echo(update, context):
    message = update.message.text
    is_genre = GENRE_MESSAGES.get(message)
    is_country = COUNTRY_MESSAGES.get(message)
    is_year = 0
    if CHOICE["genre"] == []:
        CHOICE["genre"].append(is_genre)

    if CHOICE["country"] == [None]:
        CHOICE['country'] = []

    if CHOICE["country"] == []:
        CHOICE["country"].append(is_country)

    if message.isdigit() and 1927 <= int(message) <= 2022:
        is_year = message
        if CHOICE["year"] == []:
            CHOICE["year"].append(is_year)

    if is_year:
        await update.message.reply_text(f'Вы выбрали год {is_year}.')

    if is_genre:
        reply_keyboard = [
            ["/country"],
        ]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text(f'Вы выбрали жанр {is_genre}.', reply_markup=markup)

    elif is_country:
        reply_keyboard = [
            ["/year"],
        ]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text(f'Вы выбрали страну {is_country}.', reply_markup=markup)

    if CHOICE["genre"] != [] and CHOICE["country"] != [] and CHOICE["year"] != []:
        print(CHOICE)


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("movie", movie))
    application.add_handler(CommandHandler("series", series))
    application.add_handler(CommandHandler("no", no))
    application.add_handler(CommandHandler("yes", yes))
    #application.add_handler(MessageHandler(filters.TEXT, add_genre))
    application.add_handler(CommandHandler("country", country))
    #application.add_handler(MessageHandler(filters.TEXT, add_country))
    application.add_handler(CommandHandler("year", year))
    application.add_handler(CommandHandler("reset", reset))
    application.add_handler(MessageHandler(filters.TEXT, echo))
    application.run_polling()


if __name__ == '__main__':
    main()




