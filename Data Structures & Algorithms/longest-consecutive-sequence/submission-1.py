class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_seq = 0

        for num in nums:
            if not num-1 in numset:
                seq_num = num + 1
                while seq_num in numset:
                    seq_num += 1
                    
                max_seq = max(max_seq, seq_num-num)
        
        return max_seq
