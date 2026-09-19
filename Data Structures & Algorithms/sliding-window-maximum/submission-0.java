class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int[] ans = new int[nums.length - k + 1];

        PriorityQueue<Integer> maxQueue = new PriorityQueue<>(Collections.reverseOrder());

        
        for (int i = 0; i < nums.length; i++) {
            maxQueue.add(nums[i]);
            if (maxQueue.size() == k) {
                ans[i - k + 1] = maxQueue.peek();
                maxQueue.remove(nums[i - k + 1]);
            }
        }

        return ans;

        // BRUTE FORCE
        // For loop for ans.length
        // Each loop we check the k next elements starting from index we are on for ans
        // get max of each windwo and place in ans
    }
}
