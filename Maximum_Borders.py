# Read the num of test case
test = int(input())

# Read rows and Columns for each test case
for t in range(test):
    line = input().split()
    if not line : continue
    row, cols = map(int,line)

 # 1. Grid storage
    grid = []
    for i in range(row):
        grid.append(input())

    max_border = 0

    # 2. Find max in rows
    for i in range(row):
        count = 0
        for char in grid[i]:
            if char == '#':
                count += 1
                if count > max_border:
                    max_border = count
            else:
                count = 0

    # 3. Find max in columns
    # We use grid[i][j] to look at row 'i', column 'j'
    for j in range(cols):
        count = 0
        for i in range(row):
            if grid[i][j] == '#':
                count += 1
                if count > max_border:
                    max_border = count
            else:
                count = 0

    # 4. Print the result once per test case
    print(max_border)

    
