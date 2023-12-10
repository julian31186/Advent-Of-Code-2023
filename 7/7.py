from collections import Counter,defaultdict
from functools import cmp_to_key

part_one = True
arr = []
res = 0

arr = open("input.txt").read().split("\n")

cards = { "A" : 14, "K" : 13, "Q" : 12, "J" : 11, "T" : 10, "9" : 9, "8" : 8, "7" : 7, "6" : 6, "5" : 5, "4" : 4, "3" : 3, "2" : 2 }
sets = { "high_card" : [], "one_pair" : [], "two_pair" : [], "three_kind" : [], "full_house" : [], "four_kind" : [], "five_kind" : [] }

def compare(a,b):
    a = a[0]
    b = b[0]
    for i,j in zip(a,b):
        if cards[i] > cards[j]:
            return 1
        elif cards[i] < cards[j]:
            return -1
    return 0

def five_of_kind(hand):
    for i in range(len(hand) - 1):
        if hand[i] != hand[i + 1]: return False
    return True

def four_of_a_kind(hand):
    cache = Counter(hand)
    return max(cache.values()) == 4

def full_house(hand):
    cache = Counter(hand)
    return max(cache.values()) == 3 and min(cache.values()) == 2

def three_of_a_kind(hand):
    cache = Counter(hand)
    return max(cache.values()) == 3

def two_pair(hand):
    cache = Counter(hand)
    pair = defaultdict(int)
    for k,v in cache.items():
        pair[v] += 1
    return pair[2] == 2

def one_pair(hand):
    cache = Counter(hand)
    pair = defaultdict(int)
    for k,v in cache.items():
        pair[v] += 1
    return pair[2] == 1

def high_card(hand):
    return not five_of_kind(hand) and not four_of_a_kind(hand) and not full_house(hand) and not three_of_a_kind(hand) and not two_pair(hand) and not one_pair(hand)
    
def check(hand,bid):
    if five_of_kind(hand): 
        sets["five_kind"].append((hand,bid))
        sets["five_kind"].sort(key=cmp_to_key(compare))
    elif four_of_a_kind(hand): 
        sets["four_kind"].append((hand,bid))
        sets["four_kind"].sort(key=cmp_to_key(compare))
    elif full_house(hand):
        sets["full_house"].append((hand,bid))
        sets["full_house"].sort(key=cmp_to_key(compare))
    elif three_of_a_kind(hand): 
        sets["three_kind"].append((hand,bid))
        sets["three_kind"].sort(key=cmp_to_key(compare))
    elif two_pair(hand): 
        sets["two_pair"].append((hand,bid))
        sets["two_pair"].sort(key=cmp_to_key(compare))
    elif one_pair(hand): 
        sets["one_pair"].append((hand,bid))
        sets["one_pair"].sort(key=cmp_to_key(compare))
    elif high_card(hand): 
        sets["high_card"].append((hand,bid)) 
        sets["high_card"].sort(key=cmp_to_key(compare))
    
def one():
    res = 0
    for row in arr:
        curr = row.split(" ")
        check(curr[0],curr[1])
    
    #print(sets)
    idx = 1
    for k,v in sets.items():
        for i in v:
            #print(k,int(i[1]),idx)
            res += (int(i[1]) * idx)
            idx += 1
    
    print(res)
    return res

def two():
    pass

if __name__ == "__main__":
    one() if part_one else two()