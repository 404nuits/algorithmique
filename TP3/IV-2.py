def insertion_sort(tab):
    
    for i in range(1, len(tab)):

        current_val = tab[i]
        current_index = i

        while current_index > 0 and (tab[current_index - 1] > current_val):
            tab[current_index] = tab[current_index - 1]
            current_index -= 1

        tab[current_index] = current_val

    return tab

if __name__ == '__main__':
    tab = [69,97,83,9,62,98,80,85,65,72]

    print(insertion_sort(tab))