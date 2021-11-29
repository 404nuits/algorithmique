#!/usr/bin/env python3

if __name__ == "__main__":
    
    n = input("Quelle est la hauteur ?")
    for i in range(0,int(n)):
        for j in range(0,i):
            print("  ", end="")
        print("* *")
    
