def solve(bo):
    find = find_empty(bo)
    if find:
        row, col = find
    else:
        return True
    
    for i in range(1,10):
        if valid(bo, (row, col), i):
            bo[row][col] = i
            
            if solve(bo):
                return True
            
            bo[row][col] = 0
            
    return False

def valid(bo, pos, num):
    #check row
    for i in range(0, len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
        
    #check col
    for j in range(0, len(bo)):
        if bo[i][pos[1]] == num and pos[1] != i:
            return False
        
    #check box
    
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
            
    return True

