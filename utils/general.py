from random import randint
import re


def generate_randomizer(Model):
    randomizer = randint(1, 100000000)
    if Model.objects.filter(randomizer=randomizer).exists():
        return generate_randomizer(Model)
    return randomizer


def generate_index(Model):
    index = randint(1, 10000)
    if Model.objects.filter(index=index).exists():
        return generate_index(Model)
    return index


def string_likeness(str1, str2):
    str1 = re.sub(r'\W+', ' ', str1).strip().lower().split(' ')
    str2 = re.sub(r'\W+', ' ', str2).strip().lower().split(' ')

    intersection = set(str1) & set(str2)
    combination = set(str2) | set(str1)

    return int((len(intersection) / len(combination)) * 100)