# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# Testcase 1
# nums = [1,2,3,1]

# Testcase 2
# nums = [1,2,3,4]

# Testcase 3
nums = [1,1,1,3,3,4,3,2,4,2]

def containsDuplicate(nums: list[int]) -> bool:
    unique_numbers = set()
    for n in nums:
        if  n in unique_numbers:
            return True
        unique_numbers.add(n)        
    return False 

print(containsDuplicate(nums))