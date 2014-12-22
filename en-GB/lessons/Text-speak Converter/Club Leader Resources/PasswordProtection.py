passwordDictionary = {

        "sohail" : "letmein"
    
    }

print("Super-secret program")
print("====================")


name = input("Name : ").lower()
password = input("Password : ").lower()

if name in passwordDictionary and passwordDictionary[name] == password:

    print("\nWELCOME", name.upper())

else:
    
    print("Access denied")

