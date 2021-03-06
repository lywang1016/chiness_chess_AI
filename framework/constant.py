import pygame

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

round_imgs = {
    'r_move': pygame.image.load("img/r_move.jpg"),
    'b_move': pygame.image.load("img/b_move.jpg")
}

button_imgs = {
    'turn180': pygame.image.load("img/turn180.jpg"),
    'reset': pygame.image.load("img/reset.jpg"),
    'tie':pygame.image.load("img/tie.png")
}

piece_values = {
    'b_rook': -1,
    'b_knight': -2,
    'b_cannon': -3,
    'b_minister': -4,
    'b_warrior': -5,
    'b_pawn': -6,
    'b_king': -7,

    'r_rook': 1,
    'r_knight': 2,
    'r_cannon': 3,
    'r_minister': 4,
    'r_warrior': 5,
    'r_pawn': 6,
    'r_king': 7
}

values_piece = {
    -1: 'b_rook',
    -2: 'b_knight',
    -3: 'b_cannon',
    -4: 'b_minister',
    -5: 'b_warrior',
    -6: 'b_pawn',
    -7: 'b_king',

    1: 'r_rook',
    2: 'r_knight',
    3: 'r_cannon',
    4: 'r_minister',
    5: 'r_warrior',
    6: 'r_pawn',
    7: 'r_king'
}

values_piece2 = {
    -1: '俥',
    -2: '傌',
    -3: '砲',
    -4: '象',
    -5: '士',
    -6: '卒',
    -7: '将',
    0: '· ',
    1: '车',
    2: '马',
    3: '炮',
    4: '相',
    5: '仕',
    6: '兵',
    7: '帅'
}