from enum import Enum


class Season(Enum):
    SPRING = 1
    SUMMER = 2
    FALL = 3
    WINTER = 4
    UNDEFINED = 5


class AnimeSeason:
    def __init__(self, year: int, season: Season):
        self._year = year
        self._season = season
