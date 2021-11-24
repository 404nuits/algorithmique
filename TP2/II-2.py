#!/usr/bin/env python3

if __name__ == "__main__":
    
    n = input("Quelle est la longueur du côté ?")
    m = int(n) - 1
    for i in range(0,int(n)):
        for j in range(0,int(n)-m):
            print("* ",end =" ")
        m-=1
        print("")
    
