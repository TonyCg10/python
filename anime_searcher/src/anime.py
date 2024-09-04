from enum import Enum
from typing import List
from anime_season import AnimeSeason


class Type(Enum):
    TV = 1
    MOVIE = 2
    OVA = 3
    ONA = 4
    SPECIAL = 5
    UNKNOWN = 6


class Status(Enum):
    FINISHED = 1
    ONGOING = 2
    UPCOMING = 3
    UNKNOWN = 4


class Anime:
    def __init__(
        self,
        title: str,
        type: Type,
        status: Status,
        tags: List[str],
        episodes: int,
        anime_season: AnimeSeason = None,
    ):
        self.title = title
        self.type = type
        self.status = status
        self.tags = tags
        self.episodes = episodes
        self.anime_season = anime_season

    def update(self, other_anime):
        self.title = other_anime.title
        self.type = other_anime.type
        self.status = other_anime.status
        self.tags = other_anime.tags
        self.episodes = other_anime.episodes
        self.anime_season = other_anime.anime_season

    def __str__(self):
        return f"Anime = {self.title}, {self.type}, {self.status}, {self.tags}, {self.episodes}, {self.anime_season}"

    def __eq__(self, other):
        if isinstance(other, Anime):
            return self.title.lower() == other.title.lower()
        return False
