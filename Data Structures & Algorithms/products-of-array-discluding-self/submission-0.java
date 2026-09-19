class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] ans = new int[nums.length];
        int pre = 1;
        int post = 1;

        for (int i = 0; i < nums.length; i ++) {
            ans[i] = pre;
            pre = pre * nums[i];
        }

        for (int i = nums.length -1; i > 0; i --) {
            post = post * nums[i];
            ans[i - 1] = post * ans[i - 1];
        }

        return ans;
    }
}  
