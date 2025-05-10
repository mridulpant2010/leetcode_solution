#https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
class Solution:
    def __init__(self):
        self.n=3
        self.rows=[0]*self.n
        self.columns=[0]*self.n
        self.diag=0
        self.antidiag=0
        self.player=None
    def move(self,row,col,player):
        add_value=1 if player=="A" else -1
        self.rows[row]+=add_value
        self.columns[col]+=add_value
        if row==col:
            self.diag+=add_value
        if row+col == self.n-1:
            self.antidiag+=add_value
        
        if abs(self.rows[row])==self.n or abs(self.columns[col])==self.n or abs(self.diag)==self.n or abs(self.antidiag)==self.n:
            
            self.player=player
        return self.player

    def tictactoe(self, moves: List[List[int]]) -> str:
        for idx, each_move in enumerate(moves):
            player='A' if idx%2==0  else 'B'
            self.move(each_move[0],each_move[1],player)
            if self.player:
                return self.player
        return "Draw" if len(moves) == self.n * self.n else "Pending" 
