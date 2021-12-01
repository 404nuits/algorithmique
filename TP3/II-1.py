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

if __name__ == '__main__':
    tab = [1,2,3,4,5,6,7,8,9]

    print(f'Index de 1 : {find(tab,1)}')
    print(f'Index de 5 : {find(tab,5)}')
    print(f'Index de 9 : {find(tab,9)}')
    print(f'Index de 10 (ne figure pas dans le tableau): {find(tab,10)}')