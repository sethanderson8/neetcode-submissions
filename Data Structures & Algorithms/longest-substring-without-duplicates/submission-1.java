class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) {
            return 0;
        } else if (s.length() == 1) {
            return 1;
        }

        Set<Character> uniqueChars = new HashSet<Character>();
        int left = 0;
        int maxSubstring = 0;

        for (int right = 0; right < s.length(); right++) {
            while (uniqueChars.contains(s.charAt(right))) {
                // Removing the left char if it is seen
                uniqueChars.remove(s.charAt(left));
                left++;
            }
            // Need to make sure we add the right char each time
            uniqueChars.add(s.charAt(right));
            maxSubstring = Math.max(maxSubstring, right - left + 1);
        }

        return maxSubstring;
    }
}

// pwwkew
// left = 1
// right = 3
// maxSubstring = 2
