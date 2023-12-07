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
        total += (2**(match - 1)) if match > 0 else 0
        
    #print(total)
    return total
        
def two():
    total = len(arr) #make len of scores (1 for each card we have)
    counts = [1] * len(arr)
    wins = defaultdict(int)
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
        wins[i] = match
    
    for i in range(len(counts) -1, -1, -1):
        for j in range(i + 1, i + 1 + wins[i]):
            counts[i] += counts[j]
            
    print(counts)
    print(sum(counts))
    return sum(counts)

if __name__ == "__main__":
    one() if part_one else two()