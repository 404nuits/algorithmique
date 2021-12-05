#!/usr/bin/env python3

if __name__ == "__main__":
    
    nb = int(input("Entrez un entier : "))  
    save_nb = nb
    nb2 = int(input("Entrez un deuxième entier : "))
    save_nb2 = nb2
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
    
    #calcul du PGCD et des coefficients de Bézout
    nb = save_nb

    u,b = 1,1
    v,a = 0,0
    while nb2 != 0 :
        c = nb // nb2
        nb, u, v, nb2, a, b = nb2, a, b, nb - c * nb2, u - c * a, v - c * b
    if nb > 0:
        nb2 = nb
    else:
        nb2 = -nb
        u = -u
        v = -v

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

    print("Le PGCD de",nb,"et",save_nb2,"est",nb2)
    print("Avec u =",u,"et v =",v)
