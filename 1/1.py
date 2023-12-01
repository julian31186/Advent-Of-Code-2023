part_one = False
arr = []
res = 0

with open("input.txt") as f:
    for row in f:
        arr.append(row)

def one():
    res = 0
    for row in arr:
        curr = ""
        for l in range(len(row)):
            if row[l].isnumeric():
                curr += row[l]
                break
        for r in range(len(row) - 1, -1, -1):
            if row[r].isnumeric():
                curr += row[r]
                break
        res += int(curr)
    print(res)
    return res

def two():
    import math
    digits = {"one" : 1,"two" : 2,"three" : 3,"four" : 4,"five" : 5,"six" : 6,"seven" : 7,"eight" : 8,"nine" : 9}
    res = 0
    
    
    return res
    
    
if __name__ == "__main__":
    one() if part_one else two()