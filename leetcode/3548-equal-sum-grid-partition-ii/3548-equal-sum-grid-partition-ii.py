from collections import Counter

class Solution:
    def canPartitionGrid(self, grid):
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)

        # ---------- Horizontal ----------
        bottom = Counter()
        for row in grid:
            bottom.update(row)

        top = Counter()
        top_sum = 0

        for i in range(m - 1):
            row = grid[i]
            for v in row:
                top[v] += 1
                bottom[v] -= 1
                if bottom[v] == 0:
                    del bottom[v]

            top_sum += sum(row)
            bottom_sum = total - top_sum

            if top_sum == bottom_sum:
                return True

            diff = abs(top_sum - bottom_sum)

            # TOP bigger
            if top_sum > bottom_sum:
                if self.valid_remove(top, grid, 0, i, 0, n-1, diff):
                    return True
            else:
                if self.valid_remove(bottom, grid, i+1, m-1, 0, n-1, diff):
                    return True

        # ---------- Vertical ----------
        right = Counter()
        for j in range(n):
            for i in range(m):
                right[grid[i][j]] += 1

        left = Counter()
        left_sum = 0

        for j in range(n - 1):
            for i in range(m):
                v = grid[i][j]
                left[v] += 1
                right[v] -= 1
                if right[v] == 0:
                    del right[v]
                left_sum += v

            right_sum = total - left_sum

            if left_sum == right_sum:
                return True

            diff = abs(left_sum - right_sum)

            if left_sum > right_sum:
                if self.valid_remove(left, grid, 0, m-1, 0, j, diff):
                    return True
            else:
                if self.valid_remove(right, grid, 0, m-1, j+1, n-1, diff):
                    return True

        return False

    # ---------- O(1) removal check ----------
    def valid_remove(self, counter, grid, r1, r2, c1, c2, diff):
        if diff not in counter:
            return False

        rows = r2 - r1 + 1
        cols = c2 - c1 + 1

        # 2D block → always valid
        if rows > 1 and cols > 1:
            return True

        # 1D row
        if rows == 1:
            return grid[r1][c1] == diff or grid[r1][c2] == diff

        # 1D column
        if cols == 1:
            return grid[r1][c1] == diff or grid[r2][c1] == diff

        return False