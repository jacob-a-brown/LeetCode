"""
Problem 20

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2==1:
            return False

        brackets = []

        open_brackets = '({['
        close_brackets = ')}]'

        o_to_c_brackets = {'(':')', '{':'}', '[':']'}
        c_to_o_brackets = {')':'(', '}':'{', ']':'['}


        for char in s:
            if char in open_brackets:
                brackets.append(char)
            elif char in close_brackets:
                if len(brackets) == 0:
                    return False
                if brackets[-1] == c_to_o_brackets[char]:
                    brackets.pop(-1)
                else:
                    return False
        if len(brackets) == 0:
            return True
        else:
            return False


if __name__ == '__main__':

    ins = ['()', '(){}[]', '(]']
    outs = [True, True, False]

    for i in range(len(ins)):
        sol = Solution().isValid(ins[i])
        out = outs[i]
        print(f'Example {i+1} is {sol==out} --> expected {out} got {sol}')