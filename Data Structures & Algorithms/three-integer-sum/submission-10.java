class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        

        List<List<Integer>> ans = new ArrayList<>();
        // Sort the array
        // Then go through each int in nums
            // startPointer = i + 1, endPointer = nums.length - 1
            // Iterate over the start and endPointer to see if those ints
            // at those indicies + nums[i] is 0 and if so, add that to the ans
        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++) {
            int startPointer = i + 1;
            int endPointer = nums.length - 1;
            if (nums[i] <= 0) {
                // Removing duplicates
                if (!(i >  0 && nums[i] == nums[i - 1])) {
                    while (startPointer < endPointer) {
                        if (nums[i] + nums[startPointer] + nums[endPointer] == 0) {
                            List<Integer> tripleSumList = new ArrayList<>();
                            tripleSumList.add(nums[i]);
                            tripleSumList.add(nums[startPointer]);
                            tripleSumList.add(nums[endPointer]);
                            ans.add(tripleSumList);
                            endPointer--;
                            startPointer++;
                            // Remove duplicates here
                            while (startPointer < endPointer && nums[endPointer] == nums[endPointer + 1]) {
                                endPointer--;
                            }
                        } else if (nums[i] + nums[startPointer] + nums[endPointer] < 0) {
                            startPointer++;
                        } else {
                            endPointer--;
                        }
                    }
                }
            }
        }
        return ans;
    }
}
