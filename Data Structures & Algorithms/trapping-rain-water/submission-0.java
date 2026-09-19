class Solution {
    public int trap(int[] height) {
        // int max = 0;
        int totalWater = 0;
        int startIndex = 0;
        int endIndex = height.length - 1;

        if (height == null || height.length == 0) {
            return 0;
        }

        int startMax = height[startIndex];
        int endMax = height[endIndex];

        while (startIndex < endIndex) {
            if (startMax < endMax) {
                startIndex++;
                // This is to get rid of negatives
                startMax = Math.max(startMax, height[startIndex]);
                totalWater = totalWater + startMax - height[startIndex];
            } else {
                endIndex--;
                // Getting rid of negatives and updating max before calc
                endMax = Math.max(endMax, height[endIndex]);
                totalWater = totalWater + endMax - height[endIndex];
            }
        }
        return totalWater;
    }
}
