from enum import Enum


class Type(Enum):
    """
    Enum para los diferentes tipos de anime.
    """

    TV = 1
    MOVIE = 2
    OVA = 3
    ONA = 4
    SPECIAL = 5
    UNKNOWN = 6


class Status(Enum):
    """
    Enum para los diferentes estados de un anime.
    """

    FINISHED = 1
    ONGOING = 2
    UPCOMING = 3
    UNKNOWN = 4


class Season(Enum):
    """
    Enum para las diferentes estaciones del año.
    """

    SPRING = 1
    SUMMER = 2
    FALL = 3
    WINTER = 4
    UNDEFINED = 5
