def pretty_answ_for_films(api_response):
    answ = []
    if api_response["nameRu"]:
        answ.append(f"Название фильма на русском - { api_response['nameRu']} ")
    if api_response["nameOriginal"]:
        answ.append(f"Оригинальное название - {api_response['nameOriginal']} ")
    if api_response["genres"]:
        answ.append(
            f"Жанр/Жанры {','.join([x['genre'] for x in api_response['genres']])}"
        )
    if api_response["countries"]:
        answ.append(
            f"Страна/Страны {','.join([x['country'] for x in api_response['countries']])}"
        )

    if api_response["year"]:
        answ.append(f"Год выхода - {api_response['year']} ")

    if api_response["ratingKinopoisk"]:
        answ.append(f"Рейтинг на кинопоиске - {api_response['ratingKinopoisk']} ")

    if api_response["posterUrl"]:
        answ.append(f"ссылка на постер - {api_response['posterUrl']} ")
    return answ
