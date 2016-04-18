---
title: Mensagens Secretas — Notas para os Líderes de Clube
language: pt-BR
embeds: "*.png"
...

#Introdução:
Este projeto ensina iteração sobre uma string de texto, e ela pode ser usada para criar uma cifra de César.

#Recursos
Para este projeto, será necessário ter Python instalado. É recomendável que a versão 3.2 esteja instalada.

As crianças podem também fazer uso dos materiais que acompanham estes desafios. Os arquivos estão incluídos na pasta 'Recursos de Projeto' (encontrada no link 'Baixe Material de Projeto'):

+ Encryption.py

Tenha certeza que cada criança tenha acesso de leitura e escrita à sua própria cópia destes recursos.

Voce pode encontrar uma versão dos desafios deste projeto clicando no link 'Baixe Material de Projeto' relativo a este projeto, lá você encontrará:

+ LoveCalculator.py

#Objetivos de Aprendizado
+ Iteração sobre uma variável do tipo string;
+ O método `find()` (que significa 'encontre');
+ O operador de módulo (`%`).

#Desafios
+ Variáveis chave - permitindo que o usuário entre a chave desejada;
+ Criptografando e descriptografando caracteres - criptografia e descriptografia de um único caracter;
+ Criptografando e descriptografando mensagens - criptografia e descriptografia de mensagens inteiras;
+ Melhorando sua cifra - modificação do programa para tornar a quebra da cifra mais difícil;
+ Calculadora do amor - aplicando iteração de texto para um novo problema.

#Perguntas Frequentes 
+ Durante buscas usando `find()` ou `if char in alphabet:` (se caracter estiver no alfabeto), note que o comando de busca diferencia maiúsculas e minúsculas. As crianças devem usar:

```python
mensagem = input("Por favor, entre uma mensagem para criptografar: ").lower()
```

asim a entrada é toda convertida em minúscula antes da busca.