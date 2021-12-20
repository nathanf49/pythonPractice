def generate(lenTriangle):
    triangle = [[1]]
    for x in range(lenTriangle): # each new x is a new row of the triangle
        newRow = []
        for i in range(len(triangle[-1])+1): # adds elements to new row, should be 1 longer than the last row
            if i == 0 or i == len(triangle[-1]): # start and end of the row should be 1
                newRow.append(1)
            else: # adds numbers from last row in triangle
                newRow.append(triangle[-1][i-1] + triangle[-1][i])
            if len(newRow) == x+2: # adds newRow to triangle
                triangle.append(newRow)
    print(triangle)



if __name__ == '__main__':
    generate(4)




"""Given an integer numRows, return the first numRows of Pascal's triangle. max = 30 rows

In Pascal's triangle, each number is the sum of the two numbers directly above it"""