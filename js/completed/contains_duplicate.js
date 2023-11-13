/*
Problem 217

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
*/

var containsDuplicate = function(nums) {
    const seen = [];

    for (let n of nums) {
        if (seen.includes(n)){
            return true;
        }
        else {
            seen.push(n)
        }
    }
    return false;
};

var containsDuplicate2 = function(nums) {
    // create a set from nums, no duplicates
    seen = new Set(nums)

    return seen.size !== nums.length;
}