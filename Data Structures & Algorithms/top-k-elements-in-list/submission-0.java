class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] ans = new int[k];
        Map<Integer, Integer> countMap = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++) {
            countMap.put(nums[i], countMap.getOrDefault(nums[i], 0) + 1);
        }

        // We create this so we can put the numbers in the index which indicates frequency of that number
        List<Integer>[] freq = new ArrayList[nums.length + 1];

        // Initialize all the lists in the array
        for (int i = 0; i < freq.length; i++) {
            freq[i] = new ArrayList<>();
        }

        for (Integer key : countMap.keySet()) {
            freq[countMap.get(key)].add(key);
        }

        int ansIndexCounter = ans.length - 1;
        for (int i = freq.length - 1; i >= 0 || ansIndexCounter >= 0; i--) {
            if (!freq[i].isEmpty()) {
                for (Integer num : freq[i]) {
                    if (ansIndexCounter >= 0) {
                        ans[ansIndexCounter] = num;
                        ansIndexCounter--;
                    }
                }
            }
        }
        
        return ans;
    }
}
