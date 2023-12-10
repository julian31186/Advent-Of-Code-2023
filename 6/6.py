import bisect
import math

part_one = False
arr = []
res = 0

arr = open("input.txt").read().split("\n")

def one():
    rows = []
    res = 1
    for r in arr:
        curr = r.split(":")[1].strip().split(" ")
        while '' in curr: curr.remove('')
        rows.append(curr)
    
    for i in range(len(rows[0])):
        time = int(rows[0][i])
        distance = int(rows[1][i])
        amount = 0
        for j in range(1,time):
            if (time - j) * j > distance:
                amount += 1
        res *= amount
    print(res)
    return res
    

def two():
    time = ""
    distance = ""
    
    res = 1
    flag = True
    for r in arr:
        curr = r.split(":")[1].strip().split(" ")
        while '' in curr: curr.remove('')
        if flag:
            flag = False 
            time = ''.join(curr)
        else: distance = ''.join(curr)
    
    time = int(time)
    distance = int(distance)
    
    #Test
    # time = 7
    # distance = 9
    
    #print([i for i in range(1,time + 1)])
    
    def check(x):
        return (time - x) * x > distance
    low = math.inf
    high = 0
    for i in range(1,time + 1): 
        #print(i,check(i))
        if check(i):
            high = max(high,i)
            low = min(low,i)
            
    #print(low,high)

    res = (high - low) + 1
    print(res)
    return res

if __name__ == "__main__":
    one() if part_one else two()