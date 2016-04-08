# -*- coding: utf-8 -*-

import difflib
import json
import requests

from .cache import Cache


SIO_API_ENDPOINT = "http://api.desperate.solutions/dagens/"


class Cafeteria(object):
    __cafeterias = Cache(value=None, ttl=86400)

    def __init__(self, name, url):
        self.__dishes = Cache(value=None, ttl=900)
        self.__name = name
        self.__url = url

    def __str__(self):
        return self.__name

    def __repr__(self):
        return "{class_name}({name}, {url})".format(
            class_name=type(self).__name__,
            name=self.__name,
            url=self.__url)

    @property
    def dishes(self):
        """
        Return the dishes currently offered by the cafeteria.
        """
        # Update the cache if it is empty or expired.
        if self.__dishes.expired:
            response = requests.get(self.__url)
            response.raise_for_status()
            response = json.loads(response.text)

            dishes = []
            for category in response["cafeteria"]:
                if category["category"] == "pris":
                    # We already know it's expensive.
                    continue
                for dish in category["dishes"]:
                    # Just keep the part describing the actual dish.
                    dish = strip_sio(dish)
                    dishes.append(Dish(category["category"], dish))

            self.__dishes.value = dishes

        return self.__dishes.value

    @property
    def name(self):
        """
        Return the name of the cafeteria.
        """
        return self.__name

    @classmethod
    def from_name(cls, name):
        """
        Return the closest matching cafeteria.
        """
        name = "informatikk" if name == "ifi" else name
        cafeterias = cls.all()
        match = difflib.get_close_matches(
            word=name.lower(),
            possibilities=cafeterias.keys(), # All in lower case.
            n=1,
            cutoff=0.5)
        return cafeterias[match[0]] if match else None

    @classmethod
    def all(cls):
        """
        Return a dictionary of all cafeterias for which data is available.
        """
        # Update the cache if it is empty or expired.
        if cls.__cafeterias.expired:
            response = requests.get(SIO_API_ENDPOINT)
            response.raise_for_status()
            response = json.loads(response.text)

            cafeterias = {}
            for name, url in response.items():
                # All of the dictionary keys has to be in lower case because
                # get_close_matches() in from_name() is case sensitive.
                cafeterias[name.lower()] = Cafeteria(name, url)

            cls.__cafeterias.value = cafeterias

        return cls.__cafeterias.value

    @classmethod
    def search(cls, dish):
        """
        Return a list of the cafeterias that offer a matching dish.
        """
        cafeterias = []
        for name, cafeteria in cls.all().items():
            matches = cafeteria.has(dish)
            if matches:
                cafeterias.append(matches)
        return cafeterias

    def has(self, needle):
        """
        Return a tuple with the cafeteria and a list of the dishes it offers
        that matches the search needle. Otherwise return None.
        """
        matches = []
        for dish in self.dishes:
            if dish.has(needle):
                matches.append(dish)
        return (self, matches) if matches else None

class Dish(object):
    def __init__(self, category, description):
        self.__category = category
        self.__description = description

    def __str__(self):
        return self.__description

    def __repr__(self):
        return "{class_name}({category}, {description})".format(
            class_name=type(self).__name__,
            category=self.__category,
            description=self.__description)

    @property
    def category(self):
        """
        Return the category of the dish.
        """
        return self.__category

    @property
    def description(self):
        """
        Return the description of the dish.
        """
        return self.__description

    def has(self, needle):
        """
        Return a boolean value indicating whether the description of the dish
        mentions the needle or not.
        """
        return needle.upper() in self.__description.upper()


def strip_sio(dish):
    prefixes = [
        "Du finner også flere varme ingredienser på buffeten:",
        "Funky Junk Friday:",
        "På buffeten finner du også",
        "Working Class Hero Thursday:"
    ]

    # Strip away stupid prefixes.
    for prefix in prefixes:
        if dish.startswith(prefix):
            dish = dish[len(prefix):]
            break

    # TODO: Replace with: http://stackoverflow.com/a/30834199
    return dish.split("Allergener")[0:1][0].strip().capitalize()
