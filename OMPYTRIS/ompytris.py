# PYTRIS Copyright (c) 2017 Jason Kim All Rights Reserved.

import pygame
import operator
from mino import *
from random import *
from pygame.locals import *

# Define
block_size = 17 # Height, width of single block
width = 10 # Board width
height = 20 # Board height

board_width = 800
board_height = 450
block_size = int(board_height*0.045)

framerate = 30 # Bigger -> Slower

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((board_width, board_height))
pygame.time.set_timer(pygame.USEREVENT, framerate * 10)
pygame.display.set_caption("PYTRIS")

class ui_variables:
    # Fonts
    font_path = "./assets/fonts/OpenSans-Light.ttf"
    font_path_b = "./assets/fonts/OpenSans-Bold.ttf"
    font_path_i = "./assets/fonts/Inconsolata/Inconsolata.otf"

    h1 = pygame.font.Font(font_path_b, 50)
    h2 = pygame.font.Font(font_path_b, 30)
    h4 = pygame.font.Font(font_path_b, 20)
    h5 = pygame.font.Font(font_path_b, 13)
    h6 = pygame.font.Font(font_path_b, 10)

    h1_b = pygame.font.Font(font_path_b, 50)
    h2_b = pygame.font.Font(font_path_b, 30)

    h2_i = pygame.font.Font(font_path_i, 30)
    h5_i = pygame.font.Font(font_path_i, 13)

    # Sounds
    click_sound = pygame.mixer.Sound("assets/sounds/SFX_ButtonUp.wav")
    move_sound = pygame.mixer.Sound("assets/sounds/SFX_PieceMoveLR.wav")
    drop_sound = pygame.mixer.Sound("assets/sounds/SFX_PieceHardDrop.wav")
    single_sound = pygame.mixer.Sound("assets/sounds/SFX_SpecialLineClearSingle.wav")
    double_sound = pygame.mixer.Sound("assets/sounds/SFX_SpecialLineClearDouble.wav")
    triple_sound = pygame.mixer.Sound("assets/sounds/SFX_SpecialLineClearTriple.wav")
    tetris_sound = pygame.mixer.Sound("assets/sounds/SFX_SpecialTetris.wav")

    # Background colors
    black = (10, 10, 10) #rgb(10, 10, 10)
    white = (0, 153, 153) #rgb(255, 255, 255) # 청록색으로 변경
    real_white = (255, 255, 255) #rgb(255, 255, 255) # 청록색으로 변경

    grey_1 = (26, 26, 26) #rgb(26, 26, 26) 
    grey_2 = (35, 35, 35) #rgb(35, 35, 35)
    grey_3 = (55, 55, 55) #rgb(55, 55, 55)
    bright_yellow = (255,217,102) # 밝은 노랑

    # Tetrimino colors
    cyan = (69, 206, 204) #rgb(69, 206, 204) # I
    blue = (64, 111, 249) #rgb(64, 111, 249) # J
    orange = (253, 189, 53) #rgb(253, 189, 53) # L
    yellow = (246, 227, 90) #rgb(246, 227, 90) # O
    green = (98, 190, 68) #rgb(98, 190, 68) # S
    pink = (242, 64, 235) #rgb(242, 64, 235) # T
    red = (225, 13, 27) #rgb(225, 13, 27) # Z

    t_color = [grey_2, cyan, blue, orange, yellow, green, pink, red, grey_3]

