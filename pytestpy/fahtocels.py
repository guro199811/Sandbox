try:
    def fahr(cels):
        fahren = cels * 9 / 5 + 32
        return fahren
except: 
    print("The number you entered was not an numerical number")
cels = int(input("Celsius: "))
print(fahr(cels))
