class Solution(object):
    def isAnagram(self, s, t):
        
        # If lengths differ, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        char_count = {}
        
        # Count characters in s
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Subtract counts based on characters in t
        for char in t:
            char_count[char] = char_count.get(char, 0) - 1
        
        # Check if all counts are zero
        for count in char_count.values():
            if count != 0:
                return False
        
        return True

