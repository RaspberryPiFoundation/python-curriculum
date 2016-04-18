import io
import json
import urllib.request
from urllib.request import urlopen
from PIL import Image, ImageTk

#função para pegar os dados para o pokemon
def pegueDadosPokemon(num):
    dados = urllib.request.urlopen("http://pokeapi.co/api/v1/pokemon/"+str(num)).readall()
    pokemonDict = json.loads(dados.decode("UTF-8"))
    return pokemonDict

#function to get the image for a pokemon
def getPokemonImage(num):
    dados = urllib.request.urlopen("http://pokeapi.co/api/v1/sprite/"+str(num)).readall()
    spriteDict = json.loads(dados.decode("UTF-8"))
    imgURL = "http://pokeapi.co" + spriteDict["image"]
    image_bytes = urlopen(imgURL).read()
    dados_stream = io.BytesIO(image_bytes)
    pil_image = Image.open(dados_stream)
    tk_image = ImageTk.PhotoImage(pil_image)
    return tk_image
