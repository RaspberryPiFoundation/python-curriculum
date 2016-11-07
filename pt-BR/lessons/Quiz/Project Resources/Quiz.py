print("No Python, como se chama uma 'caixa' usada para armazenar dados?")
respostas = input()

if resposta == "variavel":
	print(" :) ")
else:
	print(" :( ")

print("Obrigado por jogar!")


print('''
Q1 - No Python, como se chama uma 'caixa' usada para armazenar dados?
a - texto
b - variavel
c - uma caixa de sapatos
''')
resposta = input().lower()

if resposta == "a":
	print(" Não - texto é um tipo de dado :( ")
elif resposta == "b":
	print(" Correto!! :) ")
elif resposta == "c":
	print(" Não seja bobinho! :( ")
else:
	print(" Você não escolheu a, b ou c :( ")
