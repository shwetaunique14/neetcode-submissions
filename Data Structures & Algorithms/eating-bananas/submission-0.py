class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        result=high
        while low<=high:
            k=(low+high)//2
            hours_spent=0
            for pile in piles:
                hours_spent+=math.ceil(pile/k)
            if hours_spent<=h:
                result=k
                high=k-1
            else:
                low=k+1
        return result
        