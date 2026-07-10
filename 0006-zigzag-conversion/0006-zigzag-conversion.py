class Solution(object):
    def convert(self, s, numRows):
        
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curRow = 0
        down = False

        for char in s:
            rows[curRow] += char

            if curRow == 0 or curRow == numRows - 1:
                down = not down

            curRow += 1 if down else -1

        return "".join(rows)