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
    digits = {"one" : 1,"two" : 2,"three" : 3,"four" : 4,"five" : 5,"six" : 6,"seven" : 7,"eight" : 8,"nine" : 9}
    res = 0
    
    for row in arr:
        s = ""
        for i in range(len(row)):
            if row[i].isnumeric(): s += row[i]
            elif row[i:i + 3] in digits.keys():
                s += str(digits[row[i:i + 3]])
            elif row[i:i + 4] in digits.keys():
                s += str(digits[row[i:i + 4]])
            elif row[i:i + 5] in digits.keys():
                s += str(digits[row[i:i + 5]])
    
        
        curr = ""
        for l in range(len(s)):
            if s[l].isnumeric():
                curr += s[l]
                break
        for r in range(len(s) - 1, -1, -1):
            if s[r].isnumeric():
                curr += s[r]
                break
        print(curr)
        res += int(curr)
        

    print(res)
    return res
    
    
if __name__ == "__main__":
    one() if part_one else two()