class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_num = 0
        for i in range(32):  # Process 32 bits
            reversed_num <<= 1  
            reversed_num |= n & 1  
            n >>= 1  
        return reversed_num