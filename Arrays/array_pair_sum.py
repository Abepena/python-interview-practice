"""
Given an integer array, output all the unique pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)
would return 2 pairs:

 (1,3)
 (2,2)
"""
def pair_sum(arr, k):
    #exit if array doesnt have 2 numbers to make a pair
    if len(arr) < 2:
        return
    
    #set up tracking set
    seen = set()
    result = set()
    for num in arr:
        target = k - num
        if target in seen:
            #append the tuple of the (num, target) to result
            result.add((min(num,target), max(num,target)))
        else:
            #add num to seen .add method for sets
            seen.add(num)
            
#     return len(result)
    print('\n'.join([str(tup) for tup in result]))