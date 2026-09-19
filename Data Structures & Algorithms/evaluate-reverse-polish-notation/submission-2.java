class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> operationValues = new Stack<Integer>();
        for (int i = 0; i < tokens.length; i ++) {
            if (tokens[i].equals("+")) {
                operationValues.push(operationValues.pop() + operationValues.pop());
            } else if (tokens[i].equals("-")) {
                int newVal = operationValues.pop();
                int oldVal = operationValues.pop();

                operationValues.push(oldVal - newVal);
            } else if (tokens[i].equals("*")) {
                operationValues.push(operationValues.pop() * operationValues.pop());
            } else if (tokens[i].equals("/")) {
                int newVal = operationValues.pop();
                int oldVal = operationValues.pop();

                operationValues.push(oldVal / newVal);
            } else {
                operationValues.push(Integer.parseInt(tokens[i]));
            }
        }

        return operationValues.pop();
    }
}
