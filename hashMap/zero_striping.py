# https://bytebytego.com/exercises/coding-patterns/hash-maps-and-sets/zero-striping

from typing import List

def zero_striping(matrix: List[List[int]]) -> None:
    # Write your code here
    index=[]
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            num = matrix[r][c]
            if num == 0:
                index.append((r,c))
    
    for r,c in index:
        matrix[r]=[0]*len(matrix[0])
        for i in range(len(matrix)):
            matrix[i][c]=0
        
    return matrix


# 2nd approach with a basic row and col. 

def zero_striping(matrix: List[List[int]]) -> None:
    zero_rows = set()
    zero_cols = set()
    
    # Collect zero positions using hash sets
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)
    
    # Set rows to zero
    for r in zero_rows:
        matrix[r] = [0] * len(matrix[0])
    
    # Set columns to zero
    for c in zero_cols:
        for r in range(len(matrix)):
            matrix[r][c] = 0