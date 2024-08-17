from tkinter import *
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.config(bg="gray")
        
        self.initialize_game()
        self.create_widgets()

    def initialize_game(self):
        
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.winning_cells = []

    def create_widgets(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.turn_label = Label(self.root, text=f"Player {self.current_player}'s Turn", font=("Arial", 20,"bold"),bg=("yellow"))
        self.turn_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        for row in range(3):
            for col in range(3):
                button = Button(self.root, text="", font=('Arial', 40), width=3, height=1, command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row+1, column=col, padx=5, pady=5)
                self.buttons[row][col] = button
        
        self.restart_button = Button(self.root, text="Restart", font=('Arial', 20), command=self.restart_game)
        self.restart_button.grid(row=5, column=1, columnspan=4, pady=15)
        self.restart_button.grid_forget()

    def on_button_click(self, row, col):
        if self.board[row][col] is None and not self.check_win() and not self.check_draw():
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_win():
                self.highlight_winner()
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.restart_button.grid()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "The game is a draw!")
                self.restart_button.grid()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.turn_label.config(text=f"Player {self.current_player}'s Turn")

    def check_win(self):
        win_conditions = [[(row, col) for col in range(3)] for row in range(3)]+[[(row, col) for row in range(3)] for col in range(3)] +[ [(i, i) for i in range(3)],[(i, 2-i) for i in range(3)]]
        
        for condition in win_conditions:
            if all(self.board[r][c] == self.current_player for r, c in condition):
                self.winning_cells = condition
                return True
        return False

    def check_draw(self):
        return all(self.board[row][col] is not None for row in range(3) for col in range(3))

    def highlight_winner(self):
        for row, col in self.winning_cells:
            self.buttons[row][col].config(bg='lightgreen')

    def restart_game(self):
        self.initialize_game()
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="", bg='SystemButtonFace')
        self.restart_button.grid_forget()
        self.turn_label.config(text=f"Player {self.current_player}'s Turn")

def main():
    root = Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
