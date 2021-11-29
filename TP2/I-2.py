#!/usr/bin/env python3

if __name__ == "__main__":
    
    sum = 0
    i = 0
    print("Entrez 10 entiers, un par un :")
    while (i != 10):
        while True:
            try:
                sum+=int(input())
                break
            except:
                print("Ce n'est pas un entier !")
        i+=1
    print("La moyenne de ces entiers est", sum/10)
   
   #la boucle for est plus adaptée car on connaît le nombre d'itérations
