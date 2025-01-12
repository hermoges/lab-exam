def find_matrix_shape(matrix):
    rowdlen = len(matrix)
    coldlen = len(matrix[0]) if rowdlen > 0 else 0
    return (rowdlen, coldlen)
find_matrix_shape([[1, 3, 6], [8, 10, 12], [14, 16, 18]])    
print(find_matrix_shape([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
