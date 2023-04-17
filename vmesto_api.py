from random import choice

import requests
from typing import List


def get_all_genres() -> List[str]:
    with requests.Session() as session:
        headers = {"X-API-KEY": "a8802738-0808-486c-85a6-d7fb20116e76"}
        with session.get("https://kinopoiskapiunofficial.tech/api/v2.2/films/filters", headers=headers) as response:
            response_json = response.json()
            answered_genres = []
            for key, value in response_json.items():
                if key == 'genres':
                    for data in value:
                        answered_genres.append(data['genre'])
    return answered_genres


def get_genres_by_ids(ids: List[int]) -> List[str]:
    with requests.Session() as session:
        headers = {"X-API-KEY": "8efda388-c22d-4558-baa3-0f9cacac5bd9"}
        with session.get("https://kinopoiskapiunofficial.tech/api/v2.2/films/filters", headers=headers) as response:
            response_json = response.json()
            answered_genres = []
            for key, value in response_json.items():
                if key == 'genres':
                    genre_by_id = {}
                    for data in value:
                        if data['id'] in ids:
                            answered_genres.append(data['genre'])
    return answered_genres


def get_ids_by_genre(genres: List[str]) -> List[int]:
    with requests.Session() as session:
        headers = {"X-API-KEY": "8efda388-c22d-4558-baa3-0f9cacac5bd9"}
        with session.get("https://kinopoiskapiunofficial.tech/api/v2.2/films/filters", headers=headers) as response:
            response_json = response.json()
            answered_ids = []
            for key, value in response_json.items():
                if key == 'genres':
                    for data in value:
                        if data['genre'] in genres:
                            answered_ids.append(data['id'])
    return answered_ids


# print(get_genres_by_ids([1, 8, 3]))
#
# print(get_ids_by_genre(['триллер', 'комедия']))
#
# print(get_all_genres())


def get_all_countries() -> List[str]:
    with requests.Session() as session:
        headers = {"X-API-KEY": "8efda388-c22d-4558-baa3-0f9cacac5bd9"}
        with session.get("https://kinopoiskapiunofficial.tech/api/v2.2/films/filters", headers=headers) as response:
            response_json = response.json()
            answered_countries = []
            for key, value in response_json.items():
                if key == 'countries':
                    for data in value:
                        answered_countries.append(data['country'])
    return answered_countries


def get_countries_by_ids(ids: List[int]) -> List[str]:
    with requests.Session() as session:
        headers = {"X-API-KEY": "8efda388-c22d-4558-baa3-0f9cacac5bd9"}
        with session.get("https://kinopoiskapiunofficial.tech/api/v2.2/films/filters", headers=headers) as response:
            response_json = response.json()
            answered_countries = []
            for key, value in response_json.items():
                if key == 'countries':
                    for data in value:
                        if data['id'] in ids:
                            answered_countries.append(data['country'])
    return answered_countries


def get_ids_by_countries(countries: List[str]) -> List[int]:
    with requests.Session() as session:
        headers = {"X-API-KEY": "8efda388-c22d-4558-baa3-0f9cacac5bd9"}
        with session.get("https://kinopoiskapiunofficial.tech/api/v2.2/films/filters", headers=headers) as response:
            response_json = response.json()
            answered_ids = []
            for key, value in response_json.items():
                if key == 'countries':
                    for data in value:
                        if data['country'] in countries:
                            answered_ids.append(data['id'])
    return answered_ids


# print(get_all_countries())
#
# print(get_countries_by_ids([1, 13, 9]))
#
# print(get_ids_by_countries(['США', 'Канада', 'Германия']))


def get_films_by_params(country_id: int, genre_id: int) -> dict:
    with requests.Session() as session:
        headers = {"X-API-KEY": "8efda388-c22d-4558-baa3-0f9cacac5bd9"}
        with session.get(f"https://kinopoiskapiunofficial.tech/api/v2.2/films/?countries={country_id}&genres={genre_id}", headers=headers) as response:
            random_film = choice(response.json()['items'])
            return random_film


for key in get_films_by_params(country_id=1, genre_id=1):
    if get_films_by_params(country_id=9, genre_id=5)[key] != None:
        print(f"{key}: {str(get_films_by_params(country_id=9, genre_id=5)[key]).replace('[', '').replace(']', '')}")
