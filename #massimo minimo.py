#massimo minimo.py
n1=float(input("Inserisci un numero: "))
n2=float(input("Inserisci un secondo numero: "))
n3=float(input("Inserisci un terzo numero: "))
massimo=n1
if (massimo>n2) and (massimo>n3):
    print("Il massimo numero è", massimo)
if (massimo<n2) and (massimo>n3):
    print("Il massimo numero è", n2)
if (massimo>n2) and (massimo<n3):
    print("Il massimo numero è", n3) 