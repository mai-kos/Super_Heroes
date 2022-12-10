from pprint import pprint
import requests

class Hero:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_stats(self):
        url = f'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api//powerstats/{self.id}.json'
        response = requests.get(url)
        return response.json()

    def get_intelligence(self):
        intelligence = self.get_stats().get('intelligence')
        return intelligence
    

def get_max_intelligence(*heroes):
    intelligence = {}
    for hero in heroes:
        intelligence.setdefault(hero.get_intelligence(), hero.name)
    max_intelligence = max(intelligence.keys())
    max_int_hero = intelligence.get(max_intelligence)
    print(f'{max_int_hero} has the biggest intelligence stat - {max_intelligence}')



if __name__ == '__main__':
    hulk = Hero('Hulk', '332')
    captain_america = Hero('Captain America', '149')
    thanos = Hero('Thanos', '655')
    get_max_intelligence(hulk, captain_america, thanos)