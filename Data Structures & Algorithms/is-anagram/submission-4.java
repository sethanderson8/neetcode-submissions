class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        Map<Character, Integer> charMap = new HashMap<>();
        Map<Character, Integer> charMap2 = new HashMap<>();

        for (int i = 0; i <= s.length() - 1; i++) {
            charMap.put(s.charAt(i), charMap.getOrDefault(s.charAt(i), 0) + 1);
            charMap2.put(t.charAt(i), charMap2.getOrDefault(t.charAt(i), 0) + 1);
        }

        for (int i = 0; i <= t.length() - 1; i++) {
            if (charMap.get(t.charAt(i)) != charMap2.get(t.charAt(i))) {
                return false;
            }
        }
        return true;
    }
}
