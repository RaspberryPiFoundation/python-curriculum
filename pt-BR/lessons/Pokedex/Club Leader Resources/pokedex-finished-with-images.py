from random import *
import tkinter
from pokeapi import *

fontePequena = ["Ariel" , 10]
fonteMedia = ["Ariel" , 14]
fonteGrande = ["Ariel" , 24]

#função para mostrar dados para um número de pokemon 
def mostreDadosDoPokemon():
    #obtenha um número aleatório de pokemon 
    numeroDoPokemon = randint(1,178)

    #use a função encontrada em 'pokeapi.py' para obter os dados do pokemon
    dicionarioDoPokemon = getPokemonData(numeroDoPokemon)
    ImagemDoPokemon = getPokemonImage(numeroDoPokemon)

    #pegue os dados do dicionário e os utilize nas etiquetas
    etiquetaValorNome.configure(text = dicionarioDoPokemon["name"])
    etiquetaValorAtingidos.configure(text = dicionarioDoPokemon["hp"])
    etiquetaValorAtaque.configure(text = dicionarioDoPokemon["attack"])
    etiquetaValorDefesa.configure(text = dicionarioDoPokemon["defense"])
    etiquetaValorVelocidade.configure(text = dicionarioDoPokemon["speed"])
    
    #obtenha a image e coloque-a na etiqueta
    etiquetaImagem.configure(image=ImagemDoPokemon)
    etiquetaImagem.image = ImagemDoPokemon

#crie uma nova janela GUI 
janela = tkinter.Tk()
janela.config(bg="#e0e0ff")
janela.title("Pokedex")

#um botão que vai obter as informações para o pokemon
btnObterInfo = tkinter.Button(janela,text="Obtenha um Pokemon!", command=mostreDadosDoPokemon, font=fontePequena)
btnObterInfo.pack()

#Nome do Pokemon 
etiquetaTextoNome = tkinter.Label(janela,text="Nome:", font=fonteMedia)
etiquetaTextoNome.config(bg="#e0e0ff", fg="#111111")
etiquetaTextoNome.pack()
etiquetaValorNome = tkinter.Label(janela,text="?", font=fonteGrande)
etiquetaValorNome.config(bg="#e0e0ff", fg="#111111")
etiquetaValorNome.pack()

#Pontos Atingidos pelo Pokemon
etiquetaPontosAtingidos = tkinter.Label(janela,text="Pontos Atingidos:", font=fonteMedia)
etiquetaPontosAtingidos.config(bg="#e0e0ff", fg="#111111")
etiquetaPontosAtingidos.pack()
etiquetaValorAtingidos = tkinter.Label(janela,text="?", font=fonteGrande)
etiquetaValorAtingidos.config(bg="#e0e0ff", fg="#111111")
etiquetaValorAtingidos.pack()

#Ataques do Pokemon 
etiquetaAtaque = tkinter.Label(janela,text="Ataque:", font=fonteMedia)
etiquetaAtaque.config(bg="#e0e0ff", fg="#111111")
etiquetaAtaque.pack()
etiquetaValorAtaque = tkinter.Label(janela,text="?", font=fonteGrande)
etiquetaValorAtaque.config(bg="#e0e0ff", fg="#111111")
etiquetaValorAtaque.pack()

#pokemon defence
etiquetaDefesa = tkinter.Label(janela,text="Defesa:", font=fonteMedia)
etiquetaDefesa.config(bg="#e0e0ff", fg="#111111")
etiquetaDefesa.pack()
etiquetaValorDefesa = tkinter.Label(janela,text="?", font=fonteGrande)
etiquetaValorDefesa.config(bg="#e0e0ff", fg="#111111")
etiquetaValorDefesa.pack()

#pokemon speed
etiquetaVelocidade = tkinter.Label(janela,text="Velocidade:", font=fonteMedia)
etiquetaVelocidade.config(bg="#e0e0ff", fg="#111111")
etiquetaVelocidade.pack()
etiquetaValorVelocidade = tkinter.Label(janela,text="?", font=fonteGrande)
etiquetaValorVelocidade.config(bg="#e0e0ff", fg="#111111")
etiquetaValorVelocidade.pack()

#etiqueta para a imagem do Pokemon
etiquetaImagem = tkinter.Label(janela)
etiquetaImagem.config(bg="#e0e0ff", fg="#111111")
etiquetaImagem.pack()

janela.mainloop()

    
