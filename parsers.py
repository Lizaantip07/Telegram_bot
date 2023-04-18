from random import choice

import requests
from typing import List

from secrets import API_KEY


def get_all_genres() -> List[str]:
    with requests.Session() as session:
        headers = {"X-API-KEY": API_KEY}
        with session.get(
            "https://kinopoiskapiunofficial.tech/api/v2.2/films/filters",
            headers=headers,
        ) as response:
            response_json = response.json()
            answered_genres = []
            for key, value in response_json.items():
                if key == "genres":
                    for data in value:
                        answered_genres.append(data["genre"])
    return answered_genres


def get_genres_by_ids(ids: List[int]) -> List[str]:
    with requests.Session() as session:
        headers = {"X-API-KEY": API_KEY}
        with session.get(
            "https://kinopoiskapiunofficial.tech/api/v2.2/films/filters",
            headers=headers,
        ) as response:
            response_json = response.json()
            answered_genres = []
            for key, value in response_json.items():
                if key == "genres":
                    genre_by_id = {}
                    for data in value:
                        if data["id"] in ids:
                            answered_genres.append(data["genre"])
    return answered_genres


def get_ids_by_genre(genres: List[str]) -> List[int]:
    with requests.Session() as session:
        headers = {"X-API-KEY": API_KEY}
        with session.get(
            "https://kinopoiskapiunofficial.tech/api/v2.2/films/filters",
            headers=headers,
        ) as response:
            response_json = response.json()
            answered_ids = []
            for key, value in response_json.items():
                if key == "genres":
                    for data in value:
                        if data["genre"] in genres:
                            return data["id"]


def get_all_countries() -> List[str]:
    with requests.Session() as session:
        headers = {"X-API-KEY": API_KEY}
        with session.get(
            "https://kinopoiskapiunofficial.tech/api/v2.2/films/filters",
            headers=headers,
        ) as response:
            response_json = response.json()
            answered_countries = []
            for key, value in response_json.items():
                if key == "countries":
                    for data in value:
                        answered_countries.append(data["country"])
    return answered_countries


def get_countries_by_ids(ids: List[int]) -> List[str]:
    with requests.Session() as session:
        headers = {"X-API-KEY": API_KEY}
        with session.get(
            "https://kinopoiskapiunofficial.tech/api/v2.2/films/filters",
            headers=headers,
        ) as response:
            response_json = response.json()
            answered_countries = []
            for key, value in response_json.items():
                if key == "countries":
                    for data in value:
                        if data["id"] in ids:
                            answered_countries.append(data["country"])
    return answered_countries


def get_ids_by_countries(countries: List[str]) -> List[int]:
    with requests.Session() as session:
        headers = {"X-API-KEY": API_KEY}
        with session.get(
            "https://kinopoiskapiunofficial.tech/api/v2.2/films/filters",
            headers=headers,
        ) as response:
            response_json = response.json()
            answered_ids = []
            for key, value in response_json.items():
                if key == "countries":
                    for data in value:
                        if data["country"] in countries:
                            return data["id"]


def get_films_by_params(params) -> dict:
    base_url = f"https://kinopoiskapiunofficial.tech/api/v2.2/films/?type=FILM&"
    for param_name, value in params:
        base_url += f"{param_name}={value}&"
    print(base_url)
    with requests.Session() as session:
        headers = {"X-API-KEY": API_KEY}
        with session.get(base_url, headers=headers) as response:
            if response.json()["items"]:
                random_film = choice(response.json()["items"])
                return random_film
            else:
                return None


def get_tv_series_by_params(params) -> dict:
    base_url = f"https://kinopoiskapiunofficial.tech/api/v2.2/films/?type=TV_SERIES&"
    for param_name, value in params:
        base_url += f"{param_name}={value}&"
    print(base_url)
    with requests.Session() as session:
        headers = {"X-API-KEY": API_KEY}
        with session.get(base_url, headers=headers) as response:
            if response.json()["items"]:
                random_tv_series = choice(response.json()["items"])
                return random_tv_series
            else:
                return None
