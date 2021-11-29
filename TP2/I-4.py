#!/usr/bin/env python3

if __name__ == "__main__":
    
    sum = 0
    i = 0
    inp = int(input("Entrez des entiers un par un, en terminant par -1 : "))
    max_nb = inp
    min_nb = inp
    while (inp != -1):
        sum+=inp
        i+=1
        if max_nb < inp:
            max_nb = inp
        if min_nb > inp:
            min_nb = inp 
        while True:
            try:
                inp=int(input())
                break
            except:
                print("Ce n'est pas un entier !")
    if i>=1:    
        print("La moyenne de ces entiers est", sum/i)
        print("Le minimum est", min_nb ,"et le maximum est", max_nb)
   
