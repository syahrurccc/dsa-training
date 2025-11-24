# Problem:
# Given a string containing only the characters ()[]{}, determine if the brackets are valid.

# A string is valid if:
# Every opening bracket has a matching closing bracket
# Brackets close in the correct order

# Examples
# Input: "()[]{}"
# Output: True

# Input: "(]"
# Output: False

# Input: "([{}])"
# Output: True

def main():
    data = input("Input: ")
    print(check_bracket(data))

def check_bracket(data):
    pairs = { ")": "(", "]": "[", "}": "{" }
    stack = []
    
    for c in data:
        if c in ["(", "[", "{"]:
            stack.append(c)
        elif c in pairs:
            if not stack:
                return False
            elif pairs[c] != stack[-1]:
                return False
            stack.pop()
             
    if not stack:
        return True
    return False

main()