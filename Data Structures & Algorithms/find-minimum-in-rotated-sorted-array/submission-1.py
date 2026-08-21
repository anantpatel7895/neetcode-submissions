class Solution:
    def findMin(self, nums: List[int]) -> int:

        minima = float("inf")

        for n in nums:

            if n < minima:
                minima = n

        return minima







