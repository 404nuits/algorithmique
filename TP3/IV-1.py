def selection_sort(tab):
    """Perform a selection sort within a list of integers

    Args:
        tab (list): List of integers

    Returns:
        list: Sorted list
    """
    for i in range(len(tab)):

        # Set lowest element to lowest index in which to search
        mini = i

        # Search for lowest element
        for j in range(i+1, len(tab)):
            
            if tab[j] < tab[mini]:
                mini = j

        # Switch i elem and lowest element
        tab[i], tab[mini] = tab[mini], tab[i]

    return tab

if __name__ == '__main__':
    tab = [69,97,83,9,62,98,80,85,65,72]

    print(selection_sort(tab))