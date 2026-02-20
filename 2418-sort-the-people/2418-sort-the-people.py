class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name[0] for name in sorted(list(zip(names,heights)),key=lambda x :-x[1])]
        