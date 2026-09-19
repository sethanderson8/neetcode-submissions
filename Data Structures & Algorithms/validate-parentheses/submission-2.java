class Solution {
    public boolean isValid(String s) {
        Stack<Character> charOpenStack = new Stack<>();
        // Queue<Character> charClosedStack = new LinkedList<>();
        // boolean isValid = false;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(' || s.charAt(i) == '[' ||
                s.charAt(i) == '{') {
                charOpenStack.push(s.charAt(i));
            } else {
                if (charOpenStack.empty()) {
                    return false;
                } else if (s.charAt(i) == ')' && charOpenStack.pop() != '(') {
                    return false;
                } else if (s.charAt(i) == ']' && charOpenStack.pop() != '[') {
                    return false;
                } else if (s.charAt(i) == '}' && charOpenStack.pop() != '{') {
                    return false;
                }
            }
        }

        return charOpenStack.empty();
    }
}
