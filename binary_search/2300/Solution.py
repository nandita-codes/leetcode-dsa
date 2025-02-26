from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        num_potions = len(potions)
        #[num_potions - bisect_left(potions,success/spell_strength) for spell_strength in spells]
        return [num_potions - bisect_left(potions,success/spell) for spell in spells]
