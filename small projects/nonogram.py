

# -------------------------setting-------------------------
def prt_grid(g,hhint,vhint): # grid[row][colum]
    print(" ",end="")
    print("_"*(2*size-1))
    for i in grid:
        print("|",end="")
        for j in i:
            print(j,end=" ")
        print()
    print(vhint)  # written on the top
    print(hhint)  # written on the left

def total(row):
    result = 0
    for i in row:
        result += i
    result += (len(row)-1)
    return result

def horizontal_fill(row,hint,gap):
    pointer = 0
    count = 0
    stack = hint[count]
    gap_stack = gap
    while pointer != total(hint):
        if stack == 0:
            count += 1
            stack = hint[count]
            gap_stack = gap
            if gap == 0:
                row[pointer] = 'x'
            pointer +=1
            continue
        if gap_stack > 0:
            gap_stack-=1
        else:
            row[pointer] = 'o'
        stack -= 1
        pointer += 1
        
size = int(input("size? : "))
grid = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(0)
    grid.append(row)

vertical_hint = []
for i in range(size):
    vertical_hint.append(None)

vertical_input = input("vertical hint \n").split(",")
for i in range(size):
    vertical_hint[i] = vertical_input[i].split(" ")
    vertical_hint[i] = [int(item) for item in vertical_hint[i]]

horizontal_hint = []
for i in range(size):
    horizontal_hint.append(None)

horizontal_input = input("horizontal hint \n").split(",")
for i in range(size):
    horizontal_hint[i] = horizontal_input[i].split(" ")
    horizontal_hint[i] = [int(item) for item in horizontal_hint[i]]

prt_grid(grid,horizontal_hint,vertical_hint)

# -------------------------solving-------------------------
for i in range(size):
    if horizontal_hint[i] == [0]:
        for j in range(size):
            grid[i][j] = 'x'
            continue
    
    if max(horizontal_hint[i]) > (size - total(horizontal_hint[i])):
        gap = (size - total(horizontal_hint[i]))
        horizontal_fill(grid[i], horizontal_hint[i], gap)



for i in range(size):
    if vertical_hint[i] == [0]:
        for j in range(size):
            grid[j][i] = 'x'
            
    if max(vertical_hint[i]) > (size - total(vertical_hint[i])):
        gap = (size - total(vertical_hint[i]))
        clone = list(zip(*grid))
        clone = [list(item) for item in clone]
        horizontal_fill(clone[i], vertical_hint[i], gap)
        grid = list(zip(*clone))
        grid = [list(item) for item in grid]

prt_grid(grid, horizontal_hint, vertical_hint)