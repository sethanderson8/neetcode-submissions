class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int[] ans = new int[nums.length - k + 1];

        Deque<Integer> numsDeque = new ArrayDeque<>();

        int left = 0;
        for (int right = 0; right < nums.length; right++) {
            if (numsDeque.peekFirst() == null) {
                numsDeque.addLast(nums[right]);
            } else {
                while (numsDeque.peekLast() != null && 
                    numsDeque.peekLast() < nums[right]) {
                    numsDeque.pollLast();
                }
                numsDeque.offer(nums[right]);
            }

            if (right >= k - 1) {
                ans[left] = numsDeque.peekFirst();
                if (numsDeque.peekFirst() == nums[left]) {
                    numsDeque.pollFirst();
                }
                left++;
            }
        }

        return ans;
    }
}
