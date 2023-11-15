/*
Problem 3

Given a string s, find the length of the longest substring without repeating characters.
*/

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    var letters = new Map();
    var left_pointer = 0;
    var max_string_length = 0;

    for (let right_pointer = 0; right_pointer < s.length; right_pointer++) {
        let letter = s[right_pointer];
        if (!letters.has(letter)) {
            // letter is not in current window
            var max_string_length = Math.max(max_string_length, right_pointer - left_pointer + 1);
        }
        else {
            if (letters.get(letter) < left_pointer){
                // letter is not in current window
                var max_string_length = Math.max(max_string_length, right_pointer - left_pointer + 1);
            }
            else{
                // letter is in the current window
                var left_pointer = letters.get(letter) + 1;
            }
        }

        // update or add the current letter to the letters map
        letters.set(letter, right_pointer);
    }

    return max_string_length
};

let s = "pwwkew";
let sol = lengthOfLongestSubstring(s);
console.log(sol);