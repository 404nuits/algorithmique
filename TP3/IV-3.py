def merge_sort(tab):
    """Perform a merge sort in a list of integers

    Args:
        tab (list): 

    Returns:
        list: Sorted list
    """

    # If the list has more than 1 element
    if len(tab) > 1:

        # We take the middle index of the list
        m = int(len(tab)/2)

        # We extract left and right list
        left = tab[:m]
        right = tab[m:]

        # We sort them
        left = merge_sort(left)
        right = merge_sort(right)

        # And we merge them
        tab = merge(left,right)
        return tab

    # If the list has one element, the program is done and we return the list
    else :
        return tab


def merge(left,right):
    """Merge two list

    Args:
        left ([type]): [description]
        right ([type]): [description]

    Returns:
        [type]: [description]
    """

    # Index for left and right tab
    i = 0
    j = 0

    merged = []

    while i < len(left) and j < len(right):

        if left[i] < right[j]:

            merged.append(left[i])
            i += 1

        else:

            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

if __name__ == '__main__':
    tab = [69,97,83,9,62,98,80,85,65,72]

    print(merge_sort(tab))