class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer = 0
        right_pointer = len(s) - 1


        while left_pointer < right_pointer:

            left_char = s[left_pointer]
            print(left_char)

            while not left_char.isalnum() and left_pointer < right_pointer:
                left_pointer += 1
                left_char = s[left_pointer]
            
            

            right_char = s[right_pointer]
            print(right_char)

            while not right_char.isalnum() and left_pointer < right_pointer:
                right_pointer -= 1
                right_char = s[right_pointer]

            if right_char.lower() != left_char.lower():
                return False

            left_pointer += 1
            right_pointer -= 1

        return True



        