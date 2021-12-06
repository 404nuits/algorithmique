def contains(string, substring):
    """Check if a substring is included in a string, and return the start index of the substring in the string

    Args:
        string (str): String in which to search
        substring (str): String to search within the first string

    Returns:
        int: Index of first char of substring in string if found, -1 else 
    """
    found = False
    i = 0
    start_index = -1

    for char_index,char in enumerate(string):
        
        if char == substring[i]:
            
            if i == 0:
                start_index = char_index

            i += 1

            if i == len(substring):
                
                found = True
                break

        else:
            i = 0

    if found:
        return start_index
    else:
        return -1

def replace(text,old,new):
    """Replace first occurence of old string by new string in text

    Args:
        text (str): Text in which old string will be replaced
        old (str): Old string to replace
        new (str): New string that will replace old string

    Returns:
        str: New text with old replaced by new
    """

    # We search start index of old
    start_index = contains(text,old)

    # End index of old
    end_index = start_index + len(old) - 1

    # Init new text containing new string
    new_text = ""

    # If old is found in text
    if start_index != -1:

        for i,c in enumerate(text):

            # We add each char of text to new_text
            # But only if char index correspond to old string
            if i < start_index or i > end_index:
                new_text += c

            # If index correspond to first char of old string, we put new string in new_text
            elif i == start_index:
                new_text += new

    # If old is not found, we directly put text in new_text
    else:
        new_text = text    
    
    return new_text

def replace_all(text,old,new):
    """Replace every occurence of old by new in text

    Args:
        text (str): Text in which old will be replaced
        old (str): Old string to be replaced
        new (str): New string to replace old with

    Returns:
        str: new version of the text
    """
    
    # We find first occurence of old string in text
    
    found = contains(text, old) == -1

    # While there is an occurence,
    while found:

        # We replace this occurence by new text
        text = replace(text, old, new)

        # And we find next occurence
        found = contains(text, old) == -1

    return text

if __name__ == '__main__':

    text = input("Rentrez un texte : ")
    old = input("Rentrez la chaîne à remplacer : ")
    new = input("Rentrez la chaîne par laquelle la remplacer : ")

    print(replace_all(text, old, new))
