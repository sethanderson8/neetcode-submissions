class Solution {
    public int longestConsecutive(int[] nums) {
        // Could sort the array but that would lead to O(Log(n)) time so cant do that

        // Could use a HashSet and put all the nums in there, we then go through each num and check if there is num + 1
        // in there and track the current max from that

        Set<Integer> numSet = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            numSet.add(nums[i]);
        }

        int overallMax = 0;
        for (int i = 0; i < nums.length; i++) {
            int curMax = 0;
            int curNum = nums[i];
            if (!numSet.contains(curNum - 1)) {
                while (numSet.contains(curNum)) {
                    curMax++;
                    curNum++;
                }
            }

            overallMax = Math.max(curMax, overallMax);
        }

        return overallMax;
    }
}
