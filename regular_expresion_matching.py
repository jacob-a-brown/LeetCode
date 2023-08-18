'''
Problem 10

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).
'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        '''
        1. 
        '''

        # first case: only 1 letter in s
        if len(s) == 1:
            if p[0] == '.' or p[0] == s[0]:
                return True
            else:
                return False

        # second case: more than 1 letter in s
        else:
            for index in range(len(p)):
                
                # automatically matches any single character.
                if p[i] == '.':
                    continue

                # automatically matches everything
                elif p[i] == '.' and p[i+1] == '*':
                    return True

                elif p[]




if __name__ == '__main__':

    in_s = ['aa', 'aa', 'ab']
    in_p = ['a', 'a*', '.*']
    expected_outs = [False, True, True]

    for i in range(len(in_s)):
        sol = Solution().isMatch(in_s[i], in_p[i])
        print(f'Example {i+1} is {sol==expected_outs[i]} -- expected {expected_outs[i]} got {sol}')