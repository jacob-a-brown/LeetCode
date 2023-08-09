class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        '''
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000
        '''

        letter_to_int = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        summation = 0
        num_letters = len(s)
        skip_next_letter = False
        for i in range(num_letters):
            if skip_next_letter:
                skip_next_letter = False
                continue

            current_letter = s[i]

            if i < num_letters-1:
                next_letter = s[i+1]

                if letter_to_int[current_letter] >= letter_to_int[next_letter]:
                    summation += letter_to_int[current_letter]
                else:
                    summation += (letter_to_int[next_letter] - letter_to_int[current_letter])
                    skip_next_letter = True
            else:
                summation += letter_to_int[current_letter]

        return summation


if __name__ == '__main__':

    # example 1
    s = 'III'
    out = 3
    sol = Solution().romanToInt(s)
    print(f'example 1 {sol == out} --- {sol} expected {out}')

    # example 2
    s = 'LVIII'
    out = 58
    sol = Solution().romanToInt(s)
    print(f'example 2 {sol == out} --- {sol} expected {out}')

    # example 3
    s = 'MCMXCIV'
    out = 1994
    sol = Solution().romanToInt(s)
    print(f'example 3 {sol == out} --- {sol} expected {out}')