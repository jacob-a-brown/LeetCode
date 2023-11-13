/*
Problem 28

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
*/

/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    let num_needle_chars = needle.length;
    let num_hay_chars = haystack.length;

    for (let i = 0; i < num_hay_chars - num_needle_chars + 1; i++) {
        let check_str = haystack.slice(i, i + num_needle_chars);
        if (check_str == needle){
            return i;
        }
    }
    return -1;
};

var test_str = "sadnotsad";
var answer_str = strStr(test_str, "sad");
console.log(answer_str);