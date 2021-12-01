def selection_sort(tab):

    for i in range(len(tab)):

        mini = i

        for j in range(i+1, len(tab)):

            if tab[j] < tab[mini]:
                mini = j

        tab[i], tab[mini] = tab[mini], tab[i]

    return tab

if __name__ == '__main__':
    tab = [69,97,83,9,62,98,80,85,65,72]

    print(selection_sort(tab))