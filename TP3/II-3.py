def binary_search(dico, val):
    left = 0
    right = len(dico) - 1
    m = int(left + right)

    while left <= right:

        if dico[m] < val:
            left = m + 1

        elif dico[m] > val:
            right = m - 1

        else:
            return m
        
        m = int(left + right)

    return None

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