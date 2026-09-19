class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        // Success: the minumum bananas/hour needed to eat all bananas
        // within the number of hours (h)

        // Could start with the max piles[i] and do binary search from ther
        // to figure out the best ban/hour rate

        int banPerHour = 0;
        for (int i = 0; i < piles.length; i++) {
            banPerHour = Math.max(banPerHour, piles[i]);
        }
        return bestBanPerHourRate(piles, h, banPerHour);
    }

    public int eat(int[] piles, int banPerHour) {
        int totalHoursToEat = 0;
        for (int i = 0; i < piles.length; i++) {
            int bans = piles[i];
            totalHoursToEat += (int) Math.ceil((double) bans/ banPerHour);
        }
        return totalHoursToEat;
    }

    public int bestBanPerHourRate(int[] piles, int h, int banPerHour) {
        int min = 1;
        int max = banPerHour;

        while (min < max) {
            int mid = min + (max - min) / 2;

            int hoursToEat = eat(piles, mid);

            if (hoursToEat <= h) {
                max = mid;
            } else {
                min = mid + 1;
            }
        }
        return min;
    }
}
