class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        s = set()

        for n in nums:
            print(n)
            if n in s:
                return True
            else:
                s.add(n)

        return False
        