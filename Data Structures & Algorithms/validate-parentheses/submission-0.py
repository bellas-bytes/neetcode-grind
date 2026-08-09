class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to hold the matching pairs
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
    
        for char in s:
            if char in bracket_map:
                # Pop the top element if there is any, else assign a dummy value '#'
                top_element = stack.pop() if stack else '#'
            
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack