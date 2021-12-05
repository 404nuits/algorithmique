#!/usr/bin/env python3

if __name__ == "__main__":
    
    nb = int(input("Entrez un entier : "))  
    save_nb = nb

    #calcul de l'inverse
    rev_nb = 0
    while (nb > 0):    
        reste = nb % 10  
        rev_nb = (rev_nb * 10) + reste  
        nb = nb // 10

    #nombre premier ou pas?
    nb = save_nb
    i = 2
    while i < nb and nb % i != 0:
        i = i + 1

    #décomposition en facteurs premiers
    i = 2
    fact_premiers = list()
    while nb > 1:
        while nb % i == 0:
            fact_premiers.append(i)
            nb = nb / i
        i+=1

    #affichage des résulats
    nb = save_nb
    if i == nb:
        print("Le nombre", nb, "est premier.")
    else:
        print(nb,"n'est pas un nombre premier.")

    print("L'inverse de ce nombre est",rev_nb)
    
    print("Décomposition en facteurs premiers :", nb,"= 1", end = ' ')
    for i in fact_premiers:
        print("x",i, end = ' ')
    print()
