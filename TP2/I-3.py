#!/usr/bin/env python3

if __name__ == "__main__":
    
    sum = 0
    i = 0
    inp = int(input("Entrez des entiers un par un, en terminant par -1 : "))
    while (inp != -1):
        sum+=inp
        i+=1
        while True:
            try:
                inp=int(input())
                break
            except:
                print("Ce n'est pas un entier !")
    if i>=1:    
        print("La moyenne de ces entiers est", sum/i)
   
