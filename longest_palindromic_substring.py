'''
Given a string s, return the longest palindromic substring in s.
'''

class Solution(object):
    def is_palindrome(self, s):
        '''
        Returns True if s is a palindrome. Else return False
        '''

        # numbers to iterate on
        if len(s) % 2 == 1:
            ni = (len(s)-1)//2
        else:
            ni = len(s)//2

        for i in range(ni):
            if s[i] != s[-(i+1)]:
                return False

        return True

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        '''
        1. Check if a string is a palindrome
        2. If it is a palindrome and it is longer than previous palindromes, save it and record its length
        3. If it is a palindrome and it is the same length as the previous palindromes, save it and continue
        '''
        
        palindrome_length = 1
        palindromes = []
        num_letters = len(s)

        for str_len in range(num_letters):
            for l in range(num_letters-str_len):
                str_to_eval = s[l:1+l+str_len]
                if self.is_palindrome(str_to_eval):
                    if len(str_to_eval) > palindrome_length:
                        palindromes = [str_to_eval]
                        palindrome_length = len(str_to_eval)
                    elif len(str_to_eval) == palindrome_length:
                        palindromes.append(str_to_eval)

        return palindromes

if __name__ == '__main__':

    strings = ['a', 'aa', 'abc', 'aba', 'abcba', 'abcbc', 'aabcbcb']
    expected_outs = [['a'], ['aa'], ['a', 'b', 'c'], ['aba'], ['abcba'], ['bcb', 'cbc'], ['bcbcb']]

    for i in range(len(strings)):
        output = Solution().longestPalindrome(strings[i])
        expected_output = expected_outs[i]
        print(f'Example {i+1} is {output == expected_output} -- Expected {expected_output} got {output}')