from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand, groupSize: int) -> bool:
        d = defaultdict(int)
        for el in hand:
            d[el]+=1
        hand.sort()
        el =0
        while el < len(hand):
            if d[hand[el]]==0:
                el+=1
                continue
            for i in range(hand[el],hand[el]+groupSize):
                if d[i]==0:
                    return False
                d[i]-=1
        return True
        
if __name__=="__main__":
    s = Solution()
    hand = [1,2,3,6,2,3,4,7,8] ; groupSize = 3
    ans = s.isNStraightHand(hand,groupSize)
    print(ans)