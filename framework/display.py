import sys
import math
import pygame
from heapq import heapify, heappop, heappush
from framework.constant import pieces_images, values_piece, round_imgs, button_imgs

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
    
    def update(self, board, round):
        self.screen.blit(self.side_img, (0, 0))
        self.screen.blit(self.side_img, (360, 0))
        self.screen.blit(self.background_img, (10, 10))
        self.screen.blit(button_imgs['tie'], (569, 185))
        self.screen.blit(button_imgs['reset'], (545, 240))
        self.screen.blit(button_imgs['turn180'], (545, 300))

        if round == 'r':
            self.screen.blit(round_imgs['r_move'], (560, 40))
        else:
            self.screen.blit(round_imgs['b_move'], (560, 505))
            

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
                pos = pygame.mouse.get_pos()
                mouse_x = pos[0]-math.ceil(self.pixel_dif/2)
                mouse_y = pos[1]-math.ceil(self.pixel_dif/2)
                if mouse_x < 512 and mouse_y < 570:  
                    queue = []
                    heapify(queue)
                    for i in range(10):
                        for j in range(9):
                            center_x = self.positions[i][j][0]
                            center_y = self.positions[i][j][1]
                            dis = (center_x - mouse_x)**2 + (center_y - mouse_y)**2
                            heappush(queue, (dis, (i, j)))
                    dis, posi = heappop(queue)
                    return 'grid', posi
                elif mouse_x < 665 and mouse_x > 515 and mouse_y < 250 and mouse_y > 210:
                    return 'reset', (-1, -1)
                elif mouse_x < 665 and mouse_x > 515 and mouse_y < 310 and mouse_y > 270:
                    return 'turn180', (-1, -1)
                elif mouse_x < 640 and mouse_x > 540 and mouse_y < 200 and mouse_y > 155:
                    return 'tie', (-1, -1)
                else:
                    print(mouse_x)
                    print(mouse_y)
                    return 'none', (-1, -1)
        return 'none', (-1, -1)