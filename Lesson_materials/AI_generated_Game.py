import pygame
import random
import sys

# ============================================================
# SETUP
# ============================================================

pygame.init()

CELL_SIZE = 32
COLS = 10
ROWS = 20
BOARD_WIDTH = COLS * CELL_SIZE
BOARD_HEIGHT = ROWS * CELL_SIZE
SIDE_PANEL = 220
WIDTH = BOARD_WIDTH + SIDE_PANEL
HEIGHT = BOARD_HEIGHT
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animal Tetris")
clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 28, bold=True)
small_font = pygame.font.SysFont("arial", 18)
tiny_font = pygame.font.SysFont("arial", 14)

# ============================================================
# COLORS
# ============================================================

BLACK = (18, 18, 24)
WHITE = (245, 245, 245)
GRAY = (150, 150, 160)
GRID_COLOR = (40, 40, 55)
PANEL_BG = (28, 28, 38)

COLORS = {
    "I": (90, 200, 120),    # frog
    "O": (245, 220, 90),    # chick
    "T": (240, 150, 170),   # cat
    "S": (255, 170, 185),   # pig
    "Z": (245, 145, 70),    # fox
    "J": (235, 235, 235),   # panda
    "L": (230, 230, 255),   # bunny
}

ANIMALS = {
    "I": "frog",
    "O": "chick",
    "T": "cat",
    "S": "pig",
    "Z": "fox",
    "J": "panda",
    "L": "bunny",
}

# ============================================================
# TETROMINO SHAPES
# ============================================================

SHAPES = {
    "I": [
        [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ],
        [
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
        ],
    ],
    "O": [
        [
            [1, 1],
            [1, 1],
        ],
    ],
    "T": [
        [
            [0, 1, 0],
            [1, 1, 1],
            [0, 0, 0],
        ],
        [
            [0, 1, 0],
            [0, 1, 1],
            [0, 1, 0],
        ],
        [
            [0, 0, 0],
            [1, 1, 1],
            [0, 1, 0],
        ],
        [
            [0, 1, 0],
            [1, 1, 0],
            [0, 1, 0],
        ],
    ],
    "S": [
        [
            [0, 1, 1],
            [1, 1, 0],
            [0, 0, 0],
        ],
        [
            [0, 1, 0],
            [0, 1, 1],
            [0, 0, 1],
        ],
    ],
    "Z": [
        [
            [1, 1, 0],
            [0, 1, 1],
            [0, 0, 0],
        ],
        [
            [0, 0, 1],
            [0, 1, 1],
            [0, 1, 0],
        ],
    ],
    "J": [
        [
            [1, 0, 0],
            [1, 1, 1],
            [0, 0, 0],
        ],
        [
            [0, 1, 1],
            [0, 1, 0],
            [0, 1, 0],
        ],
        [
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 1],
        ],
        [
            [0, 1, 0],
            [0, 1, 0],
            [1, 1, 0],
        ],
    ],
    "L": [
        [
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0],
        ],
        [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 1],
        ],
        [
            [0, 0, 0],
            [1, 1, 1],
            [1, 0, 0],
        ],
        [
            [1, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
        ],
    ],
}

# ============================================================
# PIECE CLASS
# ============================================================

class Piece:
    def __init__(self, shape=None):
        if shape is None:
            shape = random.choice(list(SHAPES.keys()))
        self.shape = shape
        self.rotations = SHAPES[shape]
        self.rotation = 0
        self.x = COLS // 2 - 2
        self.y = 0
        self.color = COLORS[shape]
        self.animal = ANIMALS[shape]

    def matrix(self):
        return self.rotations[self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.rotations)

    def rotate_back(self):
        self.rotation = (self.rotation - 1) % len(self.rotations)

# ============================================================
# BOARD
# ============================================================

def create_board():
    return [[None for _ in range(COLS)] for _ in range(ROWS)]

def valid_position(board, piece, offset_x=0, offset_y=0):
    matrix = piece.matrix()
    for row_index, row in enumerate(matrix):
        for col_index, cell in enumerate(row):
            if not cell:
                continue

            x = piece.x + col_index + offset_x
            y = piece.y + row_index + offset_y

            if x < 0 or x >= COLS:
                return False
            if y >= ROWS:
                return False
            if y >= 0 and board[y][x] is not None:
                return False
    return True

def lock_piece(board, piece):
    matrix = piece.matrix()
    for row_index, row in enumerate(matrix):
        for col_index, cell in enumerate(row):
            if cell:
                x = piece.x + col_index
                y = piece.y + row_index
                if 0 <= y < ROWS:
                    board[y][x] = {
                        "color": piece.color,
                        "animal": piece.animal
                    }

def clear_lines(board):
    lines_cleared = 0
    new_board = []

    for row in board:
        if all(cell is not None for cell in row):
            lines_cleared += 1
        else:
            new_board.append(row)

    while len(new_board) < ROWS:
        new_board.insert(0, [None for _ in range(COLS)])

    return new_board, lines_cleared

def calculate_score(lines):
    scores = {1: 100, 2: 300, 3: 500, 4: 800}
    return scores.get(lines, 0)

# ============================================================
# DRAW ANIMAL BLOCKS
# ============================================================

def draw_eye(surface, x, y, r=2):
    pygame.draw.circle(surface, BLACK, (x, y), r)

