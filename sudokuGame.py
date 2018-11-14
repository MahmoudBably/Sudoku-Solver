class SudokuGame:

    def __init__(self, sudokuBoard):
        for row in range(9):
            for col in range(9):
                sudokuBoard[row][col] = int(sudokuBoard[row][col])
        self.__sudokuBoard = sudokuBoard
        self.__solution = []

    def getSolution(self):
        return self.__solution

    def setSolution(self, solution):
        self.__solution = solution

    def getNumber(self, row, col):
        return self.__sudokuBoard[row][col]

    def setNumber(self, row, col, number):
        self.__sudokuBoard[row][col] = number

    def checkNumberValidity(self, row, col, number):
        if self.getNumber(row, col) == number:
            return True
        if self.getNumber(row, col) != 0:
            return False
        for iterCL in range(9):
            if self.__sudokuBoard[row][iterCL] == number:
                return False
        for iterRW in range(9):
            if self.__sudokuBoard[iterRW][col] == number:
                return False
        threeBYthree_rowRange = int(row/3)
        threeBYthree_colRange = int(col/3)
        for r in range(threeBYthree_rowRange*3, (threeBYthree_rowRange+1)*3):
            for c in range(threeBYthree_colRange*3, (threeBYthree_colRange+1)*3):
                if self.__sudokuBoard[r][c] == number:
                    return False
        return True

    def writeSolution(self, solution):
        file = open("FinalSolution.txt", "w")
        try:
            for row in range(9):
                for col in range(9):
                    file.write(str(solution[row][col]))
                    file.write(" ")
                file.write("\n")
            file.close()
        except:
            print("ERROR!! FILE CAN'T BE SAVED")
        finally:
            file.close()

    def solveSudokuBoard(self, row, col):
        if row == 9:
            self.__solution = self.__sudokuBoard
            self.writeSolution(self.getSolution())
            return 0
        else:
            for number in range(1, 10):
                if self.checkNumberValidity(row, col, number):
                    backtrackTemp = self.getNumber(row,col)
                    self.setNumber(row, col, number)
                    if col == 8:
                        self.solveSudokuBoard(row+1, 0)
                    else:
                        self.solveSudokuBoard(row, col+1)
                    self.setNumber(row, col, backtrackTemp)
