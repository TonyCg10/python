@echo off
set PYTHONPATH=./src
pyinstaller --onefile --windowed --add-data "assets/anime-offline-database-minified.json;assets" --distpath "./Anime Searcher" --specpath "./Anime Searcher" --workpath "./Anime Searcher/build" src/main.py
