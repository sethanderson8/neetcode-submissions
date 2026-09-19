class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> tempIndexes = new Stack<>();
        int[] result = new int[temperatures.length];

        for (int i = 0; i < temperatures.length; i++) {
            int temp = temperatures[i];
            // While the stack is not empty and while the temp is greater than 
            // the temp of the top most index in the stack
            while(!tempIndexes.isEmpty() && temp > temperatures[tempIndexes.peek()]) {
                int index = tempIndexes.pop();
                result[index] = i - index;
            }
            tempIndexes.push(i);
        }
        
        return result;
    }
}

// 30,38,30,36,35,40,28

// 30, 38, 30, 36

// Stack: 1,2
