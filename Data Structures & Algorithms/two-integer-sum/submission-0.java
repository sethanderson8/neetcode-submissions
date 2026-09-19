class Solution {
    public int[] twoSum(int[] nums, int target) {

        // This is storing by Key: compliment, Value: index
        Map<Integer, Integer> complimentMap = new HashMap<>();

        for (int i = 0; i < nums.length; i ++) {
            if (complimentMap.get(nums[i]) != null) {
                int complimentIndex = complimentMap.get(nums[i]);
                // Double check this
                return new int[]{Math.min(i, complimentIndex), Math.max(i, complimentIndex)};
            }
            complimentMap.put(target - nums[i], i);
        }

        return new int[]{};
    }
}
