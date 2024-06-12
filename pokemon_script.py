from bs4 import BeautifulSoup
import requests

def type_extract(type):
    types = type.split(" · ")
    return(types)


website = requests.get("https://pokemondb.net/pokedex/game/diamond-pearl").text

#print(website)
soup = BeautifulSoup(website , 'lxml')
pokemons = soup.find_all('div', class_="infocard")
c = 0
list_type = []
temp = []
type_dict = {}
for pokemon in pokemons:
    info_text = pokemon.find('a', class_='ent-name').text
    small = pokemon.find_all('small')
    poke_type = small[1].text
    temp = type_extract(str(poke_type))
    list_type = list_type + temp
    #print(info_text)
    #print(poke_type)
    c+=1

print(f"Total pokemon {c}")
#print(list_type)  

for each_type in list_type:

    if each_type in type_dict:
        type_dict[each_type] += 1
    else:
        type_dict.update({each_type : 1})

print(type_dict)
