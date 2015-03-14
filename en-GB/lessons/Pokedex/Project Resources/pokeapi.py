import io
import json
import urllib.request
from urllib.request import urlopen
from PIL import Image, ImageTk

#function to get the data for a pokemon
def getPokemonData(num):
    data = urllib.request.urlopen("http://pokeapi.co/api/v1/pokemon/"+str(num)).readall()
    pokemonDict = json.loads(data.decode("UTF-8"))
    return pokemonDict

#function to get the image for a pokemon
def getPokemonImage(num):
    data = urllib.request.urlopen("http://pokeapi.co/api/v1/sprite/"+str(num)).readall()
    spriteDict = json.loads(data.decode("UTF-8"))
    imgURL = "http://pokeapi.co" + spriteDict["image"]
    image_bytes = urlopen(imgURL).read()
    data_stream = io.BytesIO(image_bytes)
    pil_image = Image.open(data_stream)
    tk_image = ImageTk.PhotoImage(pil_image)
    return tk_image
