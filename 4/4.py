from collections import defaultdict,deque
from functools import cache

part_one = False
arr = []
res = 0

with open("input.txt") as f:
    for row in f:
        if row[-1] == "\n":
            arr.append(row[:-1])
        else:
            arr.append(row)

scores = defaultdict(int)

def one():
    total = 0
    for i,row in enumerate(arr):
        winning_mine = row.split(":")[1].split("|")
        mine = set()
        match = 0
        for num in winning_mine[1].split(" "):
            if num != "": mine.add(int(num))
        
        #print(winning_mine[0].split(" "))
        for num in winning_mine[0].split(" "):
            if num != '' and int(num) in mine: 
                match += 1
        
        scores[i] = match
        total += (2**(match - 1)) if match > 0 else 0
        
    #print(total)
    return total
        
def two():
    one()
    print(scores)
    total = len(scores)
    q = deque()
    for k,v in scores.items(): q.append((k,v))
    
    while q:
        k,v = q.popleft()
        total += v
        for i in range(k + 1, k + 1 + v):
            q.append((i,scores[i]))
    
    
    print(total)
    return total

if __name__ == "__main__":
    one() if part_one else two()