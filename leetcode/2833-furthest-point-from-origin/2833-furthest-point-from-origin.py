class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        n = len(moves)
        left = moves.count('L')
        right = moves.count('R')
        none = moves.count('_')

        if left > right:
            return left + none - right
        return right + none - left