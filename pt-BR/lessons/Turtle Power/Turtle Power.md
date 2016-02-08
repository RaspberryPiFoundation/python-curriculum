---
title: O poder da Tartaruga (Turtle)
level: Python 1
language: pt-BR
stylesheet: python
embeds: "*.png"
materials: ["Recursos do Projeto/*.*"]
...

#Introdução:  { .intro}
Neste projeto, você aprenderá a usar o 'turtle' para desenhar figuras e padrões fantásticos.

#Passo 1: Olá, turtle! { .activity}

Vamos nos divertir programando tartarugas (turtles). A tartaruga (turtle) é um pequeno robô que desenha na sua tela, e pode ser controlada usando comandos Python.

## Lista de atividades { .check}

+ Vamos fazer uma tartaruga se mover pela tela, executando este pequeno programa Python:

	```python
	from turtle import *
	shape("turtle")
	speed(5)

	forward(100)
	right(90)
	forward(100)

	done()
	```

	![screenshot](turtle.png)

+ A tartaruga tem uma caneta ligada a ela, e ela desenha uma linha à medida em que se move pela tela. Veja o que o programa faz:

	+ `from turtle import *` este comando diz ao Python que você quer usar a biblioteca turtle, que é uma coleção de código que você pode usar para desenhar na tela. O `*` significa 'importe tudo'.

	+ `shape("turtle")` - este comando faz com que o robô que desenha se pareça com uma tartaruga. Nós usamos "turtle" (tartaruga), mas você poderia também usar "arrow" (seta), "circle" (círculo), "square" (quadrado), "triangle" (triângulo) or "classic" (clássico).

	+ `speed(5)` - este comando diz à tartaruga quão rápido ela deve desenhar. Você pode usar um número entre 1 e 11. 11 é o mais rápido, 1 é o mais devagar.

	+ `forward(100)` and `backward(100)` . "forward" significa "para frente" e "backward" significa "para trás". Este comando pede à tartaruga que se mova 100 pixels para frente ou para trás.

	+ `left(45)` and `right(90)`. "left" significa "esquerda", e  "right" significa "direita". Este comando faz com que a tartaruga gire para a esquerda ou direita. Ela vai girar o número de graus que você indicar entre parênteses. Veja alguns exemplos:
	
		![screenshot](turtle_degrees.png)

	+ `done()` - "done" significa "pronto". Este comando diz ao Python que nós terminamos a programação da tartaruga.


+ Qual sua cor favorita? Para tornar os desenhos mais interessantes, você pode trocar a cor e o tamanho da caneta que vai desenhar a linha. Alguns exemplos para você experimentar:

	```python
	from turtle import *
	shape("turtle")
	speed(8)

	color("Purple")
	pensize(7)
	right(90)
	forward(100)
	left(90)
	forward(50)

	color("Orange")
	pensize(3)
	penup()
	forward(50)
	pendown()
	forward(50)

	done()
	```

	![screenshot](turtle_colour.png)

+ O código acima contém uma série de comandos:

	+ `color("Purple")` faz com que a tartaruga e a caneta fiquem roxas. Note que estamos usando a ortografia americana da palavra cor (color) e não a britânica (colour),  which doesn't have a 'u' in it. Você também pode especificar as cores em *hexadecimal*, como foi feito em CSS. Ao invés de usar `pencolor("Red")` você poderia usar `pencolor("#FF0000")`.

	+ `penup()` - "pen up" significa "levantar caneta". Este comando tira a caneta  da tela. E `pendown()`, que significa "baixar caneta" coloca a caneta novamente na tela. Isto significa que você pode mover a tartaruga sem que ela desenhe o caminho feito!

## Salve seu projeto {.save}

## Desenhe: Desenhando formatos { .challenge}
+ Voc~e consegue usar os comandos de tartaruga acima para desenhar:
	+ Um quadrado?
	+ Um triângulo?

+ Você consegue desenhar uma casa? O que mais você consegue desenhar?

## Salve Seu Projeto {.save}

