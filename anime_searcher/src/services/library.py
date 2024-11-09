from typing import List

from models.animeEnum import Type, Status
from models.anime import Anime
from models.animeSeason import AnimeSeason


class Library:
    """
    Clase para manejar una colección de animes.
    """

    def __init__(self) -> None:
        """
        Inicializa una nueva instancia de la clase Library.
        """
        self.animes: List[Anime] = []

    def add_anime(self, anime: Anime) -> None:
        """
        Añade un anime a la colección. Si el anime ya existe, lo actualiza.

        Args:
            anime (Anime): El anime a añadir o actualizar.
        """
        index = next(
            (i for i, a in enumerate(self.animes) if a.title == anime.title), -1
        )
        if index == -1:
            self.animes.append(anime)
        else:
            self.animes[index].update(anime)

    def delete_anime(self, title: str) -> None:
        """
        Elimina un anime de la colección por su título.

        Args:
            title (str): El título del anime a eliminar.
        """
        self.animes = [
            anime for anime in self.animes if anime.title.lower() != title.lower()
        ]

    def take_anime_equal_title(self, title: str) -> List[Anime]:
        """
        Devuelve una lista de animes que coinciden con el título dado.

        Args:
            title (str): El título del anime a buscar.

        Returns:
            List[Anime]: Lista de animes que coinciden con el título.
        """
        return [anime for anime in self.animes if title.lower() == anime.title.lower()]

    def take_anime_contain_title(self, title: str) -> List[Anime]:
        """
        Devuelve una lista de animes que contienen la cadena del título dado.

        Args:
            title (str): La cadena del título del anime a buscar.

        Returns:
            List[Anime]: Lista de animes que contienen la cadena del título.
        """

        return [anime for anime in self.animes if title.lower() in anime.title.lower()]

    def take_anime_list(
        self,
        tipo: Type,
        temporada: AnimeSeason,
        year: int,
        estado: Status,
        etiquetas: List[str],
    ) -> List[Anime]:
        """
        Devuelve una lista de animes que coinciden con los criterios dados.

        Args:
            tipo (Type): El tipo de anime a buscar.
            temporada (AnimeSeason): La temporada del anime a buscar.
            year (int): El año del anime a buscar.
            estado (Status): El estado del anime a buscar.
            etiquetas (List[str]): Las etiquetas del anime a buscar.

        Returns:
            List[Anime]: Lista de animes que coinciden con los criterios.
        """
        anime_list = []
        for anime in self.animes:
            if tipo and tipo != anime.anime_type:
                continue
            if temporada and temporada != anime.anime_season.season:
                continue
            if year and year != anime.anime_season.year:
                continue
            if estado and estado != anime.status:
                continue
            if etiquetas and not self.find_all_tag(etiquetas, anime.tags):
                continue
            anime_list.append(anime)
        return anime_list

    def find_all_tag(self, tags: List[str], anime_tags: List[str]) -> bool:
        """
        Verifica si todas las etiquetas dadas están presentes en las etiquetas del anime.

        Args:
            tags (List[str]): Las etiquetas a buscar.
            anime_tags (List[str]): Las etiquetas del anime.

        Returns:
            bool: True si todas las etiquetas están presentes, False en caso contrario.
        """
        return all(tag in anime_tags for tag in tags)
