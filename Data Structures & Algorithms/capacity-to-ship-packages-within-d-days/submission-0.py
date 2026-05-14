class Solution:
    def canShip(self,weights,capacity,days):
        days_count=1
        current_load=0
        for w in weights:
            if current_load+w>capacity:
                days_count+=1
                current_load=w
            else:
                current_load+=w
        return days_count<=days
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        ans=right
        while(left<=right):
            mid=(left+right)//2
            if self.canShip(weights,mid,days):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans