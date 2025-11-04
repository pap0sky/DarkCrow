età= float(input("Inserisci la tua età: "))
nome= str(input("Inserisci il tuo nome: "))
if età%3==0 and età%2!=0:
    s=nome[0:2] + nome[-2:]
else:
    s= nome[2:-2]
print(s)
