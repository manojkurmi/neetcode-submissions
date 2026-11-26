class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top<bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1
            if not (left < right and top < bottom):
                break
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1
        
        return res

        # if not matrix or not matrix[0]:
        #     return res

        # top_x, top_y = 0, 0
        # bot_x, bot_y = len(matrix)-1, len(matrix[0])-1

        # while top_x <= bot_y and top_y <= bot_y:
        #     if(top_x == bot_x):
        #         for y in range(top_y, bot_y+1):
        #             res.append(matrix[top_x][y])
        #         return res
        #     if top_y == bot_y:
        #         for x in range(top_x, bot_x+1):
        #             res.append(matrix[x][top_y])
        #         return res
            
        #     for y in range(top_y, bot_y):
        #         res.append(matrix[top_x][y])
        #     for x in range(top_x, bot_x):
        #         res.append(matrix[x][bot_y])
        #     for y in range(bot_y, top_y, -1):
        #         res.append(matrix[bot_x][y])
        #     for x in range(top_x, bot_x, -1):
        #         res.append(matrix[x][top_y])
        #     top_x += 1
        #     top_y += 1
        #     bot_x -= 1
        #     bot_y -= 1
        
        # return res
                        
