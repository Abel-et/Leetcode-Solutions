class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
            col , posdiagonal, negative diagonal are tool which tells us on which way the queen can go and indicate us to put the next 
            queen on next row they help ups telling the current row is taken or not 

                 why we use these variables
                    col => tells the taken column because the queen can move vertically and can attack
                    posetive Diagonal => tells from top to right diagonal which the queen is waiting to attack or not
                    negative Diagonal => tells from top to left or bottom to left diagonal which the queens have control on 
                    board = > it show on which the queen is sitted 
                    result => is holds orgainzied board elements

                what approach we use is :
                    backtracking which is check every row and every positions and
                        put the queen on safe places then countinue 
                        if he reach last row with valid spots (which i means the base case)
                            it will return and append the answer on result arr
                        if all options are not vaild it will back to one places from the upper 
                            and check the another option 
                                if it get :
                                    it will continue down ward 
                            else 
                                go back form the very begining and change the start option
                    ******************this so intersting thing i had ever see in algorithm***********


        """ 
        # tools which help to track the valid options
        cols ,posetivDiagonal, negativeDiagonal = [False]*(n), [False]*(2*n-1), [False]*(2*n-1)

        # a board used to put the queen 
        board = [['.']*n for _ in range(n)]

        # a container which returned finally when the backtrack def finish its work
        result = []
        

        def backtrack(row):
            # base case
            if row == n:
                result.append([''.join(r) for r in board])

            # iterating every nodes and checking the valid spot to put the queen and backtracking which remove invalid sitted queen
            for col in range(n):

                # tracking the value of the current row postions 
                posetiveDiagonalIndex = row - col
                negativeDiagonalIndex = row + col
               
            #    checking if one of the indicator is true continue which mean we can't put our queen here
                if cols[col] or posetivDiagonal[posetiveDiagonalIndex] or negativeDiagonal[negativeDiagonalIndex]:
                    continue
                
                # or we get a valid spot putting our queen on this place
                cols[col] = posetivDiagonal[posetiveDiagonalIndex] = negativeDiagonal[negativeDiagonalIndex] = True
                board[row][col] = 'Q'
                backtrack(row + 1)

                # backtracking after checking all posible ways then i back and update my way
                cols[col] = posetivDiagonal[posetiveDiagonalIndex] = negativeDiagonal[negativeDiagonalIndex] = False
                board[row][col] = '.'
        backtrack(0)
        return result
            


            

