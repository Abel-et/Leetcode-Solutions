class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        container = list(zip(names,heights))
        container.sort(key=lambda x :-x[1])
        return [name[0] for name in container]
        