class Empty:
    def __init__(self, color, x, y):
        self.x = x
        self.y = y
        self.color = color
        self.moved = False
        self.name = 'empty'

    def possible_moves(self):
        return []
    
    def clear_path(self, x1, y1, x2, y2, obstacles):
        return False
    
    def draw(self):
        return ' '

class Pawn:
    def __init__(self, color, x, y):
        self.x = x
        self.y = y
        self.color = color
        self.moved = False
        self.en_passant = False
        self.name = 'pawn'
    
    def possible_moves(self):
        x = self.x
        y = self.y
        if self.color == 'white':
            moves = [(x+1, y), (x+1, y+1), (x+1, y-1)]
            if not self.moved:
                moves.append((x+2, y))
        else:
            moves = [(x-1, y), (x-1, y+1), (x-1, y-1)]
            if not self.moved:
                moves.append((x-2, y))
        return moves

    def clear_path(self, x1, y1, x2, y2, obstacles):
        if y1 != y2:
            return obstacles[x2][y2]

        for i in range(min(x1, x2), max(x1, x2)+1):
            if obstacles[i][y1]:
                return False
                    
        return True
    
    def draw(self):
        return '\u2659' if self.color == 'black' else '\u265F'

class Knight:
    def __init__(self, color, x, y):
        self.x = x
        self.y = y
        self.color = color
        self.moved = False
        self.name = 'knight'

    def possible_moves(self):
        x = self.x
        y = self.y
        moves = [(x+1, y+2), (x+1, y-2), (x-1, y+2), (x-1, y-2), (x+2, y+1), (x+2, y-1), (x-2, y+1), (x-2, y-1)]
        return moves

    def clear_path(self, x1, y1, x2, y2, obstacles):
        return True
    
    def draw(self):
        return '\u2658' if self.color == 'black' else '\u265E'

class Bishop:
    def __init__(self, color, x, y):
        self.x = x
        self.y = y
        self.color = color
        self.moved = False
        self.name = 'bishop'

    def possible_moves(self):
        x = self.x
        y = self.y
        moves = []
        for i in range(8):
            moves.append((x+i, y+i))
            moves.append((x+i, y-i))
            moves.append((x-i, y+i))
            moves.append((x-i, y-i))
        return moves
    
    def clear_path(self, x1, y1, x2, y2, obstacles):
        x_delta = 1 if x1 < x2 else -1
        y_delta = 1 if y1 < y2 else -1
        for i in range(x1, x2, x_delta):
            if obstacles[i][y1+(i-x1)*y_delta]:
                return False
    
    def draw(self):
        return '\u2657' if self.color == 'black' else '\u265D'

class Rook:
    def __init__(self, color, x, y):
        self.x = x
        self.y = y
        self.color = color
        self.moved = False
        self.name = 'rook'

    def possible_moves(self):
        x = self.x
        y = self.y
        moves = []
        for i in range(8):
            moves.append((x, i))
            moves.append((i, y))
        return moves
    
    def clear_path(self, x1, y1, x2, y2, obstacles):
        obstacles[x2][y2] = False
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2)):
                if obstacles[x1][i]:
                    return False
        else:
            for i in range(min(x1, x2), max(x1, x2)):
                if obstacles[i][y1]:
                    return False
        return True
    
    def draw(self):
        return '\u2656' if self.color == 'black' else '\u265C'

class Queen:
    def __init__(self, color, x, y):
        self.x = x
        self.y = y
        self.color = color
        self.moved = False
        self.name = 'queen'

    def possible_moves(self):
        x = self.x
        y = self.y
        moves = []
        for i in range(8):
            moves.append((x+i, y+i))
            moves.append((x+i, y-i))
            moves.append((x-i, y+i))
            moves.append((x-i, y-i))
            moves.append((x, y+i))
            moves.append((x, y-i))
            moves.append((x+i, y))
            moves.append((x-i, y))
        return moves
    
    def clear_path(self, x1, y1, x2, y2, obstacles):
        obstacles[x2][y2] = False
        if x1 != x2 and y1 != y2:
            x_delta = 1 if x1 < x2 else -1
            y_delta = 1 if y1 < y2 else -1
            for i in range(x1, x2, x_delta):
                if obstacles[i][y1+(i-x1)*y_delta]:
                    return False
        else:
            if x1 == x2:
                for i in range(min(y1, y2), max(y1, y2)):
                    if obstacles[x1][i]:
                        return False
            else:
                for i in range(min(x1, x2), max(x1, x2)):
                    if obstacles[i][y1]:
                        return False
        return True
    
    def draw(self):
        return '\u2655' if self.color == 'black' else '\u265B'

class King:
    def __init__(self, color, x, y):
        self.x = x
        self.y = y
        self.color = color
        self.moved = False
        self.name = 'king'

    def possible_moves(self):
        x = self.x
        y = self.y
        moves = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:
                    moves.append(x+i, y+j)
        return moves
    
    def clear_path(self, x1, y1, x2, y2, obstacles):
        return True

    def draw(self):
        return '\u2654' if self.color == 'black' else '\u265A'

