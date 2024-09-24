def removeDuplicates(nums: list[int]) -> int:
        l = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[l] = nums[i]
                l+=1
        return l



# nums = [1,1,2]

nums = [0,0,1,1,1,2,2,3,3,4]
k = removeDuplicates(nums)
print(k)