import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")

        self.current_player = "X"

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text="", width=10, height=4, font=("Helvetica", 24), command=lambda i=i, j=j: self.handle_click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def handle_click(self, row, col):
        button = self.buttons[row][col]
        if button["text"] == "":
            button["text"] = self.current_player
            if self.current_player == "X":
                self.current_player = "O"
            else:
                self.current_player = "X"

        # Check if a player has won or if it's a tie
        winner = self.check_winner()
        if winner:
            messagebox.showinfo("Game over", f"{winner} wins!")
        elif self.check_tie():
            messagebox.showinfo("Game over", "It's a tie!")
            self.reset_game()

    def check_winner(self):
        # Check rows
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return self.buttons[i][0]["text"]

        # Check columns
        for i in range(3):
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return self.buttons[0][i]["text"]

        # Check diagonals
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return self.buttons[0][0]["text"]
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return self.buttons[0][2]["text"]

        return None

    def check_tie(self):
        for row in self.buttons:
            for button in row:
                if button["text"] == "":
                    return False
        return True

    def reset_game(self):
        for row in self.buttons:
            for button in row:
                button["text"] = ""
        self.current_player = "X"

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = TicTacToeGUI()
    gui.run()
