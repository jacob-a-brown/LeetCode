'''
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        string_x = str(x)

        reversed_character_list = []

        for char in string_x:
            reversed_character_list.insert(0, char)
        
        if reversed_character_list[-1] == '-':
            negative_sign = reversed_character_list.pop(-1)
            reversed_character_list.insert(0, negative_sign)

        reversed_string_x = ''.join(reversed_character_list)
        reversed_x = int(reversed_string_x)

        if reversed_x > 2**31 - 1 or reversed_x < -2**31:
            return 0

        return reversed_x



if __name__ == '__main__':
    ins = [123, -123, 120]
    expected_outs = [321, -321, 21]
    for i in range(len(ins)):
        sol = Solution().reverse(ins[i])
        if sol == expected_outs[i]:
            correctness = 'correct'
        else:
            correctness = 'false'
        print(f'Example {i+1} is {correctness} -- expected {expected_outs[i]} got {sol}')