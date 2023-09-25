class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = 0
        for candy in candies:
            if candy > greatest:
                greatest = candy

        boolean_array = []
        for candy in candies:
            if (candy + extraCandies) >= greatest:
                boolean_array.append(True)
            else:
                boolean_array.append(False)
        return boolean_array

        