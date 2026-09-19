class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 30,38,30,36,35,40,28

        tempIndexes = []
        tempIndexes.append(0)
        daysTilWarner = [0 for i in range(len(temperatures))]
        for i in range(1, len(temperatures)):
            print(tempIndexes)
            
            while tempIndexes and temperatures[i] > temperatures[tempIndexes[-1]]:
                colderDayIndex = tempIndexes.pop()
                daysTilWarner[colderDayIndex] = i - colderDayIndex

            tempIndexes.append(i)

        return daysTilWarner

