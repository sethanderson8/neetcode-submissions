class Solution {
    public int characterReplacement(String s, int k) {

        // Counting the occurences of each char
        Map<Character, Integer> charCount = new HashMap<>();

        // Find the length of the window - most frequent char = 
            // number of chars that will get replaced

        int left = 0;
        int right = 0;
        Character mostUsedChar = s.charAt(0);
        int mostUsedCharCount = 1;
        int curSubstring = 0;
        int maxSubstring = 0;

        while (right < s.length()) {
            charCount.put(s.charAt(right), 
                charCount.getOrDefault(s.charAt(right), 0) + 1);
            curSubstring++;
            if (charCount.get(s.charAt(right)) > mostUsedCharCount) {
                mostUsedChar = s.charAt(right);
                mostUsedCharCount = charCount.get(s.charAt(right));
            }
            // for (Character key : charCount.keySet()) {
            //     if (charCount.get(key) > charCount.get(mostUsedChar)) {
            //         mostUsedChar = key;
            //     }
            // }

            // Repeat this until out sliding window is valid
            while (curSubstring - charCount.get(mostUsedChar) > k) {
                charCount.put(s.charAt(left), 
                    charCount.get(s.charAt(left)) - 1);
                curSubstring--;
                if (s.charAt(left) == mostUsedChar) {
                    mostUsedCharCount--;
                }
                if (charCount.get(s.charAt(right)) >= mostUsedCharCount) {
                    mostUsedChar = s.charAt(right);
                    mostUsedCharCount = charCount.get(s.charAt(right));
                }
                left++;

                // for (Character key : charCount.keySet()) {
                //     if (charCount.get(key) > charCount.get(mostUsedChar)) {
                //         mostUsedChar = key;
                //     }
                // }
            }

            // Once sliding window is valid, check to see if we have new max
            maxSubstring = Math.max(maxSubstring, curSubstring);
            right++;
        }
        return maxSubstring;
    }
}