def draw_animal_tile(surface, px, py, size, animal, color, outline=WHITE):
    rect = pygame.Rect(px + 2, py + 2, size - 4, size - 4)

    # shadow
    shadow = pygame.Rect(px + 4, py + 5, size - 4, size - 4)
    pygame.draw.rect(surface, (0, 0, 0, 40), shadow, border_radius=8)

    # base
    pygame.draw.rect(surface, color, rect, border_radius=8)
    pygame.draw.rect(surface, outline, rect, 2, border_radius=8)

    cx = px + size // 2
    cy = py + size // 2

    # common lighter face center
    face_rect = pygame.Rect(px + 6, py + 8, size - 12, size - 14)
    highlight = tuple(min(255, c + 25) for c in color)
    pygame.draw.rect(surface, highlight, face_rect, border_radius=8)

    if animal == "cat":
        pygame.draw.polygon(surface, color, [(px + 8, py + 10), (px + 13, py + 2), (px + 18, py + 10)])
        pygame.draw.polygon(surface, color, [(px + size - 18, py + 10), (px + size - 13, py + 2), (px + size - 8, py + 10)])
        draw_eye(surface, px + 12, py + 15, 2)
        draw_eye(surface, px + size - 12, py + 15, 2)
        pygame.draw.circle(surface, BLACK, (cx, py + 19), 2)
        pygame.draw.line(surface, BLACK, (cx, py + 21), (cx - 3, py + 24), 1)
        pygame.draw.line(surface, BLACK, (cx, py + 21), (cx + 3, py + 24), 1)
        pygame.draw.line(surface, BLACK, (cx - 4, py + 19), (cx - 9, py + 18), 1)
        pygame.draw.line(surface, BLACK, (cx - 4, py + 21), (cx - 9, py + 22), 1)
        pygame.draw.line(surface, BLACK, (cx + 4, py + 19), (cx + 9, py + 18), 1)
        pygame.draw.line(surface, BLACK, (cx + 4, py + 21), (cx + 9, py + 22), 1)

    elif animal == "frog":
        pygame.draw.circle(surface, WHITE, (px + 10, py + 9), 5)
        pygame.draw.circle(surface, WHITE, (px + size - 10, py + 9), 5)
        draw_eye(surface, px + 10, py + 9, 2)
        draw_eye(surface, px + size - 10, py + 9, 2)
        pygame.draw.arc(surface, BLACK, (px + 8, py + 13, size - 16, 10), 0.2, 2.9, 2)

    elif animal == "chick":
        draw_eye(surface, px + 12, py + 14, 2)
        draw_eye(surface, px + size - 12, py + 14, 2)
        pygame.draw.polygon(surface, (255, 140, 0), [(cx - 3, py + 18), (cx + 3, py + 18), (cx, py + 22)])
        pygame.draw.circle(surface, (255, 220, 130), (cx, py + 8), 4)

    elif animal == "pig":
        pygame.draw.polygon(surface, color, [(px + 8, py + 10), (px + 13, py + 4), (px + 16, py + 10)])
        pygame.draw.polygon(surface, color, [(px + size - 16, py + 10), (px + size - 13, py + 4), (px + size - 8, py + 10)])
        draw_eye(surface, px + 12, py + 14, 2)
        draw_eye(surface, px + size - 12, py + 14, 2)
        nose = pygame.Rect(cx - 6, py + 18, 12, 8)
        pygame.draw.ellipse(surface, (255, 120, 150), nose)
        pygame.draw.ellipse(surface, BLACK, nose, 1)
        pygame.draw.circle(surface, BLACK, (cx - 3, py + 22), 1)
        pygame.draw.circle(surface, BLACK, (cx + 3, py + 22), 1)

    elif animal == "fox":
        pygame.draw.polygon(surface, color, [(px + 8, py + 10), (px + 13, py + 2), (px + 18, py + 10)])
        pygame.draw.polygon(surface, color, [(px + size - 18, py + 10), (px + size - 13, py + 2), (px + size - 8, py + 10)])
        pygame.draw.polygon(surface, (255, 240, 220), [(cx, py + 13), (px + 9, py + 24), (px + size - 9, py + 24)])
        draw_eye(surface, px + 12, py + 14, 2)
        draw_eye(surface, px + size - 12, py + 14, 2)
        pygame.draw.circle(surface, BLACK, (cx, py + 22), 2)

    elif animal == "panda":
        pygame.draw.circle(surface, (50, 50, 50), (px + 10, py + 9), 5)
        pygame.draw.circle(surface, (50, 50, 50), (px + size - 10, py + 9), 5)
        pygame.draw.circle(surface, WHITE, (cx, cy), 10)
        pygame.draw.circle(surface, (50, 50, 50), (px + 12, py + 15), 4)
        pygame.draw.circle(surface, (50, 50, 50), (px + size - 12, py + 15), 4)
        draw_eye(surface, px + 12, py + 15, 2)
        draw_eye(surface, px + size - 12, py + 15, 2)
        pygame.draw.circle(surface, BLACK, (cx, py + 22), 2)

    elif animal == "bunny":
        pygame.draw.ellipse(surface, color, (px + 7, py + 1, 6, 12))
        pygame.draw.ellipse(surface, color, (px + size - 13, py + 1, 6, 12))
        pygame.draw.ellipse(surface, (255, 190, 210), (px + 9, py + 3, 2, 8))
        pygame.draw.ellipse(surface, (255, 190, 210), (px + size - 11, py + 3, 2, 8))
        draw_eye(surface, px + 12, py + 15, 2)
        draw_eye(surface, px + size - 12, py + 15, 2)
        pygame.draw.circle(surface, (255, 140, 160), (cx, py + 20), 2)
        pygame.draw.line(surface, BLACK, (cx, py + 22), (cx, py + 25), 1)
        pygame.draw.line(surface, BLACK, (cx, py + 25), (cx - 2, py + 27), 1)
        pygame.draw.line(surface, BLACK, (cx, py + 25), (cx + 2, py + 27), 1)

def draw_grid():
    for x in range(COLS + 1):
        pygame.draw.line(screen, GRID_COLOR, (x * CELL_SIZE, 0), (x * CELL_SIZE, BOARD_HEIGHT))
    for y in range(ROWS + 1):
        pygame.draw.line(screen, GRID_COLOR, (0, y * CELL_SIZE), (BOARD_WIDTH, y * CELL_SIZE))

