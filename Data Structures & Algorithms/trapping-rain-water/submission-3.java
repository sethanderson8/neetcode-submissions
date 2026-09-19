class Solution {
    public int trap(int[] height) {
        int left = 0;
        int right = height.length - 1;

        // Formula is Min(leftMax, rightMax) - height[i] = amount of water stored, if not negative
        int leftMax = height[left];
        int rightMax = height[right];

        int totalWater = 0;

        while (left < right) {
            if (leftMax < rightMax) {
                left++;
                leftMax = Math.max(height[left], leftMax);
                totalWater += leftMax - height[left];
            } else {
                right--;
                rightMax = Math.max(height[right], rightMax);
                totalWater += rightMax - height[right];
            }
        }
        
        return totalWater;
    }
}
