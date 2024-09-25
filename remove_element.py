# In-place algorithm
#   In computer science, an in-place algorithm is an algorithm that operates directly 
#   on the input data structure without requiring extra space proportional to the input size. 
#   In other words, it modifies the input in place, without creating a separate copy of the data structure.

# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# Then return the number of elements in nums which are not equal to val
# The order of the elements may be changed.

def removeElement(nums: list[int], val: int) -> int:
    
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            count+=1
            nums.insert(0,nums[i])
            nums.pop(i+1)
    
    print(nums)

    return count

# Testcase 1
# nums = [3,2,2,3]
# val = 3

# Testcase 2
nums = [0,1,2,2,3,0,4,2]
val = 2

k=removeElement(nums, val)
print(k)