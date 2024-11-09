from models.animeEnum import Season


class AnimeSeason:
    """
    Clase que representa la temporada de un anime.

    Atributos:
        _year (int): El año de la temporada.
        _season (Season): La estación del año de la temporada.
    """

    def __init__(self, year: int, season: Season):
        """
        Inicializa una nueva instancia de la clase AnimeSeason.

        Args:
            year (int): El año de la temporada.
            season (Season): La estación del año de la temporada.
        """
        self._year = year
        self._season = season

    @property
    def year(self) -> int:
        """
        Devuelve el año de la temporada.
        """
        return self._year

    @property
    def season(self) -> Season:
        """
        Devuelve la estación de la temporada.
        """
        return self._season

    def __str__(self):
        """
        Devuelve una representación en cadena de la temporada del anime.

        Returns:
            str: Representación en cadena de la temporada.
        """
        return f"AnimeSeason(year={self._year}, season={self._season.name})"
