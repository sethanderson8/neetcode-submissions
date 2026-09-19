class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ans = new ArrayList<>();

        generateParens(n, 0, 0, "", ans);

        return ans;
    }

    public void generateParens(int n, int open, int closed, String parens, List<String> ans) {
        if (open == n && closed == n) {
            ans.add(parens);
        }
        
        if (open < n) {
            parens += "(";
            generateParens(n, open + 1, closed, parens, ans);
            parens = parens.substring(0, parens.length() - 1);
        }
        
        if (closed < open) {
            parens += ")";
            generateParens(n, open, closed + 1, parens, ans);
            parens = parens.substring(0, parens.length() - 1);
        }
    }
}
