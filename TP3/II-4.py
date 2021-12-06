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

    # Iterate through every char of the string
    for char in string:
        
        # If the current char equal the i char of the substring
        if char == substring[i]:

            # We will compare next char in string with next char in substring 
            i += 1

            # If i has reached the length of the substring
            if i == len(substring):
                
                # We found the complete substring in string
                found = True

                # So we end the loop
                break

        else:
            i = 0

    return found

if __name__ == '__main__':

    print(f'Est-ce qu\'il y a un a dans lasagnes ?  : {contains("lasagnes","a")}')
    print(f'Est-ce qu\'il y a un z dans lasagnes ?  : {contains("lasagnes","z")}')
