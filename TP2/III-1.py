#!/usr/bin/env python3

if __name__ == "__main__":
    
    nb = int(input("Entrez un entier : "))  
    rev_nb = 0  
  
    while (nb > 0):    
        reste = nb % 10  
        rev_nb = (rev_nb * 10) + reste  
        nb = nb // 10 

    print("L'inverse de ce nombre est",rev_nb)
    
