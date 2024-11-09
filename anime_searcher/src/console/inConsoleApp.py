from services.jsonLibrary import JsonLibrary
from services.library import Library

from utils.searchFns import (
    search_by_title,
    search_by_titles,
    search_by_criteria,
    get_type,
    get_status,
    get_season,
    get_year,
    get_tags,
    get_random_anime,
)

# Inicializa el loader y carga los datos
anime_loader = JsonLibrary()
IS_LOADED = anime_loader.load_data(
    "T:/GitHub/python/anime_searcher/assets/anime-offline-database-minified.json"
)
anime_library = Library()
anime_library.animes = anime_loader.get_anime()


def main():
    """
    Función principal para interactuar con la biblioteca de animes desde la consola.
    """

    print()
    print("Bienvenido a la Biblioteca de Animes")
    while True:
        print("\nElige una opción:")
        print()
        print(" 1. Buscar animes por título")
        print(" 2. Buscar animes que contengan un título")
        print(" 3. Buscar animes por criterios")
        print(" 4. Obtener un anime aleatorio")
        print(" 5. Salir")

        print()
        choice = input("Ingresa tu opción: ")
        print()

        if choice == "1":
            title = input("Ingresa el título: ")
            result = search_by_title(anime_library, title)
            print(result)
        elif choice == "2":
            title = input("Ingresa parte del título: ")
            result = search_by_titles(anime_library, title)
            print(result)
        elif choice == "3":
            type_str = input(
                "Ingresa el tipo (TV, MOVIE, SPECIAL, ONA, OVA, UNKNOWN): "
            )
            type_search = get_type(type_str)
            season_str = input(
                "Ingresa la temporada (SPRING, SUMMER, FALL, WINTER, UNDEFINED): "
            )
            season_search = get_season(season_str)
            year_str = input("Ingresa el año: ")
            year_search = get_year(year_str)
            status_str = input(
                "Ingresa el estado (FINISHED, ONGOING, UPCOMING, UNKNOWN): "
            )
            status_search = get_status(status_str)
            tags_str = input("Ingresa las etiquetas separadas por comas: ")
            tags_search = get_tags(tags_str)
            limit = int(input("Ingresa el número máximo de resultados: "))

            result = search_by_criteria(
                anime_library,
                type_search,
                year_search,
                season_search,
                status_search,
                tags_search,
                limit,
            )
            print(result)
        elif choice == "4":
            result = get_random_anime(anime_loader)
            print(result)
        elif choice == "5":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
