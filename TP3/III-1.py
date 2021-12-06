def contains(string, substring):
    """Is true if the substring is included in the string

    Args:
        string (str): String in which to search
        substring (str): String to search within the first string

    Returns:
        boolean: True if string contains substring, False else
    """
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
    """Check if a submitted word is a good word for the pyramid game.
    For being a good word, the word must contains every letter of previous word,
    and be 1 char longer

    Args:
        old_word (str): previous submitted word
        new_word (str): current submitted word

    Returns:
        boolean: True if word is accepted, False else
    """
    # We init good to True and will change it if something is wrong
    good = True

    # We check every char in old word
    for c in old_word:

        # If this char is not in the new word,
        if not contains(new_word, c):

            # The word is not accepted, end of the loop
            good = False
            break

    # We also check is new word is not just 1 letter longer than the previous one
    if not (len(new_word) == len(old_word) + 1):
        good = False

    return good

def pyramid_game(word=""):
    """Method allowing to play pyramid game

    Args:
        word (str, optional): Previous word. Defaults to "" (to start the game). 
    """

    next_word = input('Rentrez le prochain mot : ')

    if good_word(word, next_word):

        pyramid_game(next_word)

    else:
        
        print("Perdu !")
    

if __name__ == '__main__':
    pyramid_game()