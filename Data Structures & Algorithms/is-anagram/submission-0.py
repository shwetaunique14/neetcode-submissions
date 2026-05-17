class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        count = {}
        
        # Count frequencies for string s
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        # Decrement frequencies for string t
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
            
        return True