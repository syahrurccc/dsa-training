#  Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums [i]
# 
# return the answer in an array
# 
# example
# Input: nums = [8, 1, 2, 2, 3]
# Output: [4, 0, 1, 1, 3]
# Explanation: For nums[0]=8 there are 4 smaller numbers than it (1, 2, 2, and 3)
# for nums[1]=1 does not exist any smaller number than it
# and so on and so forth

nums = [8, 1, 2, 2, 3]

sorted_nums = sorted(nums)

d = {}

for i, num in enumerate(sorted_nums):
    if num not in d:
        d[num] = i
        
ret = []

for i in nums:
    ret.append(d[i])
    
print(ret)
    