class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(len(board)):
            for col in range(len(board[row])):
                number = board[row][col]
                if number == ".":
                    continue
                box = 0
                if row < 3:
                    box = col // 3
                elif row < 6:
                    box = col // 3 + 3
                else:
                    box = col // 3 + 6
                if number in rows[row] or number in cols[col] or number in boxes[box]:
                    return False
                else:
                    rows[row].add(number)
                    cols[col].add(number)
                    boxes[box].add(number)

        return True
