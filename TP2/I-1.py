#!/usr/bin/env python3

if __name__ == "__main__":
    
    sum = 0
    print("Entrez 10 entiers, un par un :")
    for i in range (0,10):
        while True:
            try:
                sum+=int(input())
                break
            except:
                print("Ce n'est pas un entier !")

    print("La moyenne de ces entiers est", sum/10)
    
