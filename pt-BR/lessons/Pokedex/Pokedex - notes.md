---
title: Pokedex — Notas para líderes de clube
language: pt-BR
embeds: "*.png"
...

#Introdução:
Este projeto ensina as crianças a fazerem uma interface gráfica de usuário(GUI), através da criação de um Pokedex para mostrar informações em um Pokemon. Este projeto acessa a <a href="http://pokeapi.co/">pokeAPI</a>, desenvolvida por <a href="http://phalt.co/?ref=pokeapi">Paul Hallett</a>.

#Recursos
Para este projeto, é necessário ter Python instalado. É recomendado que a versão 3.2 do Python seja utilizada. 

As crianças precisarão usar os materiais que acompanham este projeto: Os arquivos incluídos na pasta 'Recurso de Projetos' (encontrados no link '/baixe Materiais de Projeto'):

+ GUI.py (pequeno programa de exemplo)
+ pokeapi.py (módulo utilizado para recuperar dados)

Certifique-se que cada criança tenha acesso de leitura e escrita à sua própria cópia destes recursos.

você pode encontrar uma versão completa dos desafios deste projeto clicando no link 'Baixe Materiais de Projeto' referente a este projeto, lá você encontrará:

+ pokedex-finished.py
+ pokedex-finished-with-images.py
+ pokeapi.py (módulo utilizado para recuperar dados)

#Objetivos de Aprendizado
+ Elementos de uma Interface Gráfica de Usuário (widgets):
	+ Caixa de Texto;
	+ Etiquetas;
	+ Botões.
+ Customizando widgets com o método `.config()`;
+ Usando botões para executar funções e atualizar os widgets.

#Desafios
+ Mais widgets - acrescentando widgets a uma janela GUI;
+ Tornando os widgets mais bonitos - modificando a aparência e a percepção do widget, utilizando o método `.config()`;
+ Finalizando seu Pokedex - modificando os valores de etiqueta dentro do programa dinamicamente.

#Perguntas Frequentes
+ Certifique-se que cada criança tenha uma cópia do arquivo `pokeapi.py`, e que esteja salvo no mesmo local que o programa que eles estão escrevendo!
+ Quando o programa GUI estiver rodando, a janela GUI pode estrar escondida atrás da janela shell do Python. Ao minimizar o shell a janela deve aparecer!
+ Apenas imagens .gif podem ser mostradas em uma janela GUI. Para a sessão opcional do Pokedex 'Acrescentando uma imagem', o <a href="https://pypi.python.org/pypi/Pillow/2.2.1#downloads">módulo 'pillow' </a> precisará ser instalado. Você pode testar se você tem o pillow instalado, simplesmente executando `from PIL import Image`. Se não retornar nenhum erro, está funcionando!