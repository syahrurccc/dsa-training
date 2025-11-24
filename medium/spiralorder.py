# Given an m x n matrix, return all elements of the matrix in spiral order
# example: 
# Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

def main():
    matrix = input("Input: ")
    print(spiral_order(matrix))

def spiral_order(matrix):
    ret = []
    while matrix:
        # add first row/list of matrix
        ret += (matrix.pop(0))
        
        # append last element of all lists in order
        if matrix and matrix[0]:
            for row in matrix:
                ret.append(row.pop())
        
        # add reverse of last row/list
        if matrix and matrix[0]:
            ret+=(matrix.pop()[::-1])
        
        # append first element of all rows/list in reverse
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                ret.append(row.pop(0))
    
    return ret

main()