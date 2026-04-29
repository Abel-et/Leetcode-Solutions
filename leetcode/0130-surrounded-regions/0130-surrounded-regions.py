from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        queue = deque()

        # 1. Find all border 'O's and add to queue
        for r in range(rows):
            for c in range(cols):
                # Check if cell is on the border
                if (r in [0, rows-1] or c in [0, cols-1]) and board[r][c] == 'O':
                    board[r][c] = 'T'
                    queue.append((r, c))

        # 2. BFS to mark all connected internal 'O's
       
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'O':
                    board[nr][nc] = 'T'
                    queue.append((nr, nc))

        # 3. Final pass: Flip 'O' to 'X' and 'T' to 'O'
    
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'
