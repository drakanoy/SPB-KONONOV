import pygame
from random import randint


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 50

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for line in range(self.height):
            for cell in range(self.width):
                x = self.left + cell * (self.cell_size)
                y = self.top + line * (self.cell_size)
                a = randint(0, 255)
                b = randint(0, 255)
                c = randint(0, 255)
                if self.board[line][cell] == 0:
                    pygame.draw.rect(screen, (a, b, c), (x, y, self.cell_size, self.cell_size), 2)
                else:
                    pygame.draw.rect(screen, 'yellow', (x, y, self.cell_size, self.cell_size), 2)
                    pygame.draw.rect(screen, 'yellow', (x, y, self.cell_size, self.cell_size))

    def get_cell(self, mouse_x, mouse_y):
        cell = (mouse_x - self.left) // self.cell_size
        line = (mouse_y - self.top) // self.cell_size
        return (line, cell)

    def on_click(self, line, cell):
        if line < self.height and cell < self.width:
            if self.board[line][cell] == 0:
                self.board[line][cell] = 1
            else:
                self.board[line][cell] = 0


size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
board = Board(10, 10)  # здесь можно менять табличку

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.on_click(*board.get_cell(event.pos[0], event.pos[1]))
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
