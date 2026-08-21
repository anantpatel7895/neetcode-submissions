class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        sorted_nums = sorted(nums)

        longest_seq = 1
        curr_longest_seq = 1

        for i in range(len(sorted_nums) - 1):

            if sorted_nums[i+1] - sorted_nums[i] == 1:
                curr_longest_seq += 1

            elif sorted_nums[i+1] - sorted_nums[i] == 0:
                curr_longest_seq += 0

            else:
                curr_longest_seq = 1

            longest_seq = max(longest_seq, curr_longest_seq)
            print(longest_seq)


        return longest_seq

            