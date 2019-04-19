import json
from unicodedata import normalize
from collections import defaultdict


class CityParser:
    
    def __init__(self):
        with open('city.list.json', 'r', encoding = 'utf-8') as file:
            cities = json.loads(file.read())
            data = defaultdict(list)

        for c in cities:
            city_name = normalize('NFC', c['name'])
            data[city_name].append(c)
            
        self.data = data
    
    
    def findall(self, name):
        name = normalize('NFC', name)
        
        if name not in self.data.keys():
            return None
    
        cities = self.data[name]
        return cities
    
    
    def find(self, name, country=None):
        
        if country is not None:
            country = normalize('NFC', country)
            
        cities = self.findall(name)
        
        if len(cities) > 1:
            if country is None:
                raise Exception('ambiguous query result')
            else:
                cities = list(filter(lambda x : x['country'] == country, cities))
                if len(cities) > 1:
                    raise Exception(f'unable to resolve query: found {len(cities)} cities.')
        
        return cities[0]
    