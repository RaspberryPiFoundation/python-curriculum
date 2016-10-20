passwordDictionary = {

        "sohail" : "letmein"
    
    }

print("Programa super secreto")
print("====================")


name = input("Nome : ").lower()
password = input("Senha : ").lower()

if name in passwordDictionary and passwordDictionary[name] == password:

    print("\nBEM-VINDO", name.upper())

else:
    
    print("Acesso negado")

