class Board:
    def __init__(self, board):
        self.board = board

    def __str__(self):
        # Crea una rappresentazione stringa della griglia del Sudoku, sostituendo gli zeri con asterischi
        board_str = ''
        for row in self.board:
            row_str = [str(i) if i else '*' for i in row]  # Sostituisce gli zeri con asterischi
            board_str += ' '.join(row_str)  # Unisce gli elementi della riga con spazi
            board_str += '\n'  # Aggiunge un'interruzione di riga dopo ogni riga
        return board_str

    def find_empty_cell(self):
        # Trova la prima cella vuota (valore zero) e restituisce la sua posizione (riga, colonna)
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)  # Cerca il primo zero nella riga corrente
                return row, col
            except ValueError:
                pass  # Se non ci sono zeri nella riga corrente, passa alla riga successiva
        return None  # Se non ci sono celle vuote, restituisce None

    def valid_in_row(self, row, num):
        # Verifica se il numero non è già presente nella riga specificata
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        # Verifica se il numero non è già presente nella colonna specificata
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        # Verifica se il numero non è già presente nel quadrato 3x3
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        # Verifica se è valido inserire il numero nella posizione specificata
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self):
        # Risolve il Sudoku utilizzando la ricorsione e il backtracking
        if (next_empty := self.find_empty_cell()) is None:
            return True  # Se non ci sono celle vuote, il Sudoku è risolto
        else:
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess  # Prova a inserire il numero nella cella vuota
                    if self.solver():
                        return True  # Se la chiamata ricorsiva risolve il Sudoku, restituisce True
                    else:
                        self.board[row][col] = 0  # Altrimenti, rimuove il numero (backtracking)
            else:
                return False  # Se nessun numero è valido, restituisce False

def solve_sudoku(board):
    # Funzione per risolvere il Sudoku dato
    gameboard = Board(board)
    print(f'Puzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print(f'Solved puzzle:\n{gameboard}')
    else:
        print('The provided puzzle is unsolvable.')
    return gameboard

# Definisce un puzzle Sudoku
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]

# Risolve il puzzle Sudoku
solve_sudoku(puzzle)
