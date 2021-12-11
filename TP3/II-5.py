def find(tab,wanted_val):
    """find a val in a list of integers

    Args:
        tab (list): list of integer values
        wanted_val (int): value to search in list

    Returns:
        int: Index of wanted_val, -1 if not found
    """

    # Init the index of wanted_val to -1 in the case it's not in the list
    index = -1
    

    # Interate through the list with index and value of each element
    for i,val in enumerate(tab):

        if val == wanted_val:
            index = i
            break
    
    return index


def contains(string, substring,):
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


def contains_all(string, substring):
    """Check for a string if it contains a substring several times. It then returns the starting index of each occurence of the substring in the string
    It check for the first occurence with contains(), then cut string from the start to this occurence and reiterate the process until nothing is found

    Args:
        string (str): Complete string
        substring (str): A substring to search in string

    Returns:
        list: Starting indexes of each occurence of substring in string, empty array if the substring is not found
    """

    # We get the index of the first occurence
    found = contains(string, substring)

    # Init array of found indexes
    found_array = []

    # Init a variable that gets the length of the cut part of string
    cut_length = 0

    # While there is a substring occurence found in string
    while (found != -1):
        #print(f'Cut length : {cut_length}, Found : {found}, Real index : {cut_length + found}')
        
        # We append the occurence
        found_array.append(found+cut_length)

        last_string = string

        # We cut the string from the last char of the current substring occurence
        string = string[found+len(substring):]

        # And we calculate the new cut length
        cut_length += len(last_string) - len(string)

        # Finally, we look for the next occurence
        found = contains(string, substring)
        

    return found_array


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
    
    # Init new version of text
    new_text = ""

    # Array of starting index of every occurence of old string in text
    found_start_indexes = contains_all(text,old)

    # Init starting and ending index of current occurence
    start_index = -1
    end_index = -1

    for i,c in enumerate(text):
        
        # If current index is part of starting indexes of old string occurences,
        if find(found_start_indexes,i) != -1:

            # We change start and ending index values
            start_index = i
            end_index = i + len(old)

            # And we add new string to new version of text
            new_text += new

        # If current char is not whithin an occurence's indexes, we add it to the new string
        if not (i >= start_index and i < end_index):
            new_text += c

    return new_text


if __name__ == '__main__':

    text = input("Rentrez un texte : ")
    old = input("Rentrez la chaîne à remplacer : ")
    new = input("Rentrez la chaîne par laquelle la remplacer : ")

    print(replace_all(text, old, new))
