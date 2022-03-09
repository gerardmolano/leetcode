/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    complements = new Map()

    for (let i = 0; i < nums.length; i++) {
        complement = target - nums[i];
        
        if (complements.has(complement)) {
            return [ complements.get(complement), i ];
        } // if

        complements.set(nums[i], i);
    } // for
};

// test here
console.log(twoSum([3, 2, 4], 6));
