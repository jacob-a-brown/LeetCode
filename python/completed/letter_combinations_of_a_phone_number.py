"""
Problem 17

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if len(digits) == 0:
            return []
        
        number_to_letters = {'1': '',
                             '2': 'abc',
                             '3': 'def',
                             '4': 'ghi',
                             '5': 'jkl',
                             '6': 'mno',
                             '7': 'pqrs',
                             '8': 'tuv',
                             '9': 'wxyz',
                             '0': ''}

        res = []

        def combine_recursive(i, curStr):

            # base case
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            # recursive case
            else:
                for c in number_to_letters[digits[i]]:
                    combine_recursive(i+1, curStr + c)


        combine_recursive(0, "")

        return res

if __name__ == '__main__':
    in = '23'
    print(Solution().letterCombinations(in))