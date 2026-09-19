class Solution {
    public boolean checkInclusion(String s1, String s2) {
        // Tracking total chars in s1
        HashMap<Character, Integer> s1CharCount = new HashMap<>();

        // Get the total count of chars in s1 first
        for (int i = 0; i < s1.length(); i++) {
            s1CharCount.put(s1.charAt(i), 
                s1CharCount.getOrDefault(s1.charAt(i), 0) + 1);
        }

        int left = 0;
        HashMap<Character, Integer> s2CharCount = new HashMap<>();
        for (int right = 0; right < s2.length(); right++) {
            s2CharCount.put(s2.charAt(right), 
                s2CharCount.getOrDefault(s2.charAt(right), 0) + 1);
            if (!s1CharCount.containsKey(s2.charAt(right))) {
                left = right + 1;
                s2CharCount = new HashMap<>();
            } else if (s2CharCount.get(s2.charAt(right)) > s1CharCount.get(s2.charAt(right))) {
                while (s2CharCount.get(s2.charAt(right)) > s1CharCount.get(s2.charAt(right))) {
                    s2CharCount.put(s2.charAt(left), 
                        s2CharCount.get(s2.charAt(left)) - 1);
                    left++;
                }
            } else if (right - left + 1 == s1.length()){
                return true;
            }
        }

        return false;
    }
}
