import math

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(char for char in s if char.isalnum()).lower()

        for index, letter in enumerate(clean):
            if index > math.floor(len(clean)/2):
                break;

            if letter == clean[len(clean) - index - 1]:
                continue;
            else:
                return False
        
        return True

