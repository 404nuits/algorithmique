def contains(string, substring):
    found = False
    i = 0

    for char in string:
        
        if char == substring[i]:

            i += 1

            if i == len(substring):
                
                found = True
                break

        else:
            i = 0

    return found

if __name__ == '__main__':

    print(f'Monique contient nique : {contains("Monique","niques")}')