part_one = False
strs = []
res = 0

with open("input.txt") as f:
    for row in f:
        strs.append(row)
        
arr = []
for s in strs:
    curr = []
    for c in s:
        curr.append(c)
    arr.append(curr)
    
        
def check1(i,j):
    res = 0
    def is_valid(i,j):
        return i >= 0 and j >= 0 and i < len(arr) and j < len(arr[0])
    diff = [(0, -1),(1, -1),(1, 0),(1, 1),(0, 1), (-1, 1),(-1, 0),(-1, -1)]
    for di,dj in diff:
        ii = i + di
        jj = j + dj
        if is_valid(i + di,j + dj):
            if arr[ii][jj].isnumeric():
                curr = ""
                #print((i,j),ii,jj)
                k = jj
                while is_valid(ii,k-1) and arr[ii][k-1].isnumeric(): k -= 1
                while arr[ii][k].isnumeric(): 
                    curr += arr[ii][k]
                    arr[ii][k] = '.'
                    k += 1
                res += int(curr)
    
    #print(res)
    return res

def one():
    res = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if not arr[i][j].isnumeric() and arr[i][j] != '.' and arr[i][j] != '\n':
                res += check1(i,j)
                
    print(res)
    return res  
                    
            

def check2(i,j):
    res = 0
    def is_valid(i,j):
        return i >= 0 and j >= 0 and i < len(arr) and j < len(arr[0])
    diff = [(0, -1),(1, -1),(1, 0),(1, 1),(0, 1), (-1, 1),(-1, 0),(-1, -1)]
    adj = 0
    gears = []
    for di,dj in diff:
        ii = i + di
        jj = j + dj
        if is_valid(i + di,j + dj):
            if arr[ii][jj].isnumeric():
                curr = ""
                #print((i,j),ii,jj)
                k = jj
                while is_valid(ii,k-1) and arr[ii][k-1].isnumeric(): k -= 1
                while arr[ii][k].isnumeric(): 
                    curr += arr[ii][k]
                    arr[ii][k] = '.'
                    k += 1
                
                adj += 1
                gears.append(int(curr))
    
    if adj == 2:
        return gears[0] * gears[1]
    
    #print(res)
    return res

def two():
    res = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if not arr[i][j].isnumeric() and arr[i][j] != '.' and arr[i][j] != '\n' and arr[i][j] == "*":
                res += check2(i,j)
                
    print(res)
    return res  

if __name__ == "__main__":
    one() if part_one else two()