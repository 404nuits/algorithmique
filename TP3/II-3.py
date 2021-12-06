def binary_search(dico, val):
    """Make a binary search within a sorted list of strings

    Args:
        dico (list): Sorted list of str values
        val (str): Value to search

    Returns:
        int: return index of element, -1 if not found
    """
    
    # Start search index
    left = 0

    # End search index
    right = len(dico) - 1

    # Middle
    m = int(left + right)

    # If we search within at least 1 element
    while left <= right:

        # If element is greater than the middle element, it is in the right part
        if dico[m] < val:
            
            # Thus, lower index is equal to the element just after the middle
            left = m + 1

        # Else, if element is lower than the middle, it is in the left part
        elif dico[m] > val:

            # Thus, greater index is the element before the middle
            right = m - 1

        # If element is directly in the middle, we found it, end
        else:
            return m
        
        # New middle element
        m = int(left + right)

    return -1

if __name__ == '__main__':
    dico = [
        'abricot',
        'banane',
        'concombre',
        'haricot',
        'kiwi',
        'peche'
    ]

    print(f'Index de abricot : {binary_search(dico, "abricot")}')
    print(f'Index de banane : {binary_search(dico, "banane")}')
    print(f'Index de peche : {binary_search(dico, "peche")}')
    print(f'Index de ananas : {binary_search(dico, "ananas")}')