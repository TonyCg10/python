class Library:
    def __init__(self):
        self.animes = []

    def add_anime(self, anime):
        index = next(
            (i for i, a in enumerate(self.animes) if a.title == anime.title), -1
        )
        if index == -1:
            self.animes.append(anime)
        else:
            self.animes[index].update(anime)

    def delete_anime(self, title):
        self.animes = [
            anime for anime in self.animes if anime.title.lower() != title.lower()
        ]

    def take_anime_contain_title(self, title):
        return [anime for anime in self.animes if title.lower() in anime.title.lower()]

    def take_anime_equal_title(self, title):
        return [
            anime for anime in self.animes if title.lower() == anime["title"].lower()
        ]

    def take_anime_list(self, tipo, temporada, year, estado, etiquetas):
        anime_list = []
        for anime in self.animes:
            if tipo and tipo != anime.type:
                continue
            if temporada and temporada != anime.anime_season.season:
                continue
            if year and year != anime.anime_season.year:
                continue
            if estado and estado != anime.status:
                continue
            if etiquetas and not self.find_all_tag(etiquetas, anime.tags):
                continue
            if etiquetas and not self.find_tag(etiquetas, anime.tags):
                continue
            anime_list.append(anime)
        return anime_list

    def find_all_tag(self, tags, anime_tags):
        return all(tag in anime_tags for tag in tags)

    def find_tag(self, tags, anime_tags):
        return any(tag in anime_tags for tag in tags)
