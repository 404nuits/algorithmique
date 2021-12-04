#!/usr/bin/env python3

if __name__ == "__main__":
    
    sum = 0
    i = 0
    inp = int(input("Entrez des entiers un par un, en terminant par -1 : "))
    max_nb = inp
    min_nb = inp
    nb_occ = inp
    occ = 1
    suite = list()
    ssuite = list()
    ssuite.append(inp)
    while (inp != -1):
        if inp < ssuite[-1]:
            suite.append(list(ssuite))
            ssuite = list()
        ssuite.append(inp)
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
        if inp == nb_occ : occ+=1
    if i>=1:
        suite.append(list(ssuite))
        suite[0].pop(0) 
        rep = ' '
        while rep != 'q':
            print("a. afficher la moyenne \nb. afficher le minimum \nc. afficher le maximum \nd. afficher le nombre d'occurences du 1er entier \ne. afficher le nombre de monotonies \nq. quitter")
            rep = input()
            if rep == 'a':
                print("La moyenne de ces entiers est", sum/i)
            elif rep == 'b':
                print("Le minimum est", min_nb)
            elif rep == 'c':
                print("Le maximum est", max_nb)
            elif rep == 'd':
                print("Le nombre", nb_occ, "apparaît", occ, "fois") 
            elif rep == 'e':
                print("Il y a",len(suite) ,"listes (dé)croissante(s)")
    else:
        print("Vous n'avez saisi aucune valeur")
