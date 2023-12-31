/*
Problem 26

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
The remaining elements of nums are not important as well as the size of nums.
Return k.
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let seen = new Set();

    let array_length = nums.length;
    let array_index = 0;

    while (array_index < array_length) {
        if (!seen.has(nums[array_index])){
            seen.add(nums[array_index]);
            array_index ++; 
        }
        else{
            nums.splice(array_index, 1);
            array_length --;
        }
    }

    return nums.length;
};

var removeDuplicates2 = function(nums) {
    let left = 0;

    for (let right = 1; right < nums.length; right++) {
        if (nums[left] === nums[right]){
            // iterate right by 1
            // pass
        }
        else {
            nums[left+1] = nums[right];
            left++;
            console.log(nums)
        }
    }
    return left+1;
}

var nums = [0,0,1,1,1,2,2,3,3,4];
var new_nums = removeDuplicates2(nums);
//console.log(new_nums)

/*
l = 0
r = 3

0  1  2  3  4  5  6
1, 1, 1, 2, 3, 3, 4
l        r


l = 0
r = 2

0  1  2  3  4  5  6
1, 2, 1, 3, 3, 3, 4
l  r 

*/