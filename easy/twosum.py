# Given an array of integers nums and an integer target, return indices of the two numbers
# such that they add up to target
# 
# You may assume that each input would have exactly one solution and you may not use the same solution twice
# 
# example
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because nums[0] + nums[1] == 9 we return [0, 1]
# 
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]

nums = [2, 7, 11, 15]
target = 9

hash_map = {}

for indx, val in enumerate(nums):
    diff = target - val
    if diff in hash_map:
        print([hash_map[diff], indx])
        exit(0)
    hash_map[val] = indx