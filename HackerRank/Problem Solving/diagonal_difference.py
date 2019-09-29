def diagonalDifference(arr):
    d1 = 0
    d2 = 0
    i = 0
    while i != len(arr):
        d1 += arr[i][i]
        d2 += arr[i][len(arr) - i - 1]
        i += 1
    return abs(d1-d2)


matriz = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
print(diagonalDifference(matriz))
