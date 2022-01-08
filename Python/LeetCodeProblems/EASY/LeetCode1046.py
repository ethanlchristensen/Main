# LEET CODE 1046 Last Stone Weight
# given a list of stones, for each turn, pick the
# two largest stones. If x == y remove them both. 
# if x < y then stone y = y - x and stone x is removed.
# continue until there is one stone. return this stone

def lastStoneWeight(stones):
    stones.sort()
    for i in range(len(stones) - 1, 0, -1):
        print(stones)
        stones[i-1] = stones[i] - stones[i-1]
        stones.pop(i)
        stones.sort()
    return(stones[0])

my_stones = [2,7,4,1,8,1]
print(lastStoneWeight(my_stones))
my_stones = [1]
print(lastStoneWeight(my_stones))