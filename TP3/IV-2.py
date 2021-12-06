def insertion_sort(tab):
    """Perform an insertion sort in a list of integers

    Args:
        tab (list): List of integers

    Returns:
        list: Sorted list
    """
    

    for i in range(1, len(tab)):

        current_val = tab[i]
        current_index = i

        # Move elements from start to i-1 index that are greater than the current value, to the previous index
        while current_index > 0 and (tab[current_index - 1] > current_val):
            tab[current_index] = tab[current_index - 1]
            current_index -= 1

        tab[current_index] = current_val

    return tab

if __name__ == '__main__':
    tab = [69,97,83,9,62,98,80,85,65,72]

    print(insertion_sort(tab))