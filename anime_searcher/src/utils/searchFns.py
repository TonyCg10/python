import random

from models.animeEnum import Type, Status, Season

from services.jsonLibrary import JsonLibrary
from services.library import Library


def get_status(status_str: str) -> Status:
    """
    Devuelve el estado correspondiente a la cadena proporcionada.

    Args:
        status_str (str): La cadena del estado.

    Returns:
        Status: El estado correspondiente.
    """
    status_str = status_str.upper()
    if status_str == Status.FINISHED.name:
        return Status.FINISHED
    elif status_str == Status.ONGOING.name:
        return Status.ONGOING
    elif status_str == Status.UNKNOWN.name:
        return Status.UNKNOWN
    elif status_str == Status.UPCOMING.name:
        return Status.UPCOMING
    return None


def get_season(season_str: str) -> Season:
    """
    Devuelve la estación correspondiente a la cadena proporcionada.

    Args:
        season_str (str): La cadena de la estación.

    Returns:
        Season: La estación correspondiente.
    """
    season_str = season_str.upper()
    if season_str == Season.FALL.name:
        return Season.FALL
    elif season_str == Season.SPRING.name:
        return Season.SPRING
    elif season_str == Season.SUMMER.name:
        return Season.SUMMER
    elif season_str == Season.UNDEFINED.name:
        return Season.UNDEFINED
    elif season_str == Season.WINTER.name:
        return Season.WINTER
    return None


def get_tags(tags_str: str) -> list:
    """
    Devuelve una lista de etiquetas a partir de una cadena.

    Args:
        tags_str (str): La cadena de etiquetas separadas por comas.

    Returns:
        list: La lista de etiquetas.
    """
    return tags_str.split(",")


def get_all_tags(library: Library) -> list:
    """
    Devuelve todas las etiquetas únicas de los animes en la biblioteca.

    Args:
        library (Library): La biblioteca de animes.

    Returns:
        list: Una lista con todas las etiquetas únicas de los animes.
    """
    all_tags = set()

    for anime in library.animes:
        if hasattr(anime, "tags"):
            for tag in anime.tags:
                all_tags.add(tag)

    return sorted(list(all_tags))


def get_year(year_str: str) -> int:
    """
    Devuelve el año correspondiente a la cadena proporcionada.

    Args:
        year_str (str): La cadena del año.

    Returns:
        int: El año correspondiente.
    """
    return int(year_str)


def get_type(type_str: str) -> Type:
    """
    Devuelve el tipo correspondiente a la cadena proporcionada.

    Args:
        type_str (str): La cadena del tipo.

    Returns:
        Type: El tipo correspondiente.
    """
    type_str = type_str.upper()
    if type_str == Type.TV.name:
        return Type.TV
    elif type_str == Type.MOVIE.name:
        return Type.MOVIE
    elif type_str == Type.SPECIAL.name:
        return Type.SPECIAL
    elif type_str == Type.ONA.name:
        return Type.ONA
    elif type_str == Type.OVA.name:
        return Type.OVA
    elif type_str == Type.UNKNOWN.name:
        return Type.UNKNOWN
    return None


def search_by_titles(library: Library, title: str) -> str:
    """
    Busca animes que contengan el título proporcionado.

    Args:
        anime_library (Library): La biblioteca de animes.
        title (str): El título a buscar.

    Returns:
        str: Una cadena con los títulos encontrados.
    """
    anime_list = library.take_anime_contain_title(title)
    return "\n".join(anime.format_anime() for anime in anime_list)


def search_by_title(library: Library, title: str) -> str:
    """
    Busca animes que coincidan con el título proporcionado.

    Args:
        library (Library): La biblioteca de animes.
        title (str): El título a buscar.

    Returns:
        str: Una cadena con los detalles formateados de los animes encontrados.
    """
    anime_list = library.take_anime_equal_title(title)
    return "\n".join(anime.format_anime() for anime in anime_list)


def search_by_criteria(
    library: Library,
    type_search: Type,
    year_search: int,
    season_search: Season,
    status_search: Status,
    tags_search: list,
    limit: int,
) -> str:
    """
    Busca animes que coincidan con los criterios proporcionados.

    Args:
        anime_library (Library): La biblioteca de animes.
        type_search (Type): El tipo de anime a buscar.
        year_search (int): El año del anime a buscar.
        season_search (Season): La temporada del anime a buscar.
        status_search (Status): El estado del anime a buscar.
        tags_search (list): Las etiquetas del anime a buscar.
        limit (int): El número máximo de resultados.

    Returns:
        str: Una cadena con los títulos encontrados.
    """
    search_result = library.take_anime_list(
        type_search, season_search, year_search, status_search, tags_search
    )

    if limit > 0:
        limit = min(limit, len(search_result))
        search_result = random.sample(search_result, limit)

    return "\n".join(anime.title for anime in search_result)


def get_random_anime(loader: JsonLibrary) -> str:
    """
    Devuelve un anime aleatorio de la biblioteca.

    Args:
        loader (JsonLibrary): El cargador de la biblioteca de animes.

    Returns:
        str: La representación en cadena de un anime aleatorio.
    """
    anime_list = loader.get_anime()
    if not anime_list:
        return None

    return random.choice(anime_list)
