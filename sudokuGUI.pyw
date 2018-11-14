from sudokuGame import SudokuGame
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

class SudokuGUI(SudokuGame):

    def __init__(self, window):
        self.style = ttk.Style()
        self.style.theme_use('clam')

        #window.iconbitmap(r'C:\Users\medom\Desktop\Task\Sudoku Solver (Bably)\Alecive-Flatwoken-Apps-Sudoku.ico')
        window.resizable(False, False)
        window.title('Sudoku Game')

        top = ttk.Frame(window)

        self.gridFrame = ttk.Frame(top)
        self.__board = []
        for gridRows in range (1, 10):
            self.__board += [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
        for row in range(9):
            for col in range(9):
                if col in [3, 4, 5] and row in [0, 1, 2, 6, 7, 8]:
                    boardColor = 'lightgreen'
                    textColor = 'black'
                elif col not in [3, 4, 5] and row not in [0, 1, 2, 6, 7, 8]:
                    boardColor = 'lightgreen'
                    textColor = 'black'
                else:
                    boardColor = 'silver'
                    textColor = 'white'
                self.__board[row][col] = Entry(self.gridFrame, width=2, bg=boardColor, fg=textColor,
                                               font=('Arial', 22), justify='center',
                                               borderwidth=2,
                                               highlightcolor='grey', highlightthickness=1,
                                               textvar=GUIEntryBoard[row][col])
                self.__board[row][col].bind('<Motion>', self.checkInputValidity)
                self.__board[row][col].grid(row=row, column=col)
        self.gridFrame.pack(padx=5, pady=5)

        self.buttonFrame = ttk.Frame(top)
        self.solveButton = ttk.Button(self.buttonFrame, text='Solve', command=self.solveButtonFunction).grid(row=0, column=0, columnspan=2, padx=5, pady=10)
        self.saveButton = ttk.Button(self.buttonFrame, text='Save', command=self.saveButtonFunction).grid(row=0, column=2, columnspan=2, padx=5, pady=10)
        self.resetButton = ttk.Button(self.buttonFrame, text='Reset', command=self.resetButtonFunction).grid(row=0, column=4, columnspan=2, padx=5, pady=10)
        self.buttonFrame.pack()

        top.pack()

    def getBoard(self):
        board = []
        for rows in range(9):
            board += [[0, 0, 0, 0, 0, 0, 0, 0, 0]]
        for row in range(9):
            for col in range(9):
                board[row][col] = GUIEntryBoard[row][col].get()
                if board[row][col] == '':
                    board[row][col] = 0
        return board

    def checkInputValidity(self, event):
        for row in range(9):
            for col in range(9):
                if GUIEntryBoard[row][col] == '':
                    continue
                if len(GUIEntryBoard[row][col].get()) > 1 or GUIEntryBoard[row][col].get() not in ['1','2','3','4','5','6','7','8','9']:
                    GUIEntryBoard[row][col].set('')

    def solveButtonFunction(self):

        def getSolutionFromFile():
            self.__filename = "FinalSolution.txt"
            file = open(self.__filename, 'r')
            text = file.readline()
            text = text.split(' ')
            for row in range(9):
                for col in range(9):
                    if text[0] == '0':
                        GUIEntryBoard[row][col].set('')
                    else:
                        GUIEntryBoard[row][col].set(text[0])
                    text.pop(0)
                text = file.readline()
                text = text.split(' ')
            file.close()
        try:
            solution = SudokuGame(self.getBoard())
            solution.solveSudokuBoard(0, 0)
            getSolutionFromFile()
            os.remove('FinalSolution.txt')
        except:
            messagebox.showinfo(title='Warning', message='Wrong Number Entered!')

    def saveButtonFunction(self):
        file = open('SavedBoards.txt', 'a')
        try:
            for row in range(9):
                for col in range(9):
                    if GUIEntryBoard[row][col].get() == '':
                        file.write('0')
                    else:
                        file.write(GUIEntryBoard[row][col].get())
                    file.write(' ')
                file.write("\n")
            file.write("\n\n")
            file.close()
        except:
            print("ERROR!! FILE NOT SAVED!!")
        finally:
            file.close()

    def resetButtonFunction(self):
        for row in range(9):
            for col in range(9):
                GUIEntryBoard[row][col].set('')

solution = []
root = Tk()
txt = StringVar(root)
GUIEntryBoard = []
for rows in range(9):
    GUIEntryBoard += [[0,0,0,0,0,0,0,0,0]]
for row in range(9):
    for col in range(9):
        GUIEntryBoard[row][col] = StringVar(root)
a = SudokuGUI(root)
root.mainloop()
