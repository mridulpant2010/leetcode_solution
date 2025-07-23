class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix); n = len(matrix[0]); output=[]
        top=0;bottom=m-1;left=0;right=n-1
        while left<=right and top<=bottom:
            i = left
            while i<=right:
                output.append(matrix[top][i])
                i+=1
            top+=1

            j=top
            while j<=bottom:
                output.append(matrix[j][right])
                j+=1
            right-=1

            if top<=bottom:
                i = right
                while i>=left:
                    output.append(matrix[bottom][i])
                    i-=1
                bottom-=1

            if left<=right:
                j = bottom
                while j>=top:
                    output.append(matrix[j][left])
                    j-=1
                left+=1
        return output

        