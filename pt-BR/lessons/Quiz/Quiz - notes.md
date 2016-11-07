---
title: Quiz — Notas para o líder do clube
language: pt-BR
embeds: "*.png"
...

#Introdução:
Este projeto ensina crianças como usar seleção (`if`, `else` e `elif`) em seus programas, to alter program flow in response to data. This is achieved through writing and testing a simple quiz program, which includes written text and multiple choice responses.

#Recursos
Para este projeto, Python precisa ser instalado. É recomendada a versão 3.2 do Python.

As crianças podem usar o material que acompanha esse projeto. Arquivos inclusos na pasta 'Project Resources' (pasta abaixo do link 'Download Project Materials'):

+ Quiz.py

Certifique-se que cada criança tenha acesso à escrita e à leitura das próprias cópias desses recursos.

#Objetivos de Aprendizado
+ Seleção, usando:
	+ `if`;
	+ `else`;
	+ `elif`.
+ Teste de programas e resolução de problemas.

#Desafio
+ Questão de tempo- usando `if` e `else` para dar feedback da resposta;
+ Arrumando seu quiz - uso do método `.lower()` para reduzir erros no feeback da resposta;
+ Quiz de múltipla escolha - usando `elif` para adicionar questões de múltipla escolha no quiz;
+ Mantendo a pontuação - adição de uma variável `score` para medir progresso;
+ Como eu fui? - continuar a utilizar `if` e `else` para fornecer uma mensagem final no quiz, baseado na pontuação.

#Perguntas frequentes
+ Como o que o usuário digitou é guardado como texto, qualquer questão com respostas em numeral devem ser representadas como texto. Por exemplo:

```python
if resposta == "4":
	...
```

e *não*:

```python
if resposta == 4:
	...
```

Como alternativa, é possível transformar a resposta do usuário em número, e então comparar os dois números:

```python
resposta = int(resposta)
if resposta == 4:
	...
```

+ Cada declaração `if`/`else`/`elif` deve terminar com dois pontos.

+ O corpo de cada declaração `if`/`else`/`elif` deve ser uniformemente recuada. É recomendado que a tecla Tab seja usada para isso, pois ela faz que erros de recuo sejam facilmente detectados. Por exemplo, o seguinte programa não irá rodar:

```python
if resposta == "variavel":
   print("Muito bem!")
  print("---------")
    print(" :) ")
 )
```

+ As crianças devem lembrar da diferença entre `=` (usado para atribuição de variável) e `==` (usada para checar igualdade).