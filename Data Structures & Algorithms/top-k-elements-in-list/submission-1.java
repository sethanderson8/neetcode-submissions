class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> numCount = new HashMap<Integer, Integer>();
        int[] ans = new int[k];
        // Go through this and count frequency of each of the numbers

        for (int i = 0; i < nums.length; i++) {
            numCount.put(nums[i], numCount.getOrDefault(nums[i], 0) + 1);
        }

        // Then build an Array of lists that we will put the values from the HashMap
        // based on their index

        List<Integer>[] countList = new ArrayList[nums.length + 1];

        for (int key : numCount.keySet()) {
            if (countList[numCount.get(key)] == null) {
                countList[numCount.get(key)] = new ArrayList<Integer>();
            }
            countList[numCount.get(key)].add(key);
        }
        
        // Then finally go through the array of lists and get the k top elements and return
        // the ans

        int counter = 0;

        for (int i = countList.length - 1; i >= 0 && counter < k; i--) {
            if (countList[i] != null) {
                for (int num : countList[i]) {
                    ans[counter] = num;
                    counter++;
                }
            }
        }

        return ans;
    }
}
