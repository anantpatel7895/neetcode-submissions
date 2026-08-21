class Solution:
    def findMin(self, nums: List[int]) -> int:

        l_p = 0
        r_p = len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return min(nums[0], nums[1])


        minima = float("inf")

        while l_p <= r_p:
            mid = (l_p + r_p) // 2
            
            if nums[mid] >= nums[l_p]:
                minima = min(minima, nums[l_p])
                l_p = mid + 1
            else:
                minima = min(minima, nums[mid])
                r_p = mid -1

        return minima







