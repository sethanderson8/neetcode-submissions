class Solution {
    public int maxArea(int[] heights) {
        int max = 0;
        int startPointer = 0;
        int endPointer = heights.length - 1;

        while (startPointer < endPointer) {
            int area = (endPointer - startPointer) * 
                Math.min(heights[startPointer], heights[endPointer]);
            max = Math.max(max, area);
            if (heights[startPointer] < heights[endPointer]) {
                startPointer++;
            } else if (heights[startPointer] > heights[endPointer]) {
                endPointer--;
            } else {
                startPointer++;
            }
        }

        return max;
    }
}
