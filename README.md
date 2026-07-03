
TIC TAC TOE

A desktop Tic Tac Toe game built with Python's Tkinter, featuring:


Play with a Friend — classic local two-player mode
Play vs AI — an unbeatable AI opponent powered by the minimax algorithm
Score tracking across rounds
Simple sound effects (Windows beeps, or terminal bell on other platforms)


Requirements


- Python 3
- Tkinter 


No external dependencies are required.

Running the game

bashpython main.py

Project structure

tic-tac-toe/
├── main.py          # Entry point — starts the app
├── ui.py             # Tkinter UI: menu, board, screens, game flow
├── game_logic.py      # Win/draw detection and the minimax AI
├── sound.py           # Sound effect helpers
└── README.md

How the AI works

The AI (playing as O) uses the minimax algorithm to search every possible sequence of remaining moves and choose the one that leads to the best guaranteed outcome. Because Tic Tac Toe is a small, fully solved game, this AI never loses — the best a human opponent can achieve is a draw.

License

Feel free to use, modify, and share this project.

<img width="480" height="650" alt="Screenshot 2026-07-03 091423" src="https://github.com/user-attachments/assets/ef49d415-f038-4e92-b0e1-885898f29ae0" />
<img width="480" height="650" alt="Screenshot 2026-07-03 091448" src="https://github.com/user-attachments/assets/c7f22103-e0c4-4751-ab41-1783368320a7" />
