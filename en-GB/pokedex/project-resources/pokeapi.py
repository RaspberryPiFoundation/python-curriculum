import io
import json
import urllib.request
from urllib.request import urlopen
#remove the line below if you haven't installed the PIL image library
from PIL import Image, ImageTk

#function to get the data for a pokemon
def getPokemonData(num):
    url = "http://pokeapi.co/api/v1/pokemon/"+str(num)
    request = urllib.request.Request(url)
    request.add_header('User-Agent', "something")
    data = urllib.request.urlopen(request).read()
    pokemonDict = json.loads(data.decode("UTF-8"))
    return pokemonDict

#function to get the image for a pokemon
#remove this function if you haven't installed the PIL image library
def getPokemonImage(num):
    pokemonDict = getPokemonData(num)
    imgURL = "http://pokeapi.co" + pokemonDict["image"]
    image_bytes = urlopen(imgURL).read()
    data_stream = io.BytesIO(image_bytes)
    pil_image = Image.open(data_stream)
    tk_image = ImageTk.PhotoImage(pil_image)
    return tk_image
