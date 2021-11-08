import tkinter as tk
import tkinter.font as font

from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.X = []
        self.O = []

        self.combinations = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            ['1', '4', '7'],
            ['2', '5', '8'],
            ['3', '6', '9'],
            ['1', '5', '9'],
            ['3', '5', '7']
        ]

        self.turn = 'X'


        defaultFont = font.nametofont('TkDefaultFont')
        defaultFont.config(size=20)

        self.b1 = tk.Button(root, text=' ', height=3, width=6, command=lambda: self.select(self.b1, '1'))
        self.b2 = tk.Button(root, text=' ', height=3, width=6, command=lambda: self.select(self.b2, '2'))
        self.b3 = tk.Button(root, text=' ', height=3, width=6, command=lambda: self.select(self.b3, '3'))

        self.b4 = tk.Button(root, text=' ', height=3, width=6, command=lambda: self.select(self.b4, '4'))
        self.b5 = tk.Button(root, text=' ', height=3, width=6, command=lambda: self.select(self.b5, '5'))
        self.b6 = tk.Button(root, text=' ', height=3, width=6, command=lambda: self.select(self.b6, '6'))

        self.b7 = tk.Button(root, text=' ', height=3, width=6, command=lambda: self.select(self.b7, '7'))
        self.b8 = tk.Button(root, text=' ', height=3, width=6, command=lambda: self.select(self.b8, '8'))
        self.b9 = tk.Button(root, text=' ', height=3, width=6, command=lambda: self.select(self.b9, '9'))

        self.b1.grid(row=0, column=0)
        self.b2.grid(row=0, column=1)
        self.b3.grid(row=0, column=2)

        self.b4.grid(row=1, column=0)
        self.b5.grid(row=1, column=1)
        self.b6.grid(row=1, column=2)
        self.b7.grid(row=2, column=0)

        self.b8.grid(row=2, column=1)
        self.b9.grid(row=2, column=2)


    def select(self, b, c):
        if c in self.list:
            if self.turn == 'X':
                self.list.remove(c)
                self.X.append(c)

                b['text'] = 'X'

                self.turn = 'O'

            elif self.turn == 'O':
                self.list.remove(c)
                self.O.append(c)

                b['text'] = 'O'

                self.turn = 'X'
            
            self.verify()


    def verify(self):
        for combination in self.combinations:
            if combination[0] in self.X and combination[1] in self.X and combination[2] in self.X:
                messagebox.showinfo('Result', 'X win!')
                self.againMessage()

                return

            elif combination[0] in self.O and combination[1] in self.O and combination[2] in self.O:
                messagebox.showinfo('Result', 'O win!')
                self.againMessage()

                return
        
        if self.list == []:
            messagebox.showinfo('Result', 'Draw!')
            self.againMessage()


    def againMessage(self):
        again = messagebox.askyesno('Play again?', 'Play again?')

        if again:
            self.restart()


    def restart(self):
        self.list.clear()
        self.list.extend(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        self.X.clear()
        self.O.clear()
        self.b1['text'] = self.b2['text'] = self.b3['text'] = self.b4['text'] = self.b5['text'] = self.b6['text'] = self.b7['text'] = self.b8['text'] = self.b9['text'] = ' '


def main():
    root = tk.Tk()

    root.title('Tic tac toe')

    TicTacToe(root)

    root.mainloop()


if __name__ == '__main__':
    main()
