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
print("Resources gathered, converting to json...")

f = open('../IdeaProjects/PrivateResources/cards.json', 'w', encoding="utf-8")
f.write('{')
f.write('"cards": [')
i = False
for c in cards:
    if (i):
        f.write('},')
    f.write('{')
    string = ""
    
    if (c.id is not None):
        f.write('"id":"' + c.id.replace('"', '') + '"')
    
    if (c.name is not None):
        f.write(',"name":"' + c.name.replace('"', '') + '"')
    
    if (c.national_pokedex_number is not None):
        f.write(',"national_pokedex_number":' + str(c.national_pokedex_number))
    
    if (c.image_url is not None):
        f.write(',"image_url":"' + c.image_url.replace('"', '') + '"')
    
    if (c.image_url_hi_res is not None):
        f.write(',"image_url_hi_res":"' + c.image_url_hi_res.replace('"', '') + '"')
    
    if (c.subtype is None):
        f.write(',"subtype":"' + c.subtype.replace('"', '') + '"')
    
    if (c.supertype is not None):
        f.write(',"supertype":"' + c.supertype.replace('"', '') + '"')

    if (c.ability is not None):
        f.write(',"ability":{' + '"name":"' + c.ability['name'].replace('"', '') + '","text":"' + c.ability['text'].replace('"', '') + '","type":"' + c.ability['type'].replace('"', '') + '"}')

    if (c.ancient_trait is not None):
        f.write(',"ancient_trait":{' + '"name":"' + c.ancient_trait['name'].replace('"', '') + '","text":"' + c.ancient_trait['text'].replace('"', '') + '"}')
    
    if (c.hp is not None):
        f.write(',"hp":"' + c.hp.replace('"', '') + '"')
    
    if (c.number is not None):
        f.write(',"number":"' + c.number.replace('"', '') + '"')
    
    if (c.artist is not None):
        f.write(',"artist":"' + c.artist.replace("\n", "").replace('"', '') + '"')
    
    if (c.rarity is not None):
        f.write(',"rarity":"' + c.rarity.replace('"', '') + '"')
    
    if (c.series is not None):
        f.write(',"series":"' + c.series.replace('"', '') + '"')
    
    if (c.set is not None):
        f.write(',"set":"' + c.set.replace('"', '') + '"')
    
    if (c.set_code is not None):
        f.write(',"set_code":"' + c.set_code.replace('"', '') + '"')
    
    if (c.retreat_cost is not None):
        string = ""
        i = False
        for cost in c.retreat_cost:
            if (i):
                string = string + ','
            string = string + '"' + cost.replace('"', '') + '"'
            i = True
        f.write(',"retreat_cost":[' + string + ']')
    
    if (c.text is not None):
        string = ""
        i = False
        for t in c.text:
            if (i):
                string = string + ','
            string = string + '"' +  t.replace('"', '') + '"'
            i = True
        f.write(',"text":[' + string + ']')
    
    if (c.types is not None):
        string = ""
        i = False
        for t in c.types:
            if (i):
                string = string + ','
            string = string + '"' + t.replace('"', '') + '"'
            i = True
        f.write(',"types":[' + string + ']')

    if (c.attacks is not None):
        string = ""
        i = False
        for a in c.attacks:
            if (i):
                string = string + ','
            lis = []
            co = ""
            s = ""
            j = False
            if 'cost' in a:
                for cost in a['cost']:
                    if (j):
                        co = co + ","
                    co = co + '"' + cost.replace('"', '') + '"'
                    j = True
                lis.append('"cost":[' + co + ']')
                
            if 'name' in a:
                lis.append('"name":"' + a['name'].replace('"', '') + '"')
                 
            if 'text' in a:
                lis.append('"text":"' + a['text'].replace('"', '') + '"')
                
            if 'damage' in a:
                lis.append('"damage":"' + str(a['damage']).replace('"', '') + '"')

            j = False
            for l in lis:
                if (j):
                    s = s + ','
                s = s + l
                j = True
            string = string + '{' + s + '}'
            i = True
        f.write(',"attacks":[' + string + ']')

    if (c.weaknesses is not None):
        string = ""
        s = ""
        i = False
        for w in c.weaknesses:
            if (i):
                string = string + ','
            s = '"type":"' + w['type'].replace('"', '') + '","value":"' + w['value'].replace('"', '') + '"'
            string = string + '{' + s + '}'
            i = True
        f.write(',"weaknesses":[' + string + ']')

    if (c.resistances is not None):
        string = ""
        s = ""
        i = False
        for r in c.resistances:
            if (i):
                string = string + ','
            s = '"type":"' + w['type'].replace('"', '') + '","value":"' + w['value'].replace('"', '') + '"'
            string = string + '{' + s + '}'
            i = True
        f.write(',"resistances":[' + string + ']')
    
    i = True
f.write('}]}')
f.close()

f = open('../IdeaProjects/PrivateResources/sets.json', 'w')
f.write('{')
f.write('"sets":[')
i = False
for s in sets:
    if (i):
        f.write(',')
    f.write('{')
    f.write('"code":"' + s.code + '",')
    f.write('"name":"' + s.name + '",')
    f.write('"series":"' + s.series + '",')
    f.write('"total_cards":' + str(s.total_cards) + ',')
    f.write('"standard_legal":' + str(s.standard_legal).lower() + ',')
    f.write('"expanded_legal":' + str(s.expanded_legal).lower() + ',')
    f.write('"release_date":"' + s.release_date + '"}')
    i = True
f.write(']}')
f.close()
