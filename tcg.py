#! /usr/bin/env python

from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
import json

#Gets all info needed
cards = Card.all()
sets = Set.all()
types = Type.all()
subtypes = Subtype.all()
supertypes = Supertype.all()

print('Resources gathered, converting to json...')

#Loops through all cards an eliminates all NoneTypes to eliminate excess null values in json
cards_list = []
for c in cards:
    card_dict = {}
    
    if c.id is not None:
        card_dict["id"] = c.id
    
    if c.name is not None:
        card_dict["name"] = c.name
    
    if c.national_pokedex_number is not None:
        card_dict["national_pokedex_number"] = c.national_pokedex_number

    if c.image_url is not None:
        card_dict['image_url'] = c.image_url

    if c.image_url_hi_res is not None:
        card_dict['image_url_hi_res'] = c.image_url_hi_res

    if c.subtype is not None:
        card_dict['subtype'] = c.subtype

    if c.supertype is not None:
        card_dict['supertype'] = c.supertype

    if c.ability is not None:
        card_dict['ability'] = c.ability
    
    if c.ancient_trait is not None:
        card_dict['ancient_trait'] = c.ancient_trait

    if c.hp is not None:
        card_dict['hp'] = c.hp

    if c.number is not None:
        card_dict['number'] = c.number

    if c.artist is not None:
        card_dict['artist'] = c.artist

    if c.rarity is not None:
        card_dict['rarity'] = c.rarity

    if c.series is not None:
        card_dict['series'] = c.series

    if c.set is not None:
        card_dict['set'] = c.set

    if c.set_code is not None:
        card_dict['set_code'] = c.set_code

    if c.retreat_cost is not None:
        card_dict['retreat_cost'] = c.retreat_cost

    if c.text is not None:
        card_dict['text'] = c.text
    
    if c.types is not None:
        card_dict['types'] = c.types
    
    if c.attacks is not None:
        card_dict['attacks'] = [{
            'cost': a.get('cost'),
            'name': a.get('name'),
            'text': a.get('text'),
            'damage': a.get('damage')
        } for a in c.attacks]

    if c.weaknesses is not None:
        card_dict['weaknesses'] = [{
            'type': w.get('type'),
            'value': w.get('value')
        } for w in c.weaknesses]

    if c.resistances is not None:
        card_dict['resistances'] = [{
            'type': r.get('type'),
            'value': r.get('value')
        } for r in c.resistances]

    cards_list.append(card_dict)

with open('../IdeaProjects/PrivateResources/tcg/cards.json', 'w') as f:
    json.dump({'cards': cards_list}, f)

#Stores all the sets into a list
sets_list = [{
        'code': s.code,
        'name': s.name,
        'series': s.series,
        'total_cards': s.total_cards,
        'standard_legal': s.standard_legal,
        'expanded_legal': s.expanded_legal,
        'release_date': s.release_date
    } for s in sets]

with open('../IdeaProjects/PrivateResources/tcg/sets.json', 'w') as f:
    json.dump({'sets': sets_list}, f)

#Adds the additional types, supertypes, and subtypes to a file for easy referencing/searching
with open('../IdeaProjects/PrivateResources/tcg/types.json', 'w') as f:
    json.dump({'types': types}, f)
    
with open('../IdeaProjects/PrivateResources/tcg/supertypes.json', 'w') as f:
    json.dump({'supertypes': supertypes}, f)
    
with open('../IdeaProjects/PrivateResources/tcg/subtypes.json', 'w') as f:
    json.dump({'subtypes': subtypes}, f)
