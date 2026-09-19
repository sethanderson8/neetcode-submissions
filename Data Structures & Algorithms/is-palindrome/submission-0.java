class Solution {
    public boolean isPalindrome(String s) {
        // Iterate over the string using two pointers
        // One at the end, one at the beginning

        // We then check if it is a space or non-alphanumeric characters
        // if it is, then we iterate -- or ++

        // If at any point, s.chartAt(EndPointer) != s.charAt(StartPointer) 
        // AND it is not alphanumeric, return false

        // Once EndPointer - StartPointer = 1 and are equal return true, 
        // OR Once EndPointer - StartPointer = 0 and are equal return true
        int startPointer = 0;
        int endPointer = s.length() - 1;

        while (startPointer <= endPointer) {
            if (!Character.isLetterOrDigit(s.charAt(startPointer)) &&
                !Character.isLetterOrDigit(s.charAt(endPointer))) {
                startPointer++;
                endPointer--;
            } else if (!Character.isLetterOrDigit(s.charAt(startPointer))) {
                startPointer++;
            } else if (!Character.isLetterOrDigit(s.charAt(endPointer))) {
                endPointer--;
            } else {
                if (Character.toLowerCase(s.charAt(startPointer)) !=
                    Character.toLowerCase(s.charAt(endPointer))) {
                        return false;
                    } else {
                        startPointer++;
                        endPointer--;
                    }
            }
        }
        // Default will be true
        return true;
    }
}
