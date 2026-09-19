class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int verticalMid = searchRecursiveVertical(matrix, target, 0, matrix.length, 0);
        return searchRecursiveHorizontal(matrix[verticalMid], target, 0, matrix[verticalMid].length);
    }

    public int searchRecursiveVertical(int[][] matrix, int target, int bottom, int top, int minIndex) {
        int mid = bottom + (top - bottom) / 2;

        if (bottom > top || mid >= matrix.length) {
            return minIndex; // Defaulting to 0 if no other good solution is found
        }

        // If it is less than target, then we keep searching upwards to see if there is one closer
        if (matrix[mid][0] <= target) {
            if (target - matrix[mid][0] < target - matrix[minIndex][0]) {
                minIndex = mid;
            }
            return searchRecursiveVertical(matrix, target, mid + 1, top, minIndex);
        } else {
            return searchRecursiveVertical(matrix, target, bottom, mid - 1, minIndex);
        }
    }

    public Boolean searchRecursiveHorizontal(int[] nums, int target, int left, int right) {
        int mid = left + (right - left) / 2;
        if (left > right || mid >= nums.length) {
            return false;
        }

        if (target == nums[mid]) {
            return true;
        } else if (nums[mid] > target) {
            return searchRecursiveHorizontal(nums, target, left, mid - 1);
        } else {
            return searchRecursiveHorizontal(nums, target, mid + 1, right);
        }
    }
}
