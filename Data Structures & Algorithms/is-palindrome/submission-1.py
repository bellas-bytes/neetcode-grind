import re # to use regex
import math

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(clean)

        for index, letter in enumerate(clean):
            if index > math.floor(len(clean)/2):
                break;

            if letter == clean[len(clean) - index - 1]:
                continue;
            else:
                return False
        
        return True

