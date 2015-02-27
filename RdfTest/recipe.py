__author__ = 'marc'

# -*- coding: utf-8 -*-

import sys
import requests
import json
import BeautifulSoup

# Pass in a URL containing hRecipe, such as
# http://wholewheatsweets.com/recipe/cookies/whole_wheat_chocolate_hazelnut_biscotti

# URL = sys.argv[1]
URL = "http://wholewheatsweets.com/recipe/cookies/whole_wheat_chocolate_hazelnut_biscotti"

# Parse out some of the pertinent information for a recipe.
# See http://microformats.org/wiki/hrecipe.


def parse_hrecipe(url):
    req = requests.get(URL)

    soup = BeautifulSoup.BeautifulSoup(req.text)

    hrecipe = soup.find(True, 'hrecipe')

    if hrecipe and len(hrecipe) > 1:
        fn = hrecipe.find(True, 'fn').string
        yield_ = hrecipe.find(True, 'yield').find(text=True)
        ingredients = [i.string
                       for i in hrecipe.findAll(True, 'ingredient')
                       if i.string is not None]

        instructions = []
        for i in hrecipe.find(True, 'instructions').findAll(True, 'instruction'):
            if type(i) == BeautifulSoup.Tag:
                s = ''.join(i.findAll(text=True)).strip()
            elif type(i) == BeautifulSoup.NavigableString:
                s = i.string.strip()
            else:
                continue

            if s != '':
                instructions += [s]

        return {
            'name': fn,
            'yield:': yield_,
            'ingredients': ingredients,
            'instructions': instructions,
        }
    else:
        return {'error': 'No recipe has been found.'}


recipe = parse_hrecipe(URL)
print json.dumps(recipe, indent=4)
