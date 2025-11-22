# Problem:
# Given a string s, return true if it is a palindrome, and false otherwise.
# Ignore non-alphanumeric characters and case sensitivity.
# 
# Example
# Input: "A man, a plan, a canal: Panama"
# Output: true
# Explanation: When cleaned it becomes "amanaplanacanalpanama"
# 
# Constraints
# Solve it in O(n) time.
# Try to do it without creating a reversed copy of the string — use pointers.

def main():
    user_input = input("Input: ")
    print(is_palindrome(user_input))

def is_palindrome(input):
    p = []
    for i in input:
        if i.isalnum():
            p.append(i.lower())

    left = 0
    right = len(p)- 1
    
    while left < right:
        if p[left] != p[right]:
            return False
        
        left += 1
        right -= 1
    
    return True

main()
    