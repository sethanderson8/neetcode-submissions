class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, Integer> numsMap = new HashMap<>();
        for (int i = 0; i <= nums.length - 1; i++) {
            if (numsMap.get(nums[i]) == null) {
                numsMap.put(nums[i], 1);
            } else {
                return true;
            }
        }
        return false;
    }
}
