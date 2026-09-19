class Solution {
    public String minWindow(String s, String t) {
        String ans = "";
        Map<Character, Integer> subStringCharCount = new HashMap<>();

        for (int i = 0; i < t.length(); i ++ ) {
            subStringCharCount.put(t.charAt(i), 
                subStringCharCount.getOrDefault(t.charAt(i), 0) + 1);
        }

        // Success = matches == keySet().size()
        int matches = 0;

        int left = 0;
        Map<Character, Integer> mainStringCharCount = new HashMap<>();

        for (int right = 0; right < s.length(); right++) {
            char rightChar = s.charAt(right);
            if (subStringCharCount.containsKey(rightChar)) {
                subStringCharCount.put(rightChar, subStringCharCount.get(rightChar) - 1);
                if (subStringCharCount.get(rightChar) == 0) {
                    matches++;
                }
            }

            while (matches == subStringCharCount.size()) {
                if (ans.equals("")) {
                    ans = s.substring(left, right + 1);
                } else if (ans.length() > right - left + 1) {
                    ans = s.substring(left, right + 1);
                }
                char deleted = s.charAt(left);
                if (subStringCharCount.containsKey(deleted)) {
                    subStringCharCount.put(deleted, subStringCharCount.get(deleted) + 1);
                    if (subStringCharCount.get(deleted) == 1) {
                        matches--;
                    }
                }
                left++;
            }
        }

        return ans;
    }
}
