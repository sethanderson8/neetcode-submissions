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
                int waterToAdd = leftMax - height[left];
                if (waterToAdd > 0) {
                    totalWater += waterToAdd;
                }
                leftMax = Math.max(leftMax, height[left]);
            } else {
                right--;
                int waterToAdd = rightMax - height[right];
                if (waterToAdd > 0) {
                    totalWater += waterToAdd;
                }
                rightMax = Math.max(rightMax, height[right]);
            }
        }

        return totalWater;
    }
}
