class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output=[];
        highest=max(candies);
        for i in range(len(candies)):
            if candies[i] + extraCandies >= highest:
                output.append(True);
            else:
                output.append(False);
        return output;