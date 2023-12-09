import time
from collections import defaultdict
import math
from multiprocessing import Pool
import datetime

part_one = False
arr = open("input.txt").read().split("\n\n")


def one():
    maps = [defaultdict(int) for i in range(7)]
    seeds = []
    res = math.inf
    
    for s in arr[0].split(" ")[1:]:
        seeds.append(int(s))

    for i in range(1,8):
        ranges = arr[i].split("\n")[1:]
        for j in range(len(ranges)):
            nums = ranges[j].split(" ")
            key = int(nums[1])
            val = int(nums[0])
            length = int(nums[2])
            maps[i - 1][key] = (val,length - 1)

    for seed in seeds:
        curr = seed
        for i in range(7):
            for k,v in maps[i].items():
                if (curr - k) >= 0 and k + (curr - k) <= k + v[1]:
                    #print(k,curr,f'\t\tMap -> {i}')
                    curr = v[0] + (curr - k)
                    #print(f'New Curr -> {curr}')
                    break
        
        #print("---------------------")
        res = min(res,curr)
    print(res)
    return res



    
def two():
    start = datetime.datetime.now()
    
    maps = [defaultdict(int) for i in range(7)]
    seeds = []
    res = math.inf
    
    for s in arr[0].split(" ")[1:]:
        seeds.append(int(s))
    

    for i in range(1,8):
        ranges = arr[i].split("\n")[1:]
        for j in range(len(ranges)):
            nums = ranges[j].split(" ")
            key = int(nums[1])
            val = int(nums[0])
            length = int(nums[2])
            maps[i - 1][key] = (val,length - 1)
    
    j = 0
    while j < (len(seeds) - 1):
        for k in range(seeds[j],seeds[j] + seeds[j + 1]):
            curr = k
            for i in range(7):
                for k,v in maps[i].items():
                    if (curr - k) >= 0 and k + (curr - k) <= k + v[1]:
                        #print(k,curr,f'\t\tMap -> {i}')
                        curr = v[0] + (curr - k)
                        #print(f'New Curr -> {curr}')
                        break
            if curr < res:
                res = curr
                print(f'New Res Value -> {res}')
            
        j += 2


    
    print(res)
    print(f'Time Elapsed -> {str(datetime.datetime.now() - start).split(".")[0]}')
    return res

if __name__ == "__main__":
    one() if part_one else two()