def draw_board(board):
    pygame.draw.rect(screen, BLACK, (0, 0, BOARD_WIDTH, BOARD_HEIGHT))
    for y in range(ROWS):
        for x in range(COLS):
            cell = board[y][x]
            if cell is not None:
                draw_animal_tile(
                    screen,
                    x * CELL_SIZE,
                    y * CELL_SIZE,
                    CELL_SIZE,
                    cell["animal"],
                    cell["color"]
                )
    draw_grid()

def draw_piece(piece):
    matrix = piece.matrix()
    for row_index, row in enumerate(matrix):
        for col_index, cell in enumerate(row):
            if cell:
                x = piece.x + col_index
                y = piece.y + row_index
                if y >= 0:
                    draw_animal_tile(
                        screen,
                        x * CELL_SIZE,
                        y * CELL_SIZE,
                        CELL_SIZE,
                        piece.animal,
                        piece.color
                    )

def draw_ghost(board, piece):
    ghost_y = piece.y
    while valid_position(board, piece, offset_y=(ghost_y - piece.y + 1)):
        ghost_y += 1

    matrix = piece.matrix()
    for row_index, row in enumerate(matrix):
        for col_index, cell in enumerate(row):
            if cell:
                x = piece.x + col_index
                y = ghost_y + row_index
                if y >= 0:
                    rect = pygame.Rect(x * CELL_SIZE + 6, y * CELL_SIZE + 6, CELL_SIZE - 12, CELL_SIZE - 12)
                    pygame.draw.rect(screen, GRAY, rect, 2, border_radius=6)

def draw_next_piece(piece):
    label = font.render("NEXT", True, WHITE)
    screen.blit(label, (BOARD_WIDTH + 55, 120))

    matrix = piece.matrix()
    preview_size = 26
    start_x = BOARD_WIDTH + 60
    start_y = 170

    for row_index, row in enumerate(matrix):
        for col_index, cell in enumerate(row):
            if cell:
                draw_animal_tile(
                    screen,
                    start_x + col_index * preview_size,
                    start_y + row_index * preview_size,
                    preview_size,
                    piece.animal,
                    piece.color
                )

def draw_side_panel(score, level, lines, next_piece):
    pygame.draw.rect(screen, PANEL_BG, (BOARD_WIDTH, 0, SIDE_PANEL, HEIGHT))

    title = font.render("TETRIS", True, WHITE)
    subtitle = small_font.render("Animal Blocks", True, GRAY)
    screen.blit(title, (BOARD_WIDTH + 42, 28))
    screen.blit(subtitle, (BOARD_WIDTH + 46, 60))

    score_text = small_font.render(f"Score: {score}", True, WHITE)
    level_text = small_font.render(f"Level: {level}", True, WHITE)
    lines_text = small_font.render(f"Lines: {lines}", True, WHITE)

    screen.blit(score_text, (BOARD_WIDTH + 28, 90))
    screen.blit(level_text, (BOARD_WIDTH + 28, 112))
    screen.blit(lines_text, (BOARD_WIDTH + 28, 134))

    draw_next_piece(next_piece)

    y = 300
    controls = [
        "CONTROLS",
        "← →  Move",
        "↑    Rotate",
        "↓    Soft drop",
        "Space Hard drop",
        "R    Restart",
    ]
    for i, line in enumerate(controls):
        text = small_font.render(line, True, WHITE if i == 0 else GRAY)
        screen.blit(text, (BOARD_WIDTH + 24, y))
        y += 24

    y += 16
    legend = [
        ("I", "Frog"),
        ("O", "Chick"),
        ("T", "Cat"),
        ("S", "Pig"),
        ("Z", "Fox"),
        ("J", "Panda"),
        ("L", "Bunny"),
    ]
    title2 = small_font.render("ANIMALS", True, WHITE)
    screen.blit(title2, (BOARD_WIDTH + 24, y))
    y += 28

    for code, name in legend:
        draw_animal_tile(screen, BOARD_WIDTH + 28, y - 4, 24, ANIMALS[code], COLORS[code])
        text = tiny_font.render(f"{code} = {name}", True, GRAY)
        screen.blit(text, (BOARD_WIDTH + 60, y + 2))
        y += 28

