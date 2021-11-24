#!/usr/bin/env python3

if __name__ == "__main__":
    
    n = input("Quelle est la longueur du côté ?")
    n = int(n)
    m = 1
    for i in range(0,n):
        for j in range(0,n-i-1):
            print("  ", end=" ")
        for k in range(0,m):
            print("* ", end=" ")
        m+=2
        print("")
    
