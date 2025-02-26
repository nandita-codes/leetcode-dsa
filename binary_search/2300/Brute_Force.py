class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        success_count = []
        for i in range(len(spells)):
            count = 0
            for j in range(len(potions)):
                if spells[i]*potions[j]>=success:
                    count+=1
            success_count.append(count)
        return success_count
