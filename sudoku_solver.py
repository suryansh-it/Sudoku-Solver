import numpy as np


# rows = 9
# columns = 9

# print("enter numbers : ")
# numbers = list(map(int, input().split()))

# grid = np.array(numbers).reshape(rows, columns)
# print(grid)


grid = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,0,0]
]



def analyze(row, col , num):
    global grid

# check for number in row
    for i in range(0,9):
        if grid[row][i] == num:
            return False
        
# check for number in column        
    for i in range(0,9):
        if grid[i][col]:
            return False
        

# rounding of numbers to divide rows into sections of 3
    x = (row//3) * 3                
    y = (col//3) * 3

# check for number in square

    for i in range(0 ,9):
        for j in range(0 , 9):
            if grid [x+i][y + j] == num:
                return False
        
    return True


def solution():
    global grid
    for row in range(0,9):
        for col in range(0,9):
            if grid[row][col] == 0:
                for num in range(1,10):
                    if analyze(row, col , num):
                        grid[row][col] = num
                        solution()
                        grid[row][col] = 0
                return

    print(np.matrix(grid))
    input("more solutions")

solution()

