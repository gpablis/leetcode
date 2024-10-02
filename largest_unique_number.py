# nums = [5,7,3,9,4,9,8,3,1]
nums = [9,9,8,8]

def largestUniqueNumber(nums: list[int]) -> int:
        dublicates = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    dublicates.add(nums[i])

        new_list = [n for n in nums if n not in dublicates]

        if len(new_list) > 0:
            max = 0
            for n in new_list:
                if n > max:
                    max = n
            return max
        else:
            return -1
        
print(largestUniqueNumber(nums))