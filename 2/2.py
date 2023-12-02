part_one = False
arr = []
res = 0

with open("input.txt") as f:
    for row in f:
        arr.append(row)

def one():
    res = 0
    #12 red cubes, 13 green cubes, and 14 blue cubes
    for i,row in enumerate(arr):
        row = row.split(":")
        id = int(row[0].split(" ")[1])
        flag = True
        
        sets = row[1].split(";")
        for set in sets:
            set = set.strip()
            set = set.replace(",","")
            set = set.split(" ")
            print(set)
            r,g,b = 0,0,0
            for j in range(len(set) - 1):
                if set[j + 1] == 'red':
                    r += int(set[j])
                elif set[j + 1] == 'blue':
                    b += int(set[j])
                elif set[j + 1] == 'green':
                    g += int(set[j])
            
                if r > 12 or g > 13 or b > 14:
                    flag = False
                    break
            
                if not flag: break
        
        if flag: res += id
        
    print(res)
    return res
    
def two():
    res = 0
    for i,row in enumerate(arr):
        row = row.split(":")
        id = int(row[0].split(" ")[1])
        sets = row[1].split(";")
        
        
        r,g,b = 0,0,0
        for set in sets:
            set = set.strip()
            set = set.replace(",","")
            set = set.split(" ")
            print(set)
            for j in range(len(set) - 1):
                if set[j + 1] == 'red':
                    r = max(r,int(set[j]))
                elif set[j + 1] == 'blue':
                    b = max(b,int(set[j]))
                elif set[j + 1] == 'green':
                    g = max(g,int(set[j]))
        
        res += (r*g*b)
        
    print(res)
    return res

if __name__ == "__main__":
    one() if part_one else two()