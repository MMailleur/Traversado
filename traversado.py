from hashlib import new
from os import remove
import random


n=-1
reponse = ""
x=0
q=1

couleur = ["Coeur","carreaux","pique","trefle"]
valeur = ["2","3","4","5","6","7","8","9","10","Valet","Dame","Roi","AS"]
carte = [(val + " de " + coul ) for val in valeur for coul in couleur ]
print("---------------------------------------------")
print("---------------------------------------------")

print(" Le but est de deviner si la prochaine carte ")
print(" est plus grande, plus petite ou egale ")
def verifCarte() :
    global x
    
    carteActuelle=carteSortie[x]
    poidsCarteActuelle=carteActuelle[1]
    if newCard[1] > poidsCarteActuelle:
        reponseVoulue = "plus" 
    if newCard[1] < poidsCarteActuelle:
        reponseVoulue = "moins"
    if newCard[1] == poidsCarteActuelle:
        reponseVoulue = "egale"
    if reponse == reponseVoulue :
        carteSortie[x]=newCard
        x+=1
        print("---------------------------------------------")
        print("---------------------------------------------")
        print("Ta carte etait :",carteActuelle[0])
        print("La nouvelle carte etait :",newCard[0])
        print("ta réponse est :", reponse)
        print("Bravo c'est juste ! ")
    else :
        print("---------------------------------------------")
        print("---------------------------------------------")
        print("Ta carte etait :",carteActuelle[0])
        print("La nouvelle carte etait :",newCard[0])
        print("ta réponse est :", reponse)
        print("Aie c'est faux recommence ! ")
        
        carteSortie[x]=newCard
        x=0
        


packet = [(carte[n],((n)//4)+1) for n in range(len(carte))]

def piocherCarte():
  
    choix =random.choice(packet)
    packet.remove(choix)
    piocheCarte = choix[0]
    packetCarte = choix[1]
   
    return piocheCarte,packetCarte
 
carteSortie = []
for i in range(5):
    carteSortie.append(piocherCarte())

def affichageConsole():
  q=1
  
  print("---------------------------------------------")
  print("---------------------------------------------")

  print("Jeux de carte :\n")
  for p in carteSortie:
    
    print("Carte",q,":")
    print(p[0], end = "\n")
    q+=1
    print()
    

while len(packet) > 0 :
    
    if x<5 :
        affichageConsole()
        carteActuelle=carteSortie[x]
        newCard = piocherCarte()
        print(" Carte actuelle",(x+1), ": " ,carteActuelle[0])
        reponse=input("Plus , moins ou egale ? ")
        
        verifCarte()
    
    if x == 5 :
        print("BRAVO c'est GAGNER !!")
        break