# Step 2: Repetindo você mesmo { .activity }

Quando desenhamos um quadrado ou um triângulo, o programa repete a mesma sequência de comandos várias vezes seguida. Vamos fazer com que o Python os repita para nós!

## Lista de Atividades { .check}

+ Abra um novo arquivo, e execute o seguinte programa:

	```python
	from turtle import *

	speed(11)
	shape("turtle")

	for count in range(4):
		forward(100)
		right(90)

	done()
	```

	Este programa usa um laço (loop) `for`. Você pode usar um laço `for` em Python todas as vezes que você quiser que ele repita um código um certo número de vezes. 

	No programa acima, os comandos `forward(100)` e `right(90)` são repetidos 4 vezes para desenhar um quadrado. Virar 90 graus para cada ângulo significa que viramos 360 graus ao todo.

+ Assim como para um comando `if`, você deve usar a tecla Tab para identar o código que você quer repetir. Tente modificar o código de modo que a linha `forward(100)` esteja identada, mas a linha `right(50)` não esteja identada, desta maneira:

	```python
	from turtle import *

	speed(11)
	shape("turtle")

	for count in range(4):
		forward(100)
	right(90)

	done()
	```

	O que acontece quando você executa o programa? Você obteve uma linha reta? Neste programa, Python repetirá `forward(100)` 4 vezes, e _após isto_ executará o comando `right(90)`, girando à direita.

+ Agora que você sabe como repetir os comandos, você pode criar formatos mais complexos e outros padrões com mais facilidade. Execute este programa:

	```python
	from turtle import *

	speed(11)
	shape("turtle")

	for count in range(8):
		forward(100)
		right(45)

	done()
	```

	![screenshot](turtle_octagon.png)

	Este programa trabalha da mesma maneira que o programa que desenha qudrado, exceto que que repete 8 vezes, e apenas gira 45 graus para cada vértice. Isto significa que o código desenha uma figura de oito lados (um octógono), e veja que o total dos ângulos dos vértices totaliza 360 graus (360 dividido por 8 é 45).

+ Aqui temos outro exemplo do que podemos criar usando um laço `for`. O que este programa desenha?

	```python
	from turtle import *

	speed(11)
	shape("turtle")

	for count in range(30):
		forward(5)
		penup()
		forward(5)
		pendown()

	done()
	```

## Salve Seu Projeto {.save}

## Desafio: Formatos em loop { .challenge}
+ Você consegue usar um laço `for` para desenhar:
	+ Um pentâgono? (5 lados)
	+ Um hexágono? (6 lados)
Lembre que os ângulos de todos os vértices sempre totalizam 360 graus!

+ Você consegue desenhar um círculo? Você pode mover 1 pixel para frente e girar 1 grau a cada vez. Quantas vezes você precisa repetir estes comandos?

## Salve Seu Projeto {.save}

## Desafio: Desenhando padrões { .challenge}
Você consegue usar o que você aprendeu para desenhar padrões fantásticos? Aqui temos um exemplo:

```python
from turtle import *

speed(11)
shape("turtle")
pensize(6)
color("Red")

for count in range(36):
	forward(100)
	right(100)

done()
```

![screenshot](turtle_loopy.png)

## Salve Seu Projeto {.save}

## Desafio: Variáveis e loops { .challenge}
Quando desenhamos diferentes formatos, precisamos calcular nós mesmos quantos graus precisamos girar para cada vértice.

Podemos fazer o cálculo no programa, assim o computador faz esse serviço para a gente? Para descobrir o número de graus que a tartaruga deve girar, você pode dividir 360 pelo número de lados da sua figura:

```python
lados = 4
angulo = 360 / lados
```

`/` é o símbolo do Python para divisão. Veja que a resposta é armazenada em uma variável chamada `angulo`, que você usar para desenhar sua figura:

```python
left(angulo)
```

Você pode modificar o número armazenado na variável `lados` e testar se funciona para qualquer figura!

## Salve seu projeto {.save}
