import json
from typing import List

from anime import Anime


class Json_Library:
    def __init__(self) -> List[Anime]:
        self.anime: List[Anime] = []

    def get_anime(self) -> List[str]:
        return [str(anime) for anime in self.anime]

    def load_data(self, from_path):
        try:
            with open(from_path, "r", encoding="utf-8-sig") as file:
                data = json.load(file)
                self.anime = data["data"]
                return True
        except Exception as e:
            print("ERROR")
            print(e)
            return False
