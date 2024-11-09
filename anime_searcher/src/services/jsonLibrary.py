import json
from typing import List

from models.anime import Anime


class JsonLibrary:
    """
    Clase para manejar una biblioteca de animes en formato JSON.
    """

    def __init__(self) -> None:
        """
        Inicializa una nueva instancia de la clase JsonLibrary.
        """
        self.anime: List[Anime] = []

    def get_anime(self) -> List[Anime]:
        """
        Devuelve la lista de animes.

        Returns:
            List[Anime]: Lista de animes.
        """
        return self.anime

    def load_data(self, from_path: str) -> bool:
        """
        Carga datos desde un archivo JSON.

        Args:
            from_path (str): Ruta al archivo JSON.

        Returns:
            bool: True si los datos se cargaron correctamente, False si hubo un error.
        """
        try:
            with open(from_path, "r", encoding="utf-8-sig") as file:
                data = json.load(file)
                self.anime = [
                    Anime.from_dict(anime_data) for anime_data in data["data"]
                ]
                return True
        except (json.JSONDecodeError, FileNotFoundError, IOError) as e:
            print("ERROR")
            print(e)
            return False
