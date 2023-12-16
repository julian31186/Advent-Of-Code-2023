from collections import defaultdict
import datetime

part_one = True
arr = []
res = 0

arr = open("input.txt").read().split("\n")

def one():
    start = datetime.datetime.now()
    
    adj = defaultdict(list)
    direct = arr[0]
    dest = arr[-1].split("=")[0].strip()
    
    for i in range(2,len(arr)):
        curr = arr[i].split("=")
        neis = curr[1]
        neis = neis.strip()
        neis = neis[1:-1]
        neis = neis.split(",")  
        adj[curr[0].strip()].append(neis[0].strip()) 
        adj[curr[0].strip()].append(neis[1].strip())
    
    res = 0
    curr = arr[2].split("=")[0].strip()
    print(curr)
    i = 0
    while curr != dest:
        if direct[i] == "L":
            curr = adj[curr][0]
        else:
            curr = adj[curr][1]
        res += 1
        i += 1
        i %= len(direct)
    
    print(res)
    print(f'Time Elapsed -> {str(datetime.datetime.now() - start).split(".")[0]}')
    return res

def two():
    pass

if __name__ == "__main__":
    one() if part_one else two()