
import tkinter as tk
from tkinter import messagebox

from game_logic import (
    PLAYER_X,
    PLAYER_O,
    EMPTY,
    check_winner,
    check_draw,
    best_ai_move,
)
from sound import play_click, play_win, play_draw

COLOR_BG = "#2b2d42"
COLOR_BTN = "#edf2f4"
COLOR_BTN_X = "#ef233c"
COLOR_BTN_O = "#3a86ff"
COLOR_WIN = "#8ac926"
COLOR_TEXT = "#edf2f4"

HUMAN_MARK = PLAYER_X
AI_MARK = PLAYER_O


class TicTacToeApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("420x640")
        self.window.configure(bg=COLOR_BG)

        self.current_player = PLAYER_X
        self.board = [EMPTY] * 9
        self.buttons = []
        self.score = {PLAYER_X: 0, PLAYER_O: 0, "Draws": 0}
        self.game_over = False
        self.game_mode = None

        self._build_menu_frame()
        self._build_game_frame()

        self.menu_frame.pack(expand=True)

    def _build_menu_frame(self):
        self.menu_frame = tk.Frame(self.window, bg=COLOR_BG)

        menu_title = tk.Label(
            self.menu_frame,
            text="TIC TAC TOE",
            font=("Arial", 28, "bold"),
            bg=COLOR_BG,
            fg=COLOR_TEXT
        )
        menu_title.pack(pady=(40, 10))

        menu_subtitle = tk.Label(
            self.menu_frame,
            text="Choose a Game Mode",
            font=("Arial", 14),
            bg=COLOR_BG,
            fg="#adb5bd"
        )
        menu_subtitle.pack(pady=(0, 30))

        friend_button = tk.Button(
            self.menu_frame,
            text="👥  Play with Friend",
            font=("Arial", 15),
            bg="#3a86ff",
            fg="white",
            relief="flat",
            width=20,
            pady=10,
            command=lambda: self.start_game("friend")
        )
        friend_button.pack(pady=10)

        ai_button = tk.Button(
            self.menu_frame,
            text="🤖  Play vs AI",
            font=("Arial", 15),
            bg="#ef233c",
            fg="white",
            relief="flat",
            width=20,
            pady=10,
            command=lambda: self.start_game("ai")
        )
        ai_button.pack(pady=10)

        ai_note = tk.Label(
            self.menu_frame,
            text="(AI plays as O and is unbeatable)",
            font=("Arial", 10),
            bg=COLOR_BG,
            fg="#6c757d"
        )
        ai_note.pack(pady=(10, 0))

    def _build_game_frame(self):
        self.game_frame = tk.Frame(self.window, bg=COLOR_BG)

        self.status = tk.Label(
            self.game_frame,
            text="Player X's Turn",
            font=("Arial", 15),
            bg=COLOR_BG,
            fg=COLOR_TEXT
        )
        self.status.pack(pady=(15, 5))

        self.score_label = tk.Label(
            self.game_frame,
            text="X Wins: 0   O Wins: 0   Draws: 0",
            font=("Arial", 11),
            bg=COLOR_BG,
            fg="#adb5bd"
        )
        self.score_label.pack(pady=(0, 10))

        board_frame = tk.Frame(self.game_frame, bg=COLOR_BG)
        board_frame.pack()

        for row in range(3):
            for col in range(3):
                index = row * 3 + col
                button = tk.Button(
                    board_frame,
                    text="",
                    width=5,
                    height=2,
                    font=("Arial", 24, "bold"),
                    bg=COLOR_BTN,
                    activebackground="#dee2e6",
                    relief="flat",
                    command=lambda i=index: self.button_click(i)
                )
                button.grid(row=row, column=col, padx=4, pady=4)
                self.buttons.append(button)

        controls_frame = tk.Frame(self.game_frame, bg=COLOR_BG)
        controls_frame.pack(pady=20)

        restart_button = tk.Button(
            controls_frame,
            text="New Round",
            font=("Arial", 13),
            bg="#8d99ae",
            fg="white",
            relief="flat",
            padx=10,
            command=lambda: self.restart(reset_score=False)
        )
        restart_button.grid(row=0, column=0, padx=6)

        reset_score_button = tk.Button(
            controls_frame,
            text="Reset Score",
            font=("Arial", 13),
            bg="#ef233c",
            fg="white",
            relief="flat",
            padx=10,
            command=lambda: self.restart(reset_score=True)
        )
        reset_score_button.grid(row=0, column=1, padx=6)

        menu_button = tk.Button(
            self.game_frame,
            text="⬅ Back to Menu",
            font=("Arial", 12),
            bg="#2b2d42",
            fg="#adb5bd",
            relief="flat",
            command=self.go_to_menu
        )
        menu_button.pack(pady=(5, 10))

    def update_score_label(self):
        self.score_label.config(
            text=f"X Wins: {self.score[PLAYER_X]}   "
                 f"O Wins: {self.score[PLAYER_O]}   "
                 f"Draws: {self.score['Draws']}"
        )

    def highlight_winning_cells(self, combo):
        for i in combo:
            self.buttons[i].config(bg=COLOR_WIN, fg="white")

    def end_game(self, winner, combo):
        self.game_over = True
        for button in self.buttons:
            button.config(state="disabled")

        if winner:
            self.highlight_winning_cells(combo)
            self.score[winner] += 1
            play_win()
            label_text = f"Player {winner} Wins! 🎉"
            if self.game_mode == "ai" and winner == AI_MARK:
                label_text = "AI Wins! 🤖"
            elif self.game_mode == "ai" and winner == HUMAN_MARK:
                label_text = "You Win! 🎉"
            self.status.config(text=label_text)
            messagebox.showinfo("Game Over", label_text)
        else:
            self.score["Draws"] += 1
            play_draw()
            self.status.config(text="It's a Draw!")
            messagebox.showinfo("Game Over", "It's a Draw!")

        self.update_score_label()

    def place_mark(self, index):
        self.board[index] = self.current_player
        color = COLOR_BTN_X if self.current_player == PLAYER_X else COLOR_BTN_O
        self.buttons[index].config(text=self.current_player, fg=color)
        play_click()

        winner, combo = check_winner(self.board)
        if winner:
            self.end_game(winner, combo)
            return
        if check_draw(self.board):
            self.end_game(None, None)
            return

        self.current_player = PLAYER_O if self.current_player == PLAYER_X else PLAYER_X
        self.status.config(text=f"Player {self.current_player}'s Turn")

        if self.game_mode == "ai" and self.current_player == AI_MARK and not self.game_over:
            self.window.after(400, self.ai_take_turn)

    def ai_take_turn(self):
        if self.game_over:
            return
        move = best_ai_move(self.board, HUMAN_MARK, AI_MARK)
        if move is not None:
            self.place_mark(move)

    def button_click(self, index):
        if self.game_over or self.board[index] != EMPTY:
            return
        if self.game_mode == "ai" and self.current_player != HUMAN_MARK:
            return  # ignore clicks during AI's turn
        self.place_mark(index)

    def restart(self, reset_score=False):
        self.current_player = PLAYER_X
        self.board = [EMPTY] * 9
        self.game_over = False
        self.status.config(text="Player X's Turn")
        for button in self.buttons:
            button.config(text="", state="normal", bg=COLOR_BTN, fg="black")

        if reset_score:
            self.score[PLAYER_X] = 0
            self.score[PLAYER_O] = 0
            self.score["Draws"] = 0
            self.update_score_label()

        if self.game_mode == "ai" and self.current_player == AI_MARK:
            self.window.after(400, self.ai_take_turn)

    def go_to_menu(self):
        self.game_frame.pack_forget()
        self.menu_frame.pack(expand=True)

    def start_game(self, mode):
        self.game_mode = mode
        self.restart(reset_score=True)
        self.menu_frame.pack_forget()
        self.game_frame.pack(expand=True)
        if mode == "ai":
            self.status.config(text="You are X — Your Turn")
        else:
            self.status.config(text="Player X's Turn")

    def run(self):
        self.window.mainloop()


def run_app():
    app = TicTacToeApp()
    app.run()
