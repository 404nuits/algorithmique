def zeros(n):
    """Return a list of n zeros
    Pre : n > 0

    Args:
        n (int): number of zeros
    """

    res = []

    for i in range(n):
        res.append(0)

    return res

def print_matrix(m):
    """Print a matrix

    Args:
        m (list): matrix of shape [[line],[line],[line],...]
    """
    for ligne in m:
        for val in ligne:
            print(val,end="\t")
        print("")

def matrix_product(m1,m2):
    """Product of two matrices

    Args:
        m1 (list): matrix of shape [[line],[line],[line],...]
        m2 (list): matrix of shape [[line],[line],[line],...]

    Returns:
        list: matrix of shape [[line],[line],[line],...]
    """

    m_res = []

    for ligne_m1 in m1:

        l_res = zeros(len(m2[0]))

        for j,ligne_m2 in enumerate(m2):

            for k, val_m2 in enumerate(ligne_m2):
                l_res[k] += val_m2*ligne_m1[j]

        m_res.append(l_res)
    
    return m_res


if __name__ == '__main__':

    matrice_1 = [[5,1],
                 [2,3],
                 [3,4]]

    matrice_2 = [[1,2,0],
                 [4,3,-1]]

    print_matrix(matrix_product(matrice_1,matrice_2))

