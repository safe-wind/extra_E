
def sum_primary_diagonal(matrix:list[list[int]]) -> int:
    somma:int = 0
    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            if i == k:
                somma += matrix[i][k]
    return somma


def sum_secondary_diagonal(matrix:list[list[int]]) -> int:
    somma:int = 0
    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            if k == (len(matrix[i]) - 1 - i):
                somma += matrix[i][k]