class button():
    def __init__(self, x, y, width, height, id, img = ''):
        self.x = x
        self.y = y
        self.width =width
        self.height = height
        self.id = id
        self.image = img

    def draw(self, win , outline = None):
        if outline:
            draw_image(screen, self.image, self.x, self.y, self.width, self.height)
    def isOver(self,pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
start_image = 'assets/images/start.png'
help_image = 'assets/images/help.png'
start_button = button(board_width*0.5, board_height*0.5,146,43,1,start_image)

background_image = 'assets/vector/Background.png'

single_button_image = 'assets/vector/single_button.png'
clicked_single_button_image = 'assets/vector/clicked_single_button.png'

pvp_button_image = 'assets/vector/pvp_button.png'
clicked_pvp_button_image = 'assets/vector/clicked_pvp_button.png'



help_button_image = 'assets/vector/help_button.png'
clicked_help_button_image = 'assets/vector/clicked_help_button.png'


quit_button_image = 'assets/vector/quit_button.png'
clicked_quit_button_image = 'assets/vector/clicked_quit_button.png'

leaderboard_vector = 'assets/vector/leaderboard_vector.png'
clicked_leaderboard_vector = 'assets/vector/clicked_leader_vector.png'

setting_vector = 'assets/vector/setting_vector.png'
clicked_setting_vector = 'assets/vector/clicked_setting_vector.png'

pause_board_image= 'assets/vector/pause_board.png'
leader_board_image= 'assets/vector/leader_board.png'
setting_board_image = 'assets/vector/setting_board.png'


resume_button_image = 'assets/vector/resume_button.png'
clicked_resume_button_image = 'assets/vector/clicked_resume_button.png'

restart_button_image = 'assets/vector/restart_button.png'
clicked_restart_button_image = 'assets/vector/clicked_restart_button.png'

setting_button_image = 'assets/vector/setting_button.png'
clicked_setting_button_image = 'assets/vector/clicked_setting_button.png'

back_button_image = 'assets/vector/back_button.png'
clicked_back_button_image = 'assets/vector/clicked_back_button.png'

volume_vector = 'assets/vector/volume_vector.png'
clicked_volume_vector = 'assets/vector/clicked_volume_vector.png'

keyboard_vector = 'assets/vector/keyboard_vector.png'
clicked_keyboard_vector = 'assets/vector/clicked_keyboard_vector.png'

screen_vector = 'assets/vector/screen_vector.png'
clicked_screen_vector = 'assets/vector/clicked_screen_vector.png'



single_button = button(board_width*0.6, board_height*0.15,int(board_width*0.3734), int(board_height*0.1777),1,single_button_image)

pvp_button = button(board_width*0.6, board_height*0.35,int(board_width*0.3734), int(board_height*0.1777),2,pvp_button_image)

help_button = button(board_width*0.6, board_height*0.55,int(board_width*0.3734), int(board_height*0.1777),3,help_button_image)

quit_button = button(board_width*0.6, board_height*0.75,int(board_width*0.3734), int(board_height*0.1777),4,quit_button_image)

setting_icon = button(board_width*0.02, board_height*0.75,int(board_height*0.23), int(board_height*0.23),5,setting_vector)

leaderboard_icon = button(board_width*0.02, board_height*0.5,int(board_height*0.23), int(board_height*0.23),6,leaderboard_vector)

resume_button    = button(board_width*0.324, board_height*0.15,int(board_width*0.3734), int(board_height*0.1777),1,resume_button_image)
restart_button   = button(board_width*0.324, board_height*0.35,int(board_width*0.3734), int(board_height*0.1777),1,restart_button_image)
setting_button   = button(board_width*0.324, board_height*0.55,int(board_width*0.3734), int(board_height*0.1777),1,setting_button_image)
pause_quit_button= button(board_width*0.324, board_height*0.75,int(board_width*0.3734), int(board_height*0.1777),1,quit_button_image)

back_button      = button(board_width*0.324, board_height*0.75,int(board_width*0.3734), int(board_height*0.1777),1,back_button_image)

volume_icon = button(board_width*0.25, board_height*0.3,int(board_height*0.23), int(board_height*0.23),5,volume_vector)

screen_icon = button(board_width*0.45, board_height*0.3,int(board_height*0.23), int(board_height*0.23),6,screen_vector)

keyboard_icon = button(board_width*0.65, board_height*0.3,int(board_height*0.23), int(board_height*0.23),6,keyboard_vector)


def checkCombo(combo_count,sent):
    if combo_count > 0:
        if combo_count <= 8:
            sent += (combo_count+1)/2
        else :
            sent += 4
    return sent

def draw_image(window,img_path, x,y,width,height):

    image= pygame.image.load(img_path)
    image = pygame.transform.scale(image,(width,height))
    window.blit(image,(x,y))

# Draw block
def draw_block(x, y, color):
    pygame.draw.rect(
        screen,
        color,
        Rect(x, y, block_size, block_size)
    )
    pygame.draw.rect(
        screen,
        ui_variables.grey_1,
        Rect(x, y, block_size, block_size),
        1
    )

# Draw game screen
def draw_board(next, hold, score, level, goal):
    sidebar_width = int(board_width*0.5312)
    

    # Draw sidebar
    pygame.draw.rect(
        screen,
        ui_variables.white,
        Rect(sidebar_width, 0, int(board_width*0.1875), board_height)
    )

    # Draw next mino
    grid_n = tetrimino.mino_map[next - 1][0]

    for i in range(4):
        for j in range(4):
            dx = int(board_width*0.045)+sidebar_width + block_size * j
            dy = int(board_height*0.3743) + block_size * i
            if grid_n[i][j] != 0:
                draw_block(dx,dy,ui_variables.t_color[grid_n[i][j]])
                

    # Draw hold mino
    grid_h = tetrimino.mino_map[hold - 1][0]

    if hold_mino != -1:
        for i in range(4):
            for j in range(4):
                dx = int(board_width*0.045) + sidebar_width + block_size * j
                dy = int(board_height*0.1336) + block_size * i
                if grid_h[i][j] != 0:
                    draw_block(dx,dy,ui_variables.t_color[grid_h[i][j]])

    # Set max score
    if score > 999999:
        score = 999999

    # Draw texts
    text_hold = ui_variables.h5.render("HOLD", 1, ui_variables.real_white)
    text_next = ui_variables.h5.render("NEXT", 1, ui_variables.real_white)
    text_score = ui_variables.h5.render("SCORE", 1, ui_variables.real_white)
    score_value = ui_variables.h4.render(str(score), 1, ui_variables.real_white)
    text_level = ui_variables.h5.render("LEVEL", 1, ui_variables.real_white)
    level_value = ui_variables.h4.render(str(level), 1, ui_variables.real_white)
    text_goal = ui_variables.h5.render("GOAL", 1, ui_variables.real_white)
    goal_value = ui_variables.h4.render(str(goal), 1, ui_variables.real_white)

    # Place texts
    screen.blit(text_hold, (int(board_width*0.045)+sidebar_width, int(board_height*0.0374)))
    screen.blit(text_next, (int(board_width*0.045)+sidebar_width , int(board_height*0.2780)))
    screen.blit(text_score, (int(board_width*0.045) + sidebar_width, int(board_height*0.5187)))
    screen.blit(score_value, (int(board_width*0.055) + sidebar_width, int(board_height*0.5614)))
    screen.blit(text_level, (int(board_width*0.045) + sidebar_width, int(board_height*0.6791)))
    screen.blit(level_value, (int(board_width*0.055) + sidebar_width , int(board_height*0.7219)))
    screen.blit(text_goal, (int(board_width*0.045) + sidebar_width , int(board_height*0.8395)))
    screen.blit(goal_value, (int(board_width*0.055) + sidebar_width, int(board_height*0.8823)))

    # Draw board
    for x in range(width):
        for y in range(height):
            dx = int(board_width*0.25) + block_size * x
            dy = int(board_height*0.055) + block_size * y
            draw_block(dx, dy, ui_variables.t_color[matrix[x][y + 1]])
def draw_1Pboard(next, hold, score, level, goal):
    sidebar_width = int(board_width*0.2867)
    

    # Draw sidebar
    pygame.draw.rect(
        screen,
        ui_variables.white,
        Rect(sidebar_width, 0, int(board_width*0.1875), board_height)
    )

    # Draw next mino
    grid_n = tetrimino.mino_map[next - 1][0]

    for i in range(4):
        for j in range(4):
            dx = int(board_width*0.045)+sidebar_width + block_size * j
            dy = int(board_height*0.3743) + block_size * i
            if grid_n[i][j] != 0:
                draw_block(dx,dy,ui_variables.t_color[grid_n[i][j]])
                

    # Draw hold mino
    grid_h = tetrimino.mino_map[hold - 1][0]


    if hold_mino != -1:
        for i in range(4):
            for j in range(4):
                dx = int(board_width*0.045) + sidebar_width + block_size * j
                dy = int(board_height*0.1336) + block_size * i
                if grid_h[i][j] != 0:
                    draw_block(dx,dy,ui_variables.t_color[grid_h[i][j]])

    # Set max score
    if score > 999999:
        score = 999999

    # Draw texts
    text_hold = ui_variables.h5.render("HOLD", 1, ui_variables.real_white)
    text_next = ui_variables.h5.render("NEXT", 1, ui_variables.real_white)
    text_score = ui_variables.h5.render("SCORE", 1, ui_variables.real_white)
    score_value = ui_variables.h4.render(str(score), 1, ui_variables.real_white)
    text_level = ui_variables.h5.render("LEVEL", 1, ui_variables.real_white)
    level_value = ui_variables.h4.render(str(level), 1, ui_variables.real_white)
    text_goal = ui_variables.h5.render("GOAL", 1, ui_variables.real_white)
    goal_value = ui_variables.h4.render(str(goal), 1, ui_variables.real_white)

    # Place texts
    screen.blit(text_hold, (int(board_width*0.045)+sidebar_width, int(board_height*0.0374)))
    screen.blit(text_next, (int(board_width*0.045)+sidebar_width , int(board_height*0.2780)))
    screen.blit(text_score, (int(board_width*0.045) + sidebar_width, int(board_height*0.5187)))
    screen.blit(score_value, (int(board_width*0.055) + sidebar_width, int(board_height*0.5614)))
    screen.blit(text_level, (int(board_width*0.045) + sidebar_width, int(board_height*0.6791)))
    screen.blit(level_value, (int(board_width*0.055) + sidebar_width , int(board_height*0.7219)))
    screen.blit(text_goal, (int(board_width*0.045) + sidebar_width , int(board_height*0.8395)))
    screen.blit(goal_value, (int(board_width*0.055) + sidebar_width, int(board_height*0.8823)))

    # Draw board
    for x in range(width):
        for y in range(height):
            dx = int(board_height*0.055) + block_size * x
            dy = int(board_height*0.055) + block_size * y
            draw_block(dx, dy, ui_variables.t_color[matrix[x][y + 1]])

def draw_2Pboard(next, hold, score, level, goal):

    sidebar_width = int(board_width*0.7867)
    

    # Draw sidebar
    pygame.draw.rect(
        screen,
        ui_variables.white,
        Rect(sidebar_width, 0, int(board_width*0.1875), board_height)
    )

    # Draw next mino
    grid_n = tetrimino.mino_map[next - 1][0]

    for i in range(4): # 16개의 그리드 칸에서 true인 값만 뽑아서 draw.rect
        for j in range(4):
            dx = int(board_width*0.045)+sidebar_width + block_size * j
            dy = int(board_height*0.3743) + block_size * i
            if grid_n[i][j] != 0:
                draw_block(dx,dy,ui_variables.t_color[grid_n[i][j]]) # 다음 블럭의 형상 가독성을 높임.
                

    # Draw hold mino
    grid_h = tetrimino.mino_map[hold - 1][0]

    if hold_mino != -1:
        for i in range(4):
            for j in range(4):
                dx = int(board_width*0.045) + sidebar_width + block_size * j
                dy = int(board_height*0.1336) + block_size * i
                if grid_h[i][j] != 0:
                    draw_block(dx,dy,ui_variables.t_color[grid_h[i][j]])

    # Set max score
    if score > 999999:
        score = 999999

    text_hold = ui_variables.h5.render("HOLD", 1, ui_variables.real_white)
    text_next = ui_variables.h5.render("NEXT", 1, ui_variables.real_white)
    text_score = ui_variables.h5.render("SCORE", 1, ui_variables.real_white)
    score_value = ui_variables.h4.render(str(score), 1, ui_variables.real_white)
    text_level = ui_variables.h5.render("LEVEL", 1, ui_variables.real_white)
    level_value = ui_variables.h4.render(str(level), 1, ui_variables.real_white)
    text_goal = ui_variables.h5.render("GOAL", 1, ui_variables.real_white)
    goal_value = ui_variables.h4.render(str(goal), 1, ui_variables.real_white)

    # Place texts
    screen.blit(text_hold, (int(board_width*0.045)+sidebar_width, int(board_height*0.0374)))
    screen.blit(text_next, (int(board_width*0.045)+sidebar_width , int(board_height*0.2780)))
    screen.blit(text_score, (int(board_width*0.045) + sidebar_width, int(board_height*0.5187)))
    screen.blit(score_value, (int(board_width*0.055) + sidebar_width, int(board_height*0.5614)))
    screen.blit(text_level, (int(board_width*0.045) + sidebar_width, int(board_height*0.6791)))
    screen.blit(level_value, (int(board_width*0.055) + sidebar_width , int(board_height*0.7219)))
    screen.blit(text_goal, (int(board_width*0.045) + sidebar_width , int(board_height*0.8395)))
    screen.blit(goal_value, (int(board_width*0.055) + sidebar_width, int(board_height*0.8823)))

    # Draw board
    for x in range(width):
        for y in range(height):
            dx = int(board_width*0.5) + block_size * x
            dy = int(board_height*0.055) + block_size * y
            draw_block(dx, dy, ui_variables.t_color[matrix_2P[x][y + 1]])

# Draw a tetrimino
def draw_mino(x, y, mino, r):
    grid = tetrimino.mino_map[mino - 1][r]

    tx, ty = x, y
    while not is_bottom(tx, ty, mino, r):
        ty += 1

    # Draw ghost
    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                matrix[tx + j][ty + i] = 8

    # Draw mino
    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                matrix[x + j][y + i] = grid[i][j]
def draw_mino_2P(x, y, mino, r):
    grid = tetrimino.mino_map[mino - 1][r]

    tx, ty = x, y
    while not is_bottom_2P(tx, ty, mino, r):
        ty += 1

    # Draw ghost
    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                matrix_2P[tx + j][ty + i] = 8

    # Draw mino
    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                matrix_2P[x + j][y + i] = grid[i][j]

# Erase a tetrimino
def erase_mino(x, y, mino, r):
    grid = tetrimino.mino_map[mino - 1][r]

    # Erase ghost
    for j in range(21):
        for i in range(10):
            if matrix[i][j] == 8:
                matrix[i][j] = 0

    # Erase mino
    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                matrix[x + j][y + i] = 0
def erase_mino_2P(x, y, mino, r):
    grid = tetrimino.mino_map[mino - 1][r]

    # Erase ghost
    for j in range(21):
        for i in range(10):
            if matrix_2P[i][j] == 8:
                matrix_2P[i][j] = 0

    # Erase mino
    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                matrix_2P[x + j][y + i] = 0
# Returns true if mino is at bottom
def is_bottom(x, y, mino, r):
    grid = tetrimino.mino_map[mino - 1][r]

    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                if (y + i + 1) > 20:
                    return True
                elif matrix[x + j][y + i + 1] != 0 and matrix[x + j][y + i + 1] != 8:
                    return True

    return False
def is_bottom_2P(x, y, mino, r):
    grid = tetrimino.mino_map[mino - 1][r]

    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                if (y + i + 1) > 20:
                    return True
                elif matrix_2P[x + j][y + i + 1] != 0 and matrix_2P[x + j][y + i + 1] != 8:
                    return True

    return False
# Returns true if mino is at the left edge
def is_leftedge(x, y, mino, r):
    grid = tetrimino.mino_map[mino - 1][r]

    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                if (x + j - 1) < 0:
                    return True
                elif matrix[x + j - 1][y + i] != 0:
                    return True

    return False
def is_leftedge_2P(x, y, mino, r):
    grid = tetrimino.mino_map[mino - 1][r]

    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                if (x + j - 1) < 0:
                    return True
                elif matrix_2P[x + j - 1][y + i] != 0:
                    return True

    return False
# Returns true if mino is at the right edge
def is_rightedge(x, y, mino, r):
    grid = tetrimino.mino_map[mino - 1][r]

    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                if (x + j + 1) > 9:
                    return True
                elif matrix[x + j + 1][y + i] != 0:
                    return True

    return False
def is_rightedge_2P(x, y, mino, r):
    grid = tetrimino.mino_map[mino - 1][r]

    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                if (x + j + 1) > 9:
                    return True
                elif matrix_2P[x + j + 1][y + i] != 0:
                    return True

    return False
# Returns true if turning right is possible
def is_turnable_r(x, y, mino, r):
    if r != 3:
        grid = tetrimino.mino_map[mino - 1][r + 1]
    else:
        grid = tetrimino.mino_map[mino - 1][0]

    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                if (x + j) < 0 or (x + j) > 9 or (y + i) < 0 or (y + i) > 20:
                    return False
                elif matrix[x + j][y + i] != 0:
                    return False

    return True
def is_turnable_r_2P(x, y, mino, r):
    if r != 3:
        grid = tetrimino.mino_map[mino - 1][r + 1]
    else:
        grid = tetrimino.mino_map[mino - 1][0]

    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                if (x + j) < 0 or (x + j) > 9 or (y + i) < 0 or (y + i) > 20:
                    return False
                elif matrix_2P[x + j][y + i] != 0:
                    return False

    return True
# Returns true if turning left is possible
def is_turnable_l(x, y, mino, r):
    if r != 0:
        grid = tetrimino.mino_map[mino - 1][r - 1]
    else:
        grid = tetrimino.mino_map[mino - 1][3]

    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                if (x + j) < 0 or (x + j) > 9 or (y + i) < 0 or (y + i) > 20:
                    return False
                elif matrix[x + j][y + i] != 0:
                    return False

    return True
def is_turnable_l(x, y, mino, r):
    if r != 0:
        grid = tetrimino.mino_map[mino - 1][r - 1]
    else:
        grid = tetrimino.mino_map[mino - 1][3]

    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                if (x + j) < 0 or (x + j) > 9 or (y + i) < 0 or (y + i) > 20:
                    return False
                elif matrix[x + j][y + i] != 0:
                    return False

    return True
# Returns true if new block is drawable
def is_stackable(mino):
    grid = tetrimino.mino_map[mino - 1][0]

    for i in range(4):
        for j in range(4):
            #print(grid[i][j], matrix[3 + j][i])
            if grid[i][j] != 0 and matrix[3 + j][i] != 0:
                return False

    return True
def is_stackable_2P(mino):
    grid = tetrimino.mino_map[mino - 1][0]

    for i in range(4):
        for j in range(4):
            #print(grid[i][j], matrix[3 + j][i])
            if grid[i][j] != 0 and matrix_2P[3 + j][i] != 0:
                return False

    return True

def draw_multiboard(next_1P,hold_1P,next_2P,hold_2P,score,level,goal):
    screen.fill(ui_variables.real_white)
    draw_1Pboard(next_1P,hold_1P,score,level,goal)
    draw_2Pboard(next_2P,hold_2P,score,level,goal)


# Initial values
blink = False
start = False
pause = False
done = False
game_over = False
leader_board = False
setting = False
pvp = False
help = False

score = 0
level = 1
goal = level * 5
bottom_count = 0
hard_drop = False




dx, dy = 3, 0 # Minos location status

rotation = 0 # Minos rotation status


mino = randint(1, 7) # Current mino

next_mino = randint(1, 7) # Next mino


hold = False # Hold status

hold_mino = -1 # Holded mino


hold_mino_2P = -1
bottom_count_2P = 0
hard_drop_2P = False
hold_2P = False
next_mino_2P = randint(1,7)
mino_2P = randint(1,7)
rotation_2P = 0
dx_2P , dy_2P = 3, 0

name_location = 0
name = [65, 65, 65]



with open('leaderboard.txt') as f:
    lines = f.readlines()
lines = [line.rstrip('\n') for line in open('leaderboard.txt')]

leaders = {'AAA': 0, 'BBB': 0, 'CCC': 0}
for i in lines:
    leaders[i.split(' ')[0]] = int(i.split(' ')[1])
leaders = sorted(leaders.items(), key=operator.itemgetter(1), reverse=True)

matrix = [[0 for y in range(height + 1)] for x in range(width)] # Board matrix

matrix_2P = [[0 for y in range(height + 1)] for x in range(width)] # Board matrix

###########################################################
# Loop Start
###########################################################

while not done:
    # Pause screen
    if setting :
        draw_image(screen,background_image,0,0,board_width,board_height)
        single_button.draw(screen,(0,0,0))
        pvp_button.draw(screen,(0,0,0))
        help_button.draw(screen,(0,0,0))
        quit_button.draw(screen,(0,0,0))
        setting_icon.draw(screen,(0,0,0))
        leaderboard_icon.draw(screen,(0,0,0))

        if start:
            screen.fill(ui_variables.real_white)

            draw_board(next_mino, hold_mino, score, level, goal)


        draw_image(screen,setting_board_image, board_width*0.15, 0, int(board_height*1.3), board_height)
        
        keyboard_icon.draw(screen,(0,0,0))
        screen_icon.draw(screen,(0,0,0))
        volume_icon.draw(screen,(0,0,0))

        back_button.draw(screen,(0,0,0))




        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == QUIT:
                done = True
            elif event.type == USEREVENT:
                pygame.time.set_timer(pygame.USEREVENT, 300)
                
                pause_text = ui_variables.h2_b.render("PAUSED", 1, ui_variables.real_white)
                pause_start = ui_variables.h5.render("Press esc to continue", 1, ui_variables.real_white)

              

                pygame.display.update()
            
            elif event.type == pygame.MOUSEMOTION:
                if back_button.isOver(pos):
                    back_button.image = clicked_back_button_image
                else :
                    back_button.image = back_button_image

                if volume_icon.isOver(pos):
                    volume_icon.image = clicked_volume_vector
                else :
                    volume_icon.image = volume_vector

                if keyboard_icon.isOver(pos):
                    keyboard_icon.image = clicked_keyboard_vector
                else :
                    keyboard_icon.image = keyboard_vector

                if screen_icon.isOver(pos):
                    screen_icon.image = clicked_screen_vector
                else :
                    screen_icon.image = screen_vector



                pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.isOver(pos):
                    ui_variables.click_sound.play()
                    setting = False

                if volume_icon.isOver(pos):
                    ui_variables.click_sound.play()


                if keyboard_icon.isOver(pos):
                    ui_variables.click_sound.play()
                    
                if screen_icon.isOver(pos):
                    ui_variables.click_sound.play()
                    
    elif pause:
        #screen.fill(ui_variables.real_white)
        #draw_board(next_mino, hold_mino, score, level, goal)
        draw_image(screen ,pause_board_image, board_width*0.3, 0, int(board_height*0.7428), board_height)
        resume_button.draw(screen,(0,0,0))
        restart_button.draw(screen,(0,0,0))
        setting_button.draw(screen,(0,0,0))
        pause_quit_button.draw(screen,(0,0,0))
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == QUIT:
                done = True
            elif event.type == USEREVENT:
                pygame.time.set_timer(pygame.USEREVENT, 300)
                
                pause_text = ui_variables.h2_b.render("PAUSED", 1, ui_variables.real_white)
                pause_start = ui_variables.h5.render("Press esc to continue", 1, ui_variables.real_white)

                

                pygame.display.update()
            elif event.type == KEYDOWN:
                erase_mino(dx, dy, mino, rotation)
                if event.key == K_ESCAPE:
                    pause = False
                    ui_variables.click_sound.play()
                    pygame.time.set_timer(pygame.USEREVENT, 1)
            elif event.type == pygame.MOUSEMOTION:
                if resume_button.isOver(pos):
                    resume_button.image = clicked_resume_button_image
                else :
                    resume_button.image = resume_button_image


                if restart_button.isOver(pos):
                    restart_button.image = clicked_restart_button_image
                else :
                    restart_button.image = restart_button_image

                if setting_button.isOver(pos):
                    setting_button.image = clicked_setting_button_image
                else :
                    setting_button.image = setting_button_image
                if pause_quit_button.isOver(pos):
                    pause_quit_button.image = clicked_quit_button_image
                else :
                    pause_quit_button.image = quit_button_image
                pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pause_quit_button.isOver(pos):
                    ui_variables.click_sound.play()
                    done=True
                if setting_button.isOver(pos):
                    ui_variables.click_sound.play()
                    setting = True
                if restart_button.isOver(pos):
                    ui_variables.click_sound.play()
                    hold = False
                    dx, dy = 3, 0
                    rotation = 0
                    mino = randint(1, 7)
                    next_mino = randint(1, 7)
                    hold_mino = -1
                    framerate = 30
                    score = 0
                    score = 0
                    level = 1
                    goal = level * 5
                    bottom_count = 0
                    hard_drop = False
                    name_location = 0
                    name = [65, 65, 65]
                    matrix = [[0 for y in range(height + 1)] for x in range(width)]

                    pause = False
                    start = False
                    if pvp :
                        pvp=False

                if resume_button.isOver(pos):
                    pause = False
                    ui_variables.click_sound.play()
                    pygame.time.set_timer(pygame.USEREVENT, 1)

    # Game screen
    elif leader_board :
        draw_image(screen,background_image,0,0,board_width,board_height)
        single_button.draw(screen,(0,0,0))
        pvp_button.draw(screen,(0,0,0))
        help_button.draw(screen,(0,0,0))
        quit_button.draw(screen,(0,0,0))
        setting_icon.draw(screen,(0,0,0))
        leaderboard_icon.draw(screen,(0,0,0))
        draw_image(screen,leader_board_image, board_width*0.15, 0, int(board_height*1.3), board_height)
        
        back_button.draw(screen,(0,0,0))

        leader_1 = ui_variables.h1_b.render('1st ' + leaders[0][0] + ' ' + str(leaders[0][1]), 1, ui_variables.grey_1)
        leader_2 = ui_variables.h1_b.render('2nd ' + leaders[1][0] + ' ' + str(leaders[1][1]), 1, ui_variables.grey_1)
        leader_3 = ui_variables.h1_b.render('3rd ' + leaders[2][0] + ' ' + str(leaders[2][1]), 1, ui_variables.grey_1)
        screen.blit(leader_1, (board_width*0.3, board_height*0.15))
        screen.blit(leader_2, (board_width*0.3, board_height*0.35))
        screen.blit(leader_3, (board_width*0.3, board_height*0.55))



        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == QUIT:
                done = True
            elif event.type == USEREVENT:
                pygame.time.set_timer(pygame.USEREVENT, 300)
                
                pause_text = ui_variables.h2_b.render("PAUSED", 1, ui_variables.real_white)
                pause_start = ui_variables.h5.render("Press esc to continue", 1, ui_variables.real_white)

              

                pygame.display.update()
            elif event.type == KEYDOWN:
                erase_mino(dx, dy, mino, rotation)
                if event.key == K_ESCAPE:
                    pause = False
                    ui_variables.click_sound.play()
                    pygame.time.set_timer(pygame.USEREVENT, 1)
            elif event.type == pygame.MOUSEMOTION:
                if back_button.isOver(pos):
                    back_button.image = clicked_back_button_image
                else :
                    back_button.image = back_button_image
                pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.isOver(pos):
                    ui_variables.click_sound.play()
                    leader_board=False
                
    
                
    elif start:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == USEREVENT:
                # Set speed
                if not game_over:
                    keys_pressed = pygame.key.get_pressed()
                    if keys_pressed[K_DOWN]:
                        pygame.time.set_timer(pygame.USEREVENT, framerate * 1)
                    else:
                        pygame.time.set_timer(pygame.USEREVENT, framerate * 10)

                # Draw a mino
                draw_mino(dx, dy, mino, rotation)
                screen.fill(ui_variables.real_white)

                draw_board(next_mino, hold_mino, score, level, goal)

                # Erase a mino
                if not game_over:
                    erase_mino(dx, dy, mino, rotation)

                # Move mino down
                if not is_bottom(dx, dy, mino, rotation):
                    dy += 1

                # Create new mino
                else:
                    if hard_drop or bottom_count == 6:
                        hard_drop = False
                        bottom_count = 0
                        score += 10 * level
                        draw_mino(dx, dy, mino, rotation)
                        screen.fill(ui_variables.real_white)
                        draw_board(next_mino, hold_mino, score, level, goal)
                        if is_stackable(next_mino):
                            mino = next_mino
                            next_mino = randint(1, 7)
                            dx, dy = 3, 0
                            rotation = 0
                            hold = False
                        else:
                            start = False
                            game_over = True
                            pygame.time.set_timer(pygame.USEREVENT, 1)
                    else:
                        bottom_count += 1

                # Erase line
                erase_count = 0
                for j in range(21):
                    is_full = True
                    for i in range(10):
                        if matrix[i][j] == 0:
                            is_full = False
                    if is_full:
                        erase_count += 1
                        k = j
                        while k > 0:
                            for i in range(10):
                                matrix[i][k] = matrix[i][k - 1]
                            k -= 1
                if erase_count == 1:
                    ui_variables.single_sound.play()
                    score += 50 * level
                elif erase_count == 2:
                    ui_variables.double_sound.play()
                    score += 150 * level
                elif erase_count == 3:
                    ui_variables.triple_sound.play()
                    score += 350 * level
                elif erase_count == 4:
                    ui_variables.tetris_sound.play()
                    score += 1000 * level

                # Increase level
                goal -= erase_count
                if goal < 1 and level < 15:
                    level += 1
                    goal += level * 5
                    framerate = int(framerate * 0.8)

            elif event.type == KEYDOWN:
                erase_mino(dx, dy, mino, rotation)
                if event.key == K_ESCAPE:
                    ui_variables.click_sound.play()
                    pause = True
                # Hard drop
                elif event.key == K_SPACE:
                    ui_variables.drop_sound.play()
                    while not is_bottom(dx, dy, mino, rotation):
                        dy += 1
                    hard_drop = True
                    pygame.time.set_timer(pygame.USEREVENT, 1)
                    draw_mino(dx, dy, mino, rotation)
                    screen.fill(ui_variables.real_white)
                    draw_board(next_mino, hold_mino, score, level, goal)
                # Hold
                elif event.key == K_LSHIFT or event.key == K_c:
                    if hold == False:
                        ui_variables.move_sound.play()
                        if hold_mino == -1:
                            hold_mino = mino
                            mino = next_mino
                            next_mino = randint(1, 7)
                        else:
                            hold_mino, mino = mino, hold_mino
                        dx, dy = 3, 0
                        rotation = 0
                        hold = True
                    draw_mino(dx, dy, mino, rotation)
                    screen.fill(ui_variables.real_white)
                    draw_board(next_mino, hold_mino, score, level, goal)
                # Turn right
                elif event.key == K_UP or event.key == K_x:
                    if is_turnable_r(dx, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        rotation += 1
                    # Kick
                    elif is_turnable_r(dx, dy - 1, mino, rotation):
                        ui_variables.move_sound.play()
                        dy -= 1
                        rotation += 1
                    elif is_turnable_r(dx + 1, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        dx += 1
                        rotation += 1
                    elif is_turnable_r(dx - 1, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        dx -= 1
                        rotation += 1
                    elif is_turnable_r(dx, dy - 2, mino, rotation):
                        ui_variables.move_sound.play()
                        dy -= 2
                        rotation += 1
                    elif is_turnable_r(dx + 2, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        dx += 2
                        rotation += 1
                    elif is_turnable_r(dx - 2, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        dx -= 2
                        rotation += 1
                    if rotation == 4:
                        rotation = 0
                    draw_mino(dx, dy, mino, rotation)
                    screen.fill(ui_variables.real_white)
                    draw_board(next_mino, hold_mino, score, level, goal)
                # Turn left
                elif event.key == K_z or event.key == K_LCTRL:
                    if is_turnable_l(dx, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        rotation -= 1
                    # Kick
                    elif is_turnable_l(dx, dy - 1, mino, rotation):
                        ui_variables.move_sound.play()
                        dy -= 1
                        rotation -= 1
                    elif is_turnable_l(dx + 1, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        dx += 1
                        rotation -= 1
                    elif is_turnable_l(dx - 1, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        dx -= 1
                        rotation -= 1
                    elif is_turnable_l(dx, dy - 2, mino, rotation):
                        ui_variables.move_sound.play()
                        dy -= 2
                        rotation += 1
                    elif is_turnable_l(dx + 2, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        dx += 2
                        rotation += 1
                    elif is_turnable_l(dx - 2, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        dx -= 2
                    if rotation == -1:
                        rotation = 3
                    draw_mino(dx, dy, mino, rotation)
                    screen.fill(ui_variables.real_white)
                    draw_board(next_mino, hold_mino, score, level, goal)
                # Move left
                elif event.key == K_LEFT:
                    if not is_leftedge(dx, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        dx -= 1
                    draw_mino(dx, dy, mino, rotation)
                    screen.fill(ui_variables.real_white)
                    draw_board(next_mino, hold_mino, score, level, goal)
                # Move right
                elif event.key == K_RIGHT:
                    if not is_rightedge(dx, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        dx += 1
                    draw_mino(dx, dy, mino, rotation)
                    screen.fill(ui_variables.real_white)
                    draw_board(next_mino, hold_mino, score, level, goal)

        pygame.display.update()
    elif pvp :
        for event in pygame.event.get():
            #event.key = pygame.key.get_pressed()
            if event.type == QUIT:
                done = True
            elif event.type == USEREVENT:
                # Set speed
                if not game_over:
                    keys_pressed = pygame.key.get_pressed()
                    if keys_pressed[K_DOWN]:
                        pygame.time.set_timer(pygame.USEREVENT, framerate * 1)
                    else:
                        pygame.time.set_timer(pygame.USEREVENT, framerate * 20)

                # Draw a mino
                draw_mino(dx, dy, mino, rotation)

                draw_mino_2P(dx_2P,dy_2P,mino_2P,rotation_2P)

                draw_multiboard(next_mino,hold_mino,next_mino_2P,hold_mino_2P,score,level,goal)

                # Erase a mino
                if not game_over:
                    erase_mino(dx, dy, mino, rotation)
                    erase_mino_2P(dx_2P, dy_2P, mino_2P, rotation_2P)


                # Move mino down
                if not is_bottom(dx, dy, mino, rotation):
                    dy += 1

                # Create new mino
                else:
                    if hard_drop or bottom_count == 6:
                        hard_drop = False
                        bottom_count = 0
                        score += 10 * level
                        draw_mino(dx, dy, mino, rotation)
                        

                        if is_stackable(next_mino):
                            mino = next_mino
                            next_mino = randint(1, 7)
                            dx, dy = 3, 0
                            rotation = 0
                            hold = False
                        else: #더이상 쌓을 수 없으면 게임오버
                            pvp = False
                            game_over = True
                            pygame.time.set_timer(pygame.USEREVENT, 1)
                    else:
                        bottom_count += 1


                # Move mino down
                if not is_bottom_2P(dx_2P, dy_2P, mino_2P, rotation_2P):
                    dy_2P += 1

                # Create new mino
                else:
                    if hard_drop_2P or bottom_count_2P == 6:
                        hard_drop_2P = False
                        bottom_count_2P = 0
                        score += 10 * level
                        draw_mino_2P(dx_2P, dy_2P, mino_2P, rotation_2P)

                        if is_stackable_2P(next_mino_2P):
                            mino_2P = next_mino_2P
                            next_mino_2P = randint(1, 7)
                            dx_2P, dy_2P = 3, 0
                            rotation_2P = 0
                            hold_2P = False
                        else: #더이상 쌓을 수 없으면 게임오버
                            pvp = False
                            game_over = True
                            pygame.time.set_timer(pygame.USEREVENT, 1)
                    else:
                        bottom_count_2P += 1

                # Erase line
                # 콤보 카운트 
                erase_count = 0
                erase_count_2P = 0
                combo_value = 0
                sent = 0

                for j in range(21):
                    is_full = True
                    for i in range(10):
                        if matrix[i][j] == 0:
                            is_full = False
                    if is_full:
                        erase_count += 1
                        k = j
                        combo_value += 1
                        while k > 0:
                            for i in range(10):
                                matrix[i][k] = matrix[i][k - 1]
                            k -= 1
                for j in range(21):
                    is_full = True
                    for i in range(10):
                        if matrix_2P[i][j] == 0:
                            is_full = False
                    if is_full:
                        erase_count_2P += 1
                        k = j
                        combo_value += 1
                        while k > 0:
                            for i in range(10):
                                matrix_2P[i][k] = matrix_2P[i][k - 1]
                            k -= 1

                # 지운 블록이 없으면 콤보 -1
                #if erase_count == 0 :
                    #combo_count -= 1
                    #if combo_count < 0:
                        #combo_count = 0

                if erase_count >= 1:
                    #combo_count += 1
                    if erase_count == 1:
                        #ui_variables.break_sound.play()
                        ui_variables.single_sound.play()
                        score += 50 * level * erase_count 
                    elif erase_count == 2:
                        #ui_variables.break_sound.play()
                        ui_variables.double_sound.play()
                        score += 150 * level * erase_count + 2 
                        
                    elif erase_count == 3:
                        #ui_variables.break_sound.play()
                        ui_variables.triple_sound.play()
                        ui_variables.triple_sound.play()
                        score += 350 * level * erase_count + 3 
                    elif erase_count == 4:
                        #ui_variables.break_sound.play()
                        ui_variables.tetris_sound.play()
                        ui_variables.tetris_sound.play()
                        score += 1000 * level * erase_count + 4 

                #    for i in range(1, 11) :
                #        if combo_count == i :  # 1 ~ 10 콤보 이미지
                #            screen.blit(ui_variables.large_combos[i-1], (124, 190))  # blits the combo number
                #        elif combo_count > 10 : # 11 이상 콤보 이미지
                #            screen.blit(tetris4, (100, 190))  # blits the combo number

                #    for i in range(1, 10) :
                #        if combo_count == i+2 : # 3 ~ 11 콤보 사운드
                #            ui_variables.combos_sound[i-1].play()


                #sent = checkCombo(combo_count, sent)  # 콤보 증가

                # Increase level
                goal -= erase_count
                if goal < 1 and level < 15:
                    level += 1
                    
                    goal += level * 5
                    framerate = int(framerate * 0.8)

            elif event.type == KEYDOWN:                                 ##중요
                erase_mino(dx, dy, mino, rotation)
                erase_mino_2P(dx_2P, dy_2P, mino_2P, rotation_2P)

                
                if event.key == K_ESCAPE:
                    ui_variables.click_sound.play()
                    pause = True
                # Hard drop
                elif event.key == K_SPACE: 
                    #ui_variables.fall_sound.play()
                    #ui_variables.drop_sound.play()
                    while not is_bottom(dx, dy, mino, rotation):
                        dy += 1
                    hard_drop = True
                    pygame.time.set_timer(pygame.USEREVENT, 1)
                    draw_mino(dx, dy, mino, rotation)
                    #draw_mino_2P(dx_2P,dy_2P,mino_2P,rotation_2P)
                    #draw_multiboard(next_mino,hold_mino,next_mino_2P,hold_mino_2P,score,level,goal)
                elif event.key == K_f:
                    #ui_variables.fall_sound.play()
                    #ui_variables.drop_sound.play()
                    while not is_bottom_2P(dx_2P, dy_2P, mino_2P, rotation_2P):
                        dy_2P += 1
                    hard_drop_2P = True
                    pygame.time.set_timer(pygame.USEREVENT, 1)
                    draw_mino_2P(dx_2P, dy_2P, mino_2P, rotation_2P)
                    #draw_mino(dx, dy, mino, rotation)
                    #draw_multiboard(next_mino,hold_mino,next_mino_2P,hold_mino_2P,score,level,goal)
                # Hold
                elif event.key == K_LSHIFT :
                    if hold == False:
                        ui_variables.move_sound.play()
                        if hold_mino == -1:
                            hold_mino = mino
                            mino = next_mino
                            next_mino = randint(1, 7)
                        else:
                            hold_mino, mino = mino, hold_mino
                        dx, dy = 3, 0
                        rotation = 0
                        hold = True
                    draw_mino(dx, dy, mino, rotation)
                    draw_mino_2P(dx_2P, dy_2P, mino_2P, rotation_2P)
                    draw_multiboard(next_mino,hold_mino,next_mino_2P,hold_mino_2P,score,level,goal)
                elif event.key == K_c :
                    if hold_2P == False:
                        ui_variables.move_sound.play()
                        if hold_mino_2P == -1:
                            hold_mino_2P = mino_2P
                            mino_2P = next_mino_2P
                            next_mino_2P = randint(1, 7)
                        else:
                            hold_mino_2P, mino_2P = mino_2P, hold_mino_2P
                        dx_2P, dy_2P = 3, 0
                        rotation_2P = 0
                        hold_2P = True
                    draw_mino_2P(dx_2P, dy_2P, mino_2P, rotation_2P)
                    draw_mino(dx, dy, mino, rotation)
                    draw_multiboard(next_mino,hold_mino,next_mino_2P,hold_mino_2P,score,level,goal)
                # Turn right
                elif event.key == K_UP :
                    if is_turnable_r(dx, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        rotation += 1
                    # Kick
                    elif is_turnable_r(dx, dy - 1, mino, rotation):
                        ui_variables.move_sound.play()
                        dy -= 1
                        rotation += 1
                    elif is_turnable_r(dx + 1, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        dx += 1
                        rotation += 1
                    elif is_turnable_r(dx - 1, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        dx -= 1
                        rotation += 1
                    elif is_turnable_r(dx, dy - 2, mino, rotation):
                        ui_variables.move_sound.play()
                        dy -= 2
                        rotation += 1
                    elif is_turnable_r(dx + 2, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        dx += 2
                        rotation += 1
                    elif is_turnable_r(dx - 2, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        dx -= 2
                        rotation += 1
                    if rotation == 4:
                        rotation = 0
                    draw_mino(dx, dy, mino, rotation)
                    draw_mino_2P(dx_2P, dy_2P, mino_2P, rotation_2P)
                    draw_multiboard(next_mino,hold_mino,next_mino_2P,hold_mino_2P,score,level,goal)
                elif event.key == K_x:
                    if is_turnable_r(dx_2P, dy_2P, mino_2P, rotation_2P):
                        ui_variables.move_sound.play()
                        rotation_2P += 1
                    # Kick
                    elif is_turnable_r(dx_2P, dy_2P - 1, mino_2P, rotation_2P):
                        ui_variables.move_sound.play()
                        dy_2P -= 1
                        rotation_2P += 1
                    elif is_turnable_r(dx_2P + 1, dy_2P, mino_2P, rotation_2P):
                        ui_variables.move_sound.play()
                        dx_2P += 1
                        rotation_2P += 1
                    elif is_turnable_r(dx_2P - 1, dy_2P, mino_2P, rotation_2P):
                        ui_variables.move_sound.play()
                        dx_2P -= 1
                        rotation_2P += 1
                    elif is_turnable_r(dx_2P, dy_2P - 2, mino_2P, rotation_2P):
                        ui_variables.move_sound.play()
                        dy_2P -= 2
                        rotation_2P += 1
                    elif is_turnable_r(dx_2P + 2, dy_2P, mino_2P, rotation_2P):
                        ui_variables.move_sound.play()
                        dx_2P += 2
                        rotation_2P += 1
                    elif is_turnable_r(dx_2P - 2, dy_2P, mino_2P, rotation_2P):
                        ui_variables.move_sound.play()
                        dx_2P -= 2
                        rotation_2P += 1
                    if rotation_2P == 4:
                        rotation_2P = 0
                    draw_mino_2P(dx_2P, dy_2P, mino_2P, rotation_2P)
                    draw_mino(dx, dy, mino, rotation)
                    draw_multiboard(next_mino,hold_mino,next_mino_2P,hold_mino_2P,score,level,goal)
                # Turn left
                elif event.key == K_z or event.key == K_LCTRL:
                    if is_turnable_l(dx, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        rotation -= 1
                    # Kick
                    elif is_turnable_l(dx, dy - 1, mino, rotation):
                        ui_variables.move_sound.play()
                        dy -= 1
                        rotation -= 1
                    elif is_turnable_l(dx + 1, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        dx += 1
                        rotation -= 1
                    elif is_turnable_l(dx - 1, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        dx -= 1
                        rotation -= 1
                    elif is_turnable_l(dx, dy - 2, mino, rotation):
                        ui_variables.move_sound.play()
                        dy -= 2
                        rotation += 1
                    elif is_turnable_l(dx + 2, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        dx += 2
                        rotation += 1
                    elif is_turnable_l(dx - 2, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        dx -= 2
                    if rotation == -1:
                        rotation = 3
                    draw_mino(dx, dy, mino, rotation)
                    draw_mino_2P(dx_2P, dy_2P, mino_2P, rotation_2P)
                    draw_multiboard(next_mino,hold_mino,next_mino_2P,hold_mino_2P,score,level,goal)
                # Move left
                elif event.key == K_LEFT :                     # key = pygame.key.get_pressed()
                    if not is_leftedge(dx, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        keys_pressed = pygame.key.get_pressed()
                        pygame.time.set_timer(pygame.KEYUP, framerate * 3)
                        dx -= 1
                    draw_mino(dx, dy, mino, rotation)
                    draw_mino_2P(dx_2P, dy_2P, mino_2P, rotation_2P)
                    draw_multiboard(next_mino,hold_mino,next_mino_2P,hold_mino_2P,score,level,goal)
                # Move right
                elif event.key == K_RIGHT :
                    if not is_rightedge(dx, dy, mino, rotation):
                        ui_variables.move_sound.play()
                        keys_pressed = pygame.key.get_pressed()
                        pygame.time.set_timer(pygame.KEYUP, framerate * 3)
                        dx += 1
                    draw_mino(dx, dy, mino, rotation)
                    draw_mino_2P(dx_2P, dy_2P, mino_2P, rotation_2P)
                    draw_multiboard(next_mino,hold_mino,next_mino_2P,hold_mino_2P,score,level,goal)
                elif event.key == K_a :                     # key = pygame.key.get_pressed()
                    if not is_leftedge_2P(dx_2P, dy_2P, mino_2P, rotation_2P):
                        ui_variables.move_sound.play()
                        keys_pressed = pygame.key.get_pressed()
                        pygame.time.set_timer(pygame.KEYUP, framerate * 3)
                        dx_2P -= 1
                    draw_mino_2P(dx_2P, dy_2P, mino_2P, rotation_2P)
                    draw_mino(dx, dy, mino, rotation)
                    draw_multiboard(next_mino,hold_mino,next_mino_2P,hold_mino_2P,score,level,goal)
                # Move right
                elif event.key == K_d :
                    if not is_rightedge_2P(dx_2P, dy_2P, mino_2P, rotation_2P):
                        ui_variables.move_sound.play()
                        keys_pressed = pygame.key.get_pressed()
                        pygame.time.set_timer(pygame.KEYUP, framerate * 3)
                        dx_2P += 1
                    draw_mino_2P(dx_2P, dy_2P, mino_2P, rotation_2P)
                    draw_mino(dx, dy, mino, rotation)
                    draw_multiboard(next_mino,hold_mino,next_mino_2P,hold_mino_2P,score,level,goal)


                

        #if any(movement_keys.values()):
        #    movement_keys_timer += clock.tick(50)
        
        pygame.display.update()

    # Game over screen
    elif game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == USEREVENT:
                pygame.time.set_timer(pygame.USEREVENT, 300)
                over_text_1 = ui_variables.h2_b.render("GAME", 1, ui_variables.white)
                over_text_2 = ui_variables.h2_b.render("OVER", 1, ui_variables.white)
                over_start = ui_variables.h5.render("Press return to continue", 1, ui_variables.white)
                
                screen.blit(over_text_1, (int(board_width*0.1933), int(board_height*0.2005)))
                screen.blit(over_text_2, (int(board_width*0.2066), int(board_height*0.2807)))

                name_1 = ui_variables.h2_i.render(chr(name[0]), 1, ui_variables.white)
                name_2 = ui_variables.h2_i.render(chr(name[1]), 1, ui_variables.white)
                name_3 = ui_variables.h2_i.render(chr(name[2]), 1, ui_variables.white)

                underbar_1 = ui_variables.h2.render("_", 1, ui_variables.white)
                underbar_2 = ui_variables.h2.render("_", 1, ui_variables.white)
                underbar_3 = ui_variables.h2.render("_", 1, ui_variables.white)

                screen.blit(name_1, (int(board_width*0.2166), int(board_height*0.3930)))
                screen.blit(name_2, (int(board_width*0.3166), int(board_height*0.3930)))
                screen.blit(name_3, (int(board_width*0.4166), int(board_height*0.3930)))

                if blink:
                    screen.blit(over_start, (int(board_width*0.1066), int(board_height*0.5213)))
                    blink = False
                else:
                    if name_location == 0:
                        screen.blit(underbar_1, ((int(board_width*0.2166), int(board_height*0.3877))))
                    elif name_location == 1:
                        screen.blit(underbar_2, ((int(board_width*0.3166), int(board_height*0.3877))))
                    elif name_location == 2:
                        screen.blit(underbar_3, ((int(board_width*0.4166), int(board_height*0.3877))))
                    blink = True

                pygame.display.update()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    ui_variables.click_sound.play()

                    outfile = open('leaderboard.txt','a')
                    outfile.write(chr(name[0]) + chr(name[1]) + chr(name[2]) + ' ' + str(score) + '\n')
                    outfile.close()

                    game_over = False
                    hold = False # 
                    dx, dy = 3, 0 #
                    rotation = 0 #
                    mino = randint(1, 7) #
                    next_mino = randint(1, 7) #
                    hold_mino = -1 #
                    framerate = 30
                    score = 0
                    score = 0
                    level = 1
                    goal = level * 5
                    bottom_count = 0 #
                    hard_drop = False #
                    name_location = 0
                    name = [65, 65, 65]
                    matrix = [[0 for y in range(height + 1)] for x in range(width)]

                    hold_mino_2P = -1 #
                    bottom_count_2P = 0 #
                    hard_drop_2P = False #
                    hold_2P = False #
                    next_mino_2P = randint(1,7) #
                    mino_2P = randint(1,7) #
                    rotation_2P = 0  #
                    dx_2P , dy_2P = 3, 0 #
                    matrix_2P = [[0 for y in range(height + 1)] for x in range(width)] # Board matrix


                    with open('leaderboard.txt') as f:
                        lines = f.readlines()
                    lines = [line.rstrip('\n') for line in open('leaderboard.txt')]

                    leaders = {'AAA': 0, 'BBB': 0, 'CCC': 0}
                    for i in lines:
                        leaders[i.split(' ')[0]] = int(i.split(' ')[1])
                    leaders = sorted(leaders.items(), key=operator.itemgetter(1), reverse=True)

                    pygame.time.set_timer(pygame.USEREVENT, 1)
                elif event.key == K_RIGHT:
                    if name_location != 2:
                        name_location += 1
                    else:
                        name_location = 0
                    pygame.time.set_timer(pygame.USEREVENT, 1)
                elif event.key == K_LEFT:
                    if name_location != 0:
                        name_location -= 1
                    else:
                        name_location = 2
                    pygame.time.set_timer(pygame.USEREVENT, 1)
                elif event.key == K_UP:
                    ui_variables.click_sound.play()
                    if name[name_location] != 90:
                        name[name_location] += 1
                    else:
                        name[name_location] = 65
                    pygame.time.set_timer(pygame.USEREVENT, 1)
                elif event.key == K_DOWN:
                    ui_variables.click_sound.play()
                    if name[name_location] != 65:
                        name[name_location] -= 1
                    else:
                        name[name_location] = 90
                    pygame.time.set_timer(pygame.USEREVENT, 1)

    # Start screen
    else:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == QUIT:
                done = True
            elif event.type == USEREVENT:
                pygame.time.set_timer(pygame.USEREVENT, 300)

            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    ui_variables.click_sound.play()
                    start = True
            elif event.type == pygame.MOUSEMOTION:
                if single_button.isOver(pos):
                    single_button.image = clicked_single_button_image
                else :
                    single_button.image = single_button_image


                if pvp_button.isOver(pos):
                    pvp_button.image = clicked_pvp_button_image
                else :
                    pvp_button.image = pvp_button_image

                if help_button.isOver(pos):
                    help_button.image = clicked_help_button_image
                else :
                    help_button.image = help_button_image

                if quit_button.isOver(pos):
                    quit_button.image = clicked_quit_button_image
                else :
                    quit_button.image = quit_button_image

                if setting_icon.isOver(pos):
                    setting_icon.image = clicked_setting_vector
                else :
                    setting_icon.image = setting_vector

                if leaderboard_icon.isOver(pos):
                    leaderboard_icon.image = clicked_leaderboard_vector
                else :
                    leaderboard_icon.image = leaderboard_vector
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if single_button.isOver(pos):
                    ui_variables.click_sound.play()
                    start = True
                if pvp_button.isOver(pos):
                    ui_variables.click_sound.play()
                    pvp = True
                if leaderboard_icon.isOver(pos):
                    ui_variables.click_sound.play()
                    leader_board = True
                if setting_icon.isOver(pos):
                    ui_variables.click_sound.play()
                    setting = True
                if quit_button.isOver(pos):
                    ui_variables.click_sound.play()
                    done = True
                if help_button.isOver(pos):
                    ui_variables.click_sound.play()
                    help = True




        screen.fill(ui_variables.white)
        
        draw_image(screen,background_image,0,0,board_width,board_height)
        
        single_button.draw(screen,(0,0,0))
        pvp_button.draw(screen,(0,0,0))
        help_button.draw(screen,(0,0,0))
        quit_button.draw(screen,(0,0,0))

        setting_icon.draw(screen,(0,0,0))
        leaderboard_icon.draw(screen,(0,0,0))


        if not start:
            pygame.display.update()
            clock.tick(3)

pygame.quit()