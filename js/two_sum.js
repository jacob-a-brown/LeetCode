/**
 * Problem 1
 * 
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var summation = 0;
    var starting_index = 0;
    var sum_not_found = true;

    while (sum_not_found) {
        for (var i = starting_index + 1; i < nums.length; i++) {
            var summation = nums[starting_index] + nums[i];
            console.log(starting_index, i);
            if (summation === target){
                var sum_not_found = false;
                console.log(sum_not_found);
                break
            }
        }
        if (sum_not_found) {
                starting_index++;
        }
    }
    if (!sum_not_found){
        var indices = [starting_index, i];
        return indices;
    }
};

var twoSum2 = function(nums, target) {
    var sum_map = new Map();

    for (let i = 0; i < nums.length; i++) {
        if (sum_map.has(nums[i])) {
            let result = [sum_map.get(nums[i]), i];
            return result;
        } else {
            sum_map.set(target-nums[i], i);
        }
    }
}

let nums = [3, 2, 3];
let target = 6;
let result = twoSum(nums, target);
console.log(result);