class Chess:
    def __init__(self):
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.pieces = self.get_pieces()
        self.move_count = 1
        self.turn = 'white'
        self.draw = True
        self.flip = True
        self.game_end = False
        self.white_king_x = 0
        self.white_king_y = 4
        self.black_king_x = 7
        self.black_king_y = 4
    
    def get_pieces(self):
        pieces = [[Empty('empty', x, y) for y in range(8)] for x in range(8)]
        for i in range(8):
            for j in range(8):
                if self.board[i][j] != ' ':
                    if self.board[i][j] == 'p':
                        pieces[i][j] = Pawn('white', i, j)
                    elif self.board[i][j] == 'r':
                        pieces[i][j] = Rook('white', i, j)
                    elif self.board[i][j] == 'n':
                        pieces[i][j] = Knight('white', i, j)
                    elif self.board[i][j] == 'b':
                        pieces[i][j] = Bishop('white', i, j)
                    elif self.board[i][j] == 'q':
                        pieces[i][j] = Queen('white', i, j)
                    elif self.board[i][j] == 'k':
                        pieces[i][j] = King('white', i, j)
                    elif self.board[i][j] == 'P':
                        pieces[i][j] = Pawn('black', i, j)
                    elif self.board[i][j] == 'R':
                        pieces[i][j] = Rook('black', i, j)
                    elif self.board[i][j] == 'N':
                        pieces[i][j] = Knight('black', i, j)
                    elif self.board[i][j] == 'B':
                        pieces[i][j] = Bishop('black', i, j)
                    elif self.board[i][j] == 'Q':
                        pieces[i][j] = Queen('black', i, j)
                    elif self.board[i][j] == 'K':
                        pieces[i][j] = King('black', i, j)
        return pieces
    
    def is_valid(self, x1, y1, x2, y2):
        if x1 < 0 or x1 > 7 or y1 < 0 or y1 > 7 or x2 < 0 or x2 > 7 or y2 < 0 or y2 > 7:
            return False

        pieces = self.pieces
        piece = pieces[x1][y1]
        if piece.color != self.turn:
            return False
        if pieces[x2][y2].color == piece.color:
            return False

        possible = piece.possible_moves()
        if (x2, y2) not in possible:
            return False

        if pieces[x1][y1].name == 'pawn' and pieces[x1][y2].name == 'pawn' and abs(x2-x1) == 1 and abs(y2-y1) == 1 and pieces[x1][y2].en_passant and pieces[x1][y1].color != pieces[x1][y2].color:
            return True
        
        obstacles = [[pieces[i][j].name!='empty' for j in range(8)] for i in range(8)]
        obstacles[x1][y1] = False
        if not piece.clear_path(x1, y1, x2, y2, obstacles):
            return False
        
        return True
    
    def is_attacked(self, x, y):
        for i in range(8):
            for j in range(8):
                if self.pieces[i][j].color != self.pieces[x][y].color and self.is_valid(i, j, x, y):
                    return True
        return False
    
    def move_piece(self, x1, y1, x2, y2):
        if self.is_valid(x1, y1, x2, y2):
            temp = self.pieces[x2][y2]
            piece = self.pieces[x1][y1]
            if piece.name == 'pawn' and self.pieces[x2][y2].name == 'empty':
                self.pieces[x1][y2] = Empty('empty', x1, y2)
            self.pieces[x2][y2] = piece
            self.pieces[x1][y1] = Empty('empty', x1, y1)

            for i in range(8):
                for j in range(8):
                    if self.pieces[i][j].name == 'pawn' and self.pieces[i][j].color == self.turn:
                        self.pieces[i][j].en_passant = False

            if piece.name == 'pawn':
                piece.en_passant = abs(x2 - x1) == 2
                if x2 == 0 or x2 == 7:
                    promoted = input('Promote to ([q]ueen, [r]ook, [b]ishop, [k]night): ')
                    if promoted[0].lower() == 'q':
                        self.pieces[x2][y2] = Queen(self.turn, x2, y2)
                    elif promoted[0].lower() == 'r':
                        self.pieces[x2][y2] = Rook(self.turn, x2, y2)
                    elif promoted[0].lower() == 'b':
                        self.pieces[x2][y2] = Bishop(self.turn, x2, y2)
                    elif promoted[0].lower() == 'k':
                        self.pieces[x2][y2] = Knight(self.turn, x2, y2)
                    else:
                        self.pieces[x1][y1] = piece
                        self.pieces[x2][y2] = temp
                        return False
            
            if piece.name == 'king':
                if piece.color == 'white':
                    self.white_king_x = x2
                    self.white_king_y = y2
                else:
                    self.black_king_x = x2
                    self.black_king_y = y2

            piece.x = x2
            piece.y = y2
            piece.moved = True
            self.turn = 'black' if self.turn == 'white' else 'white'
            self.move_count += 1
            return True
        else:
            return False
    
    def move(self, p1, p2):
        x1 = int(p1[1])
        y1 = ord(p1[0]) - 96
        x2 = int(p2[1])
        y2 = ord(p2[0]) - 96

        if not self.move_piece(x1-1, y1-1, x2-1, y2-1):
            print('INVALID MOVE, try again.')

    def draw_board(self):
        print()
        print('Move:', self.move_count, '-', 'Turn:', self.turn)
        print('   ' + '_' *16 + '   ')
        idx = 1
        for row in (self.pieces[::-1] if self.flip else self.pieces):
            print(8-idx+1 if self.flip else idx, '|', end='')
            for col in row:
                print(col.draw(), end=' ')
            print('|')
            idx += 1
        print('   ' + '‾' *16 + '   ')
        print('   a b c d e f g h   ')
        print()

    def flip_board(self):
        self.flip = not self.flip

game = Chess()
while not game.game_end:
    game.draw_board()
    p1, p2 = input('Enter move: ').split(' ')
    game.move(p1, p2)
