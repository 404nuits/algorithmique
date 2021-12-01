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

def good_word(old_word, new_word):

    good = True

    for c in old_word:
        if not contains(new_word, c):
            good = False
            break

    if not (len(new_word) == len(old_word) + 1):
        good = False

    return good

def pyramid_game(word=""):
    
    next_word = input('Rentrez le prochain mot : ')
    if good_word(word, next_word):
        pyramid_game(next_word)
    else:
        print("Perdu !")
    

if __name__ == '__main__':
    pyramid_game()