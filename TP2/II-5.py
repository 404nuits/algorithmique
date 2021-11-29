#!/usr/bin/env python3

if __name__ == "__main__":
    
    n = input("Quelle est la longueur du côté ?")
    for i in range(0,int(n)):
        print("* ",end=" ")
    print("")
    for i in range(1,int(n)-1):
        print("* ",end=" ")
        for j in range(1,int(n)-1):
            print("  ",end =" ")
        print("* ")
    if int(n) != 1:    
        for i in range(0,int(n)):
            print("* ",end=" ")
    print("")
    
