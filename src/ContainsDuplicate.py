class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()  # an empty set to keep track of seen numbers
        for num in nums:
            if num in seen:
                return True  # if number is already in the set return True
            seen.add(num)  # Add the number to the set
        return False  # if no duplicates are found then return False
