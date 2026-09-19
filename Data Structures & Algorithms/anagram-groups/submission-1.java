class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> ans = new ArrayList<>();
        Map<String, List<String>> currentStringHashMap = 
            new HashMap<>();


        for (int i = 0; i <= strs.length - 1; i ++) {
            char[] arr = strs[i].toCharArray();
            
            //sort the letters
            Arrays.sort(arr);
            
            // create key and put into map
            if (currentStringHashMap.get(String.valueOf(arr)) == null) {
                currentStringHashMap.put(String.valueOf(arr), new ArrayList<>());
            }
            currentStringHashMap.get(String.valueOf(arr)).add(strs[i]);
        }

        return new ArrayList<>(currentStringHashMap.values());
    }
}
