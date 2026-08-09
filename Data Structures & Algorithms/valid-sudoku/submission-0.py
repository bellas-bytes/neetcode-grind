class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check each row
        for row in board:
            if not self.helper(row):
                return False

        # Check each column
        for i in range(9):
            col = []
            for j in range(9):
                col.append(board[j][i]) 
            if not self.helper(col):
                return False

        # Check each 3x3 box
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = []
                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        box.append(board[i][j])
                if not self.helper(box):
                    return False

        return True

    def helper(self, nums: List[str]) -> bool:
        num_set = set()
        for num in nums:
            if num != '.':  # Ignore empty cells
                if num in num_set:
                    return False
                num_set.add(num)
        return True