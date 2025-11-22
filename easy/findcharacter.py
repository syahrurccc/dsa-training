# Problem:
# Given a string s, return the first character that appears only once.
# If no such character exists, return "_".

# Input: "abacabad"
# Output: "c"
# Explanation: 'c' is the first non-repeating character.

# Input: "aaaa"
# Output: "_"

# Constraints
# Try to solve it in O(n) time.
# Use a dictionary / hash map to count frequencies.

data = input("Input: ")

counts = {}

for c in data:
    if c not in counts:
        counts[c] = 1
    else:
        counts[c] += 1

for c in data:
    if counts[c] == 1:
        print(c)
        exit(0)

print("_")
        