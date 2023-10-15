somme = 1000.0 
taux = 0.02 
Epargne = [0.0] * 21

for i in range(21):
    Epargne[i] = somme
    somme *= (1 + taux)

for i in range(21):
    print(f"Anniversaire de Mohamed {i} an : {Epargne[i]} Dhs")
