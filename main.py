import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

from parsers import (
    get_all_genres,
    get_all_countries,
    get_ids_by_genre,
    get_ids_by_countries,
    get_films_by_params,
)
from make_pretty_answ import pretty_answ_for_films
from secrets import BOT_TOKEN

COUNTRY, YEAR, PREDICT = range(3)


async def genre_choice(update, context) -> int:
    reply_keyboard = [
        [x, ]
        for x in sorted(get_all_genres())
    ]

    await update.message.reply_text(
        "Привет, я бот, который может предложить фильм тебе\n"
        "Для этого тебе надо будет ответить на несколько вопросов, чтобы мой подбор был точнее \n"
        "Отправь /cancel чтобы отменить выбор.\n"
        "Итак, для начала, фильм какого жанра ты хочешь посмотреть:",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,
            one_time_keyboard=True,
            input_field_placeholder="genre choice",
        ),
    )

    return COUNTRY


async def country_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    text = update.message.text
    context.user_data["genre_choice"] = text
    country_choices_keyboard = [
        [
            x,
        ]
        for x in get_all_countries()
    ]
    await update.message.reply_text(
        "Отлично, идем дальше, теперь выбери страну производства \n"
        "также можешь отправить команду /skip_country, чтобы пропустить этот параметр",
        reply_markup=ReplyKeyboardMarkup(
            country_choices_keyboard,
            one_time_keyboard=True,
            input_field_placeholder="genre choice",
        ),
    )

    return YEAR


async def year_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    text = update.message.text
    context.user_data["country_choice"] = text
    await update.message.reply_text(
        "Теперь отправь целое число - минимальный год, старше которого должен быть фильм\n",
        reply_markup=ReplyKeyboardRemove(),
    )

    return PREDICT


async def get_predict(update, context):
    user = update.message.from_user
    year_text = update.message.text
    try:
        if int(year_text) not in range(1910, 2022):
            await update.message.reply_text(
                "Ты нам назвал плохое число, мы его учитывать не будем",
            )
    except ValueError as e:
        await update.message.reply_text(
            "Ты нам назвал вообще не число, мы его учитывать не будем",
        )
    context.user_data["year_choice"] = year_text
    params = list()
    params.append(("genres", get_ids_by_genre(context.user_data["genre_choice"])))
    if context.user_data["country_choice"]:
        params.append(
            ("countries", get_ids_by_countries(context.user_data["country_choice"]))
        )
    if context.user_data["year_choice"]:
        params.append(
            ("yearFrom", get_ids_by_countries(context.user_data["country_choice"]))
        )
    response = get_films_by_params(params)
    if not response:
        await update.message.reply_text(
            "Фильма с такими параметрами на нашлось, попробуй другой набор фильтров"
        )
        return ConversationHandler.END
    else:
        res = "\n".join(pretty_answ_for_films(response))
        await update.message.reply_text(res)
        return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    await update.message.reply_text(
        "Пока, надеюсь вернешься к нам снова", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("film", genre_choice)],
        states={
            COUNTRY: [
                MessageHandler(filters.Text(get_all_genres()), country_choice),
            ],
            YEAR: [MessageHandler(filters.Text(get_all_countries()), year_choice)],
            PREDICT: [MessageHandler(filters.Text(), get_predict)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    application.add_handler(conv_handler)
    application.run_polling()


if __name__ == "__main__":
    main()