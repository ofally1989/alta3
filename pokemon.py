#!/usr/bin/python3
import requests

### CHALLENGE 1: CHANGE THIS SCRIPT SO THAT A USER MAY INPUT WHAT POKEMON THEY WANT TO VIEW.
### CHALLENGE 2: USING A WHILE LOOP AND TRY/EXCEPT, FORCE THE USER TO RE-ENTER THE POKEMON'S NAME IF THEY CREATE A BOGUS URL.
def url():
    # Using the requests library, pull a Pokemon from the PokeAPI
    try:
        poke1 = input("What Pokemon do you want? ").lower()
        poke_api = requests.get(f'https://pokeapi.co/api/v2/pokemon/{poke1}/')
        poke_api = poke_api.json() # poke_api is the translated API
        return poke_api
    except:
      print("Invalid selection!")
      url()

def main():
    poke_api= url()
    print(str(poke_api["forms"][0]["name"]).capitalize(), ", I CHOOSE YOU!\n")

    games= []

### CHALLENGE 3: ADD A WHILE LOOP THAT FORCES THE USER TO KEEP GUESSING UNTIL THEY GET THE ANSWER CORRECT!
    for x in poke_api["game_indices"]:
        version= x["version"]["name"]
        games.append(version)

    guess= input("Guess one Pokemon game version this Pokemon was in! ")
    if guess in games:
        print("Correct!")
    else:
        print("Wrong!")

main()
