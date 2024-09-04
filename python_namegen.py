from re import A
import string
import random

abc = list(string.ascii_lowercase)
letras_aleatorias = random.sample(abc, random.randint(4, 8))


def gen(n):
    vocales = ["a", "e", "i", "o", "u"]
    consonantes = [letter for letter in abc if letter not in vocales]

    nombre = "".join([n[0].capitalize()] + n[1:])
    if n[0] not in consonantes or n[1] not in consonantes:
        return nombre


gen(letras_aleatorias)
