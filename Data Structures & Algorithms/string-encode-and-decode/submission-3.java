class Solution {

    public String encode(List<String> strs) {
        String encodedList ="[";
        if (strs.size() >= 1) {
            encodedList = encodedList + "\"" + strs.get(0); 
            for (int i = 1; i < strs.size(); i++) {
                 encodedList = encodedList + "\",\"" + strs.get(i);
            }
            return encodedList + "\"]";
        }
        return encodedList + "]";
    }
    // ["neet","code","love","you"]

    public List<String> decode(String str) {
        if (str.equals(null) || str.equals("") || str.equals("[]")) {
            return new ArrayList<String>();
        }
        List<String> csvList = Arrays.asList(str.split("\",\""));
        if (csvList.size() == 1) {
            csvList.set(0, csvList.get(0).substring(2, csvList.get(0).length() - 2)); 
        } else if (csvList.size() > 1) {
            csvList.set(0, csvList.get(0).substring(2, csvList.get(0).length()));
            csvList.set(csvList.size() - 1, 
                csvList.get(csvList.size() - 1)
                    .substring(0, csvList.get(csvList.size() - 1).length() - 2)); 
        }
        return csvList;
    }
}
