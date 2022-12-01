from aocd import get_data

# adding AOC folder to the system path
import sys
sys.path.insert(0, '/Users/johanol/repos/privat/AOC')
from helpers import transforms


data = get_data(day=15, year=2021)

input_data = transforms.get_array_of_numbers(data)
input_data_a = []

for number in input_data:
    input_data_a.append([int(i) for i in str(number)])

print(f"input_data_a: {input_data_a}")


import sys
 
# Naive recursive function to find the minimum cost to reach
# cell (m, n) from cell (0, 0)
def findMinCost_naive(matris, m=None, n=None):
    #print(f"Current location: ({m},{n})")
    # initialize m and n
    if not m and not n:
        m, n = len(matris), len(matris[0])
 
    # base case
    if not matris or not len(matris):
        return 0
 
    # base case, @tif Why return max size on error?
    if n == 0 or m == 0:
        return sys.maxsize
 
    # if we are in the first cell (0, 0)
    if m == 1 and n == 1:
        return 0 # Dont count the first cell, otherwise: matris[0][0]
 
    # include the current cell's cost in the path and recur to find the minimum
    # of the path from the adjacent left cell and adjacent top cell.
    return min(findMinCost(matris, m - 1, n), findMinCost(matris, m, n - 1))\
        + matris[m - 1][n - 1]
 



# Iterative function to find the minimum cost to traverse from the
# first cell to the last cell of a matrix
def findMinCost(cost):
 
    # `M × N` matrix
    (M, N) = (len(cost), len(cost[0]))
 
    # `T[i][j]` maintains the minimum cost to reach cell (i, j) from cell (0, 0)
    T = [[0 for x in range(N)] for y in range(M)]
 
    # fill the matrix in a bottom-up manner
    for i in range(M):
        for j in range(N):
            T[i][j] = cost[i][j]
 
            # fill the first row (there is only one way to reach any cell in the
            # first row from its adjacent left cell)
            if i == 0 and j > 0:
                T[0][j] += T[0][j - 1]
 
            # fill the first column (there is only one way to reach any cell in
            # the first column from its adjacent top cell)
            elif j == 0 and i > 0:
                T[i][0] += T[i - 1][0]
 
            # fill the rest with the matrix (there are two ways to reach any
            # cell in the rest of the matrix, from its adjacent
            # left cell or adjacent top cell)
            elif i > 0 and j > 0:
                T[i][j] += min(T[i - 1][j], T[i][j - 1])
 
    # last cell of `T[][]` stores the minimum cost to reach destination cell
    # (M-1, N-1) from source cell (0, 0)
    return T[M - 1][N - 1]
 


if __name__ == '__main__':
 
    input_test_data = [[1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
                       [1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
                       [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
                       [3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
                       [7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
                       [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
                       [1, 3, 5, 9, 9, 1, 2, 4, 2, 1],
                       [3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
                       [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
                       [2, 3, 1, 1, 9, 4, 4, 5, 8, 1]]

    m, n = len(input_data_a), len(input_data_a[0])
    print(f"m: {m}")
    print(f"n: {n}")
    
    total_cost = findMinCost(input_data_a) 
    print(f'The minimum cost is: {total_cost}')

    # Whe return max on error?
    # total_cost = findMinCost([[]]) 
    # print(f'TEST EMPTY: {total_cost}')

