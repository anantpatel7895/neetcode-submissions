class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        s = set()
        s.add(nums[0])

        for i in range(1, len(nums)):
            n = nums[i]

            second_number = target - n

            if second_number in s:
                break
            else:
                s.add(n)

        print(i)
        print(second_number)
        j = i

        for n in range(len(nums)):

            if nums[n] == second_number:
                i = n
                break
        
        return [i, j]


            




        