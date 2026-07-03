
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = ""

WINNING_COMBINATIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   
    (0, 4, 8), (2, 4, 6)               
]


def check_winner(board):
    """Return (winner_mark, winning_combo) or (None, None) if no winner."""
    for a, b, c in WINNING_COMBINATIONS:
        if board[a] == board[b] == board[c] != EMPTY:
            return board[a], (a, b, c)
    return None, None


def check_draw(board):
    """Return True if the board is full (and, by caller convention,
    already confirmed to have no winner)."""
    return EMPTY not in board


def minimax(board, depth, is_maximizing, human_mark, ai_mark):
    """Recursively score a board position for the AI player.

    Positive scores favor the AI, negative scores favor the human.
    Shallower wins/losses are scored more strongly so the AI prefers
    winning sooner and losing later.
    """
    winner, _ = check_winner(board)
    if winner == ai_mark:
        return 10 - depth
    elif winner == human_mark:
        return depth - 10
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = ai_mark
                score_val = minimax(board, depth + 1, False, human_mark, ai_mark)
                board[i] = EMPTY
                best_score = max(best_score, score_val)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = human_mark
                score_val = minimax(board, depth + 1, True, human_mark, ai_mark)
                board[i] = EMPTY
                best_score = min(best_score, score_val)
        return best_score


def best_ai_move(board, human_mark, ai_mark):
    """Return the index of the best move for the AI, or None if the
    board is full."""
    best_score = -float("inf")
    move = None
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = ai_mark
            score_val = minimax(board, 0, False, human_mark, ai_mark)
            board[i] = EMPTY
            if score_val > best_score:
                best_score = score_val
                move = i
    return move
