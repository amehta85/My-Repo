class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1  # Increment count if the least significant bit is 1
            n >>= 1  # Right shift n by 1 to check the next bit
        return count
