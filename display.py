import sys
import math
import pygame
from heapq import heapify, heappop, heappush
from utils import values_piece

pieces_images = {
    'b_rook': pygame.image.load("img/b_c.png"),
    'b_minister': pygame.image.load("img/b_x.png"),
    'b_king': pygame.image.load("img/b_j.png"),
    'b_knight': pygame.image.load("img/b_m.png"),
    'b_warrior': pygame.image.load("img/b_s.png"),
    'b_cannon': pygame.image.load("img/b_p.png"),
    'b_pawn': pygame.image.load("img/b_z.png"),

    'r_rook': pygame.image.load("img/r_c.png"),
    'r_minister': pygame.image.load("img/r_x.png"),
    'r_king': pygame.image.load("img/r_j.png"),
    'r_knight': pygame.image.load("img/r_m.png"),
    'r_warrior': pygame.image.load("img/r_s.png"),
    'r_cannon': pygame.image.load("img/r_p.png"),
    'r_pawn': pygame.image.load("img/r_z.png")
}

class GUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((720, 580))
        self.background_img = pygame.image.load("img/bg.png")
        self.side_img = pygame.image.load("img/bg.jpg")
        self.pixel_dif = 57
        pixel_init_row = 8
        pixel_init_col = 6
        self.piece_size = 50
        self.positions = []
        for i in range(10):
            temp = []
            for j in range(9):
                temp.append((pixel_init_col+j*self.pixel_dif, pixel_init_row+i*self.pixel_dif))
            self.positions.append(temp)
    
    def update(self, board):
        self.screen.blit(self.side_img, (0, 0))
        self.screen.blit(self.side_img, (360, 0))
        self.screen.blit(self.background_img, (10, 10))

        for i in range(10):
            for j in range(9):
                if board[i][j] != 0:
                    self.screen.blit(pieces_images[values_piece[board[i][j]]], self.positions[i][j])

        pygame.display.update()
    
    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  
            if event.type == pygame.MOUSEBUTTONDOWN:
                queue = []
                heapify(queue)
                pos = pygame.mouse.get_pos()
                mouse_x = pos[0]-math.ceil(self.pixel_dif/2)
                mouse_y = pos[1]-math.ceil(self.pixel_dif/2)
                if mouse_x < 512 and mouse_y < 570:
                    for i in range(10):
                        for j in range(9):
                            center_x = self.positions[i][j][0]
                            center_y = self.positions[i][j][1]
                            dis = (center_x - mouse_x)**2 + (center_y - mouse_y)**2
                            heappush(queue, (dis, (i, j)))
                    dis, posi = heappop(queue)
                    return posi
                else:
                    return (-1, -1)