import random
from anime import Type, Status
from anime_season import Season
from json_library import Json_Library
from library import Library

loader = Json_Library()
loaded = loader.load_data("../assets/anime-offline-database-minified.json")
library = Library()
library.animes = loader.get_anime()


def get_status(status_str):
    status = None
    status_str = status_str.upper()
    if status_str == Status.FINISHED.name:
        status = Status.FINISHED
    elif status_str == Status.ONGOING.name:
        status = Status.ONGOING
    elif status_str == Status.UNKNOWN.name:
        status = Status.UNKNOWN
    elif status_str == Status.UPCOMING.name:
        status = Status.UPCOMING
    return status


def get_season(season_str):
    season = None
    season_str = season_str.upper()
    if season_str == Season.FALL.name:
        season = Season.FALL
    elif season_str == Season.SPRING.name:
        season = Season.SPRING
    elif season_str == Season.SUMMER.name:
        season = Season.SUMMER
    elif season_str == Season.UNDEFINED.name:
        season = Season.UNDEFINED
    elif season_str == Season.WINTER.name:
        season = Season.WINTER
    return season


def get_tags(tags_str):
    return tags_str.split(",")


def get_year(year_str):
    return int(year_str)


def get_type(type_str):
    type_ = None
    type_str = type_str.upper()
    if type_str == Type.TV.name:
        type_ = Type.TV
    elif type_str == Type.MOVIE.name:
        type_ = Type.MOVIE
    elif type_str == Type.SPECIAL.name:
        type_ = Type.SPECIAL
    elif type_str == Type.ONA.name:
        type_ = Type.ONA
    elif type_str == Type.OVA.name:
        type_ = Type.OVA
    elif type_str == Type.UNKNOWN.name:
        type_ = Type.UNKNOWN
    return type_


def search_by_titles(library, title):
    anime_list = library.take_anime_contain_title(title)
    return "\n".join(anime.title for anime in anime_list)


def search_by_title(library, title):
    anime_list = library.take_anime_equal_title(title)
    return "\n".join(anime.title for anime in anime_list)


def search_by_criteria(library, type_search, year_search, season_search, status_search, tags_search, limit):
    search_result = library.take_anime_list(
        type_search, season_search, year_search, status_search, tags_search
    )

    if limit > 0:
        search_result = search_result[:limit]

    return "\n".join(anime.title for anime in search_result)


def get_random_anime(loader):
    anime_list = loader.get_anime()
    if not anime_list:
        return "No anime available."

    random_anime = random.choice(anime_list)
    return str(random_anime)
