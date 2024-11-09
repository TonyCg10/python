from typing import List

from models.animeEnum import Type, Status, Season
from models.animeSeason import AnimeSeason


class Anime:
    """
    Clase que representa un anime.

    Atributos:
        title (str): El título del anime.
        anime_type (Type): El tipo de anime.
        status (Status): El estado del anime.
        tags (List[str]): Lista de etiquetas para el anime.
        episodes (int): Número de episodios del anime.
        anime_season (AnimeSeason): La temporada del anime.
        picture (str): URL de la imagen del anime.
        sources (List[str]): Lista de fuentes del anime.
    """

    def __init__(
        self,
        title: str,
        anime_type: Type,
        status: Status,
        tags: List[str],
        episodes: int,
        anime_season: AnimeSeason = None,
        picture: str = None,
        sources: List[str] = None,
    ):
        """
        Inicializa una nueva instancia de la clase Anime.
        """
        self.title = title
        self.anime_type = anime_type
        self.status = status
        self.tags = tags
        self.episodes = episodes
        self.anime_season = anime_season
        self.picture = picture
        self.sources = sources

    @classmethod
    def from_dict(cls, data):
        """
        Crea una instancia de Anime a partir de un diccionario de datos.
        Args: data (dict): Diccionario con los datos del anime.
        Returns: Anime: Una instancia de la clase Anime.
        """
        anime_season = None
        if "animeSeason" in data:
            anime_season = AnimeSeason(
                year=data["animeSeason"].get("year"),
                season=Season[data["animeSeason"].get("season").upper()],
            )

        return cls(
            title=data["title"],
            anime_type=Type[data["type"].upper()],
            status=Status[data["status"].upper()],
            tags=data["tags"],
            episodes=data["episodes"],
            anime_season=anime_season,
            picture=data.get("picture"),
            sources=data.get("sources"),
        )

    def update(self, other_anime):
        """
        Actualiza los atributos del anime con los de otro anime.

        Args:
            other_anime (Anime): Otra instancia de Anime para actualizar los datos.
        """
        self.title = other_anime.title
        self.anime_type = other_anime.anime_type
        self.status = other_anime.status
        self.tags = other_anime.tags
        self.episodes = other_anime.episodes
        self.anime_season = other_anime.anime_season
        self.picture = other_anime.picture
        self.sources = other_anime.sources

    def __str__(self):
        """
        Devuelve una representación en cadena del anime.
        """
        return f"Anime = {self.title}, {self.anime_type}, {self.status}, {self.tags}, {self.episodes}, {self.anime_season}"

    def __eq__(self, other):
        """
        Compara dos instancias de Anime en base a su título.
        """
        if isinstance(other, Anime):
            return self.title.lower() == other.title.lower()
        return False

    def format_anime(self) -> str:
        """
        Devuelve una cadena con los detalles formateados del anime.

        Returns:
            tr: Detalles formateados del anime.
        """
        return (
            f"\nTítulo: {self.title}\n"
            f"Tipo: {self.anime_type.name}\n"
            f"Episodios: {self.episodes}\n"
            f"Estado: {self.status.name}\n"
            f"Temporada: {self.anime_season.season.name if self.anime_season else 'N/A'}, {self.anime_season.year if self.anime_season else 'N/A'}\n"
            f"Imagen: {self.picture if self.picture else 'N/A'}\n"
            f"Etiquetas: {', '.join(self.tags)}\n"
            f"Fuentes: {', '.join(self.sources) if self.sources else 'N/A'}\n"
            f""
        ).strip()
