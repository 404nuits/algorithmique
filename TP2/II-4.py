#!/usr/bin/env python3

if __name__ == "__main__":
    
    n = input("Quelle est la hauteur du losange ?")
    n = int(int(n)/2)    
    m = 1
    for i in range(0,n):
        for j in range(0,n-i):
            print("  ", end=" ")
        for k in range(0,m):
            print("* ", end=" ")
        m+=2
        print("")
    for i in range(n+1,0,-1):
        for j in range(0,n-i+1):
            print("  ", end=" ")
        for k in range(0,m):
            print("* ", end=" ")
        m-=2
        print("")
    