def draw_game_over(score):
    overlay = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))

    text = font.render("GAME OVER", True, WHITE)
    score_text = small_font.render(f"Score: {score}", True, WHITE)
    restart_text = small_font.render("Press R to restart", True, WHITE)

    screen.blit(text, (BOARD_WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 60))
    screen.blit(score_text, (BOARD_WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 10))
    screen.blit(restart_text, (BOARD_WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 28))

# ============================================================
# GAME STATE
# ============================================================

def reset_game():
    board = create_board()
    current_piece = Piece()
    next_piece = Piece()
    score = 0
    lines = 0
    level = 1
    game_over = False
    return board, current_piece, next_piece, score, lines, level, game_over

# ============================================================
# MAIN GAME
# ============================================================

def main():
    board, current_piece, next_piece, score, lines, level, game_over = reset_game()
    fall_timer = 0
    running = True

    while running:
        delta_time = clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    board, current_piece, next_piece, score, lines, level, game_over = reset_game()
                    fall_timer = 0
                    continue

                if game_over:
                    continue

                if event.key == pygame.K_LEFT:
                    if valid_position(board, current_piece, offset_x=-1):
                        current_piece.x -= 1

                elif event.key == pygame.K_RIGHT:
                    if valid_position(board, current_piece, offset_x=1):
                        current_piece.x += 1

                elif event.key == pygame.K_DOWN:
                    if valid_position(board, current_piece, offset_y=1):
                        current_piece.y += 1
                        score += 1

                elif event.key == pygame.K_UP:
                    current_piece.rotate()
                    if not valid_position(board, current_piece):
                        if valid_position(board, current_piece, offset_x=-1):
                            current_piece.x -= 1
                        elif valid_position(board, current_piece, offset_x=1):
                            current_piece.x += 1
                        elif valid_position(board, current_piece, offset_x=-2):
                            current_piece.x -= 2
                        elif valid_position(board, current_piece, offset_x=2):
                            current_piece.x += 2
                        else:
                            current_piece.rotate_back()

                elif event.key == pygame.K_SPACE:
                    drop_distance = 0
                    while valid_position(board, current_piece, offset_y=1):
                        current_piece.y += 1
                        drop_distance += 1

                    score += drop_distance * 2
                    lock_piece(board, current_piece)
                    board, cleared = clear_lines(board)

                    if cleared > 0:
                        lines += cleared
                        score += calculate_score(cleared) * level

                    level = 1 + lines // 10
                    current_piece = next_piece
                    next_piece = Piece()

                    if not valid_position(board, current_piece):
                        game_over = True

                    fall_timer = 0

        if not game_over:
            fall_timer += delta_time
            fall_speed = max(100, 700 - ((level - 1) * 60))

            if fall_timer >= fall_speed:
                fall_timer = 0

                if valid_position(board, current_piece, offset_y=1):
                    current_piece.y += 1
                else:
                    lock_piece(board, current_piece)
                    board, cleared = clear_lines(board)

                    if cleared > 0:
                        lines += cleared
                        score += calculate_score(cleared) * level

                    level = 1 + lines // 10
                    current_piece = next_piece
                    next_piece = Piece()

                    if not valid_position(board, current_piece):
                        game_over = True

        screen.fill(BLACK)
        draw_board(board)

        if not game_over:
            draw_ghost(board, current_piece)
            draw_piece(current_piece)

        draw_side_panel(score, level, lines, next_piece)

        if game_over:
            draw_game_over(score)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()