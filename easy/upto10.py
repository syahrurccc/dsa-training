# Problem:
# Given a list of integers nums, return True if the list contains two numbers that add up to 10, otherwise return False.

# Input: [3, 4, 7, 1]
# Output: True
# Explanation: 3 + 7 = 10

# Input: [2, 2, 5]
# Output: False
# Explanation: no two numbers add up to 10


nums = [1, 3, 5, 4, 7]

seen = set()

for x in nums:
    complement = 10 - x
    if complement in seen:
        print(True)
        exit(0)
    seen.add(x)

print(False)