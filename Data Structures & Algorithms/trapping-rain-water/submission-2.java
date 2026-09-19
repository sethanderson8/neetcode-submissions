class Solution {
    public int trap(int[] height) {
        if (height == null || height.length <= 1) {
            return 0;
        }

        int left = 0;
        int right = height.length - 1;

        int leftMax = height[left];
        int rightMax = height[right];

        int totalWater = 0;

        while (left < right) {
            if (leftMax < rightMax) {
                left++;
                // If we calc max before calculation, we do not need to worry about adding negatives
                // Since we know that if height was taller, it would be the new max so would add 0
                leftMax = Math.max(leftMax, height[left]);
                int waterToAdd = leftMax - height[left];
                totalWater += waterToAdd;
            } else {
                right--;
                rightMax = Math.max(rightMax, height[right]);
                int waterToAdd = rightMax - height[right];
                totalWater += waterToAdd;
            }
        }

        return totalWater;
    }
}
