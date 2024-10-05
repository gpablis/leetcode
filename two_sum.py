
# Approach 1: Brute Force
# The brute force approach is simple. Loop through each element x and find if there is another value that equals
# def twoSum(nums: list[int], target: int) -> list[int]:
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i,j]
            
# Time complexity: O(n^2)
# Space complexity: O(1), The space required does not depend on the size of the input array, so only constant space is used.             

# Approach 2: Two-pass Hash Table
def twoSum(nums: list[int], target: int) -> list[int]:
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i

    for i in range(len(nums)):
        n2 = target - nums[i]
        if n2 in hashmap and hashmap[n2]!=i:
            return [i, hashmap[n2]]

# Testcase 1
# nums = [2,7,11,15]
# target = 9

# Testcase 2
# nums = [3,2,4]
# target = 6

# Testcase 3
nums = [3,3] 
target = 6

print(twoSum(nums,target))
