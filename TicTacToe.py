from tkinter import EventType
import pygame
from pygame.locals import *
import sys
import random
pygame.init()
run = True
screen_with = 600
screen_height = 600
screen = pygame.display.set_mode((screen_height,screen_with))
pygame.display.set_caption('TicTacToe')
line_with = 6
markers = []
clicked = False
pos = []
player = 1
yeþil = (0,255,0)
kýrmýzý = (255,0,0)
mavi = (0,0,255)
beyaz = (255,255,255)
siyah = (0,0,0)
lacivert = (7,19,48)
font = pygame.font.SysFont("arial",20)
winner = 0
game_over = False
again_rect = Rect(screen_with // 2 -102, screen_height // 2 + 10 , 206 ,50)

def draw_grid():
    bg = (255,200,102)
    grid = (0,0,0)
    screen.fill(bg)
    for x in range(1,3):
        pygame.draw.line(screen, grid,(0,x*200),(screen_with,x*200),line_with)
        pygame.draw.line(screen, grid,(x*200,0),(x*200,screen_height),line_with)


for x in range(3):
    row = [0]*3
    markers.append(row)

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen,yeþil,(x_pos*200+15,y_pos*200+15),(x_pos*200+185,y_pos*200+185),line_with)
                pygame.draw.line(screen,yeþil,(x_pos*200+15,y_pos*200+185),(x_pos*200+185,y_pos*200+15),line_with)
            if y == -1:
                pygame.draw.circle(screen,kýrmýzý,(x_pos*200+100,y_pos*200+100),76,line_with)    
            y_pos += 1
        x_pos += 1
def check_winner():
    y_pos = 0
    global winner
    global game_over
    for x in markers:
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        game_over = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 2
        game_over = True
    if markers[0][0] != 0 and markers[0][1] != 0 and markers[0][2] != 0 and markers[1][0] != 0 and markers[1][1] != 0 and markers[1][2] != 0 and markers[2][0] != 0 and markers[2][1] != 0 and markers[2][2] != 0 :
        winner = 0
        game_over = True
def draw_winner(winner):
    if winner == 0:
        win_text = "No one Wins !!!"
        win_img = font.render(win_text,True,mavi)
        pygame.draw.rect(screen,yeþil,(screen_with // 2 - 102, screen_height // 2 -50,206,50))
        screen.blit(win_img,(screen_with // 2 - 55, screen_height // 2 - 37))
    if winner != 0:
        win_text = 'Player '+ str(winner) + " Wins !!!"
        win_img = font.render(win_text,True,mavi)
        pygame.draw.rect(screen,yeþil,(screen_with // 2 - 102, screen_height // 2 -50,206,50))
        screen.blit(win_img,(screen_with // 2 - 55, screen_height // 2 - 37))

    again_text = 'Play Again ?'
    again_img = font.render(again_text,True,mavi)
    pygame.draw.rect(screen,kýrmýzý,again_rect)
    screen.blit(again_img,(screen_with // 2 -40, screen_height // 2 + 22))
while run:
    draw_grid()
    draw_markers()

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            sys.exit()
        if game_over == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False  
                pos = pygame.mouse.get_pos()
                pos_x = pos[0]
                pos_y = pos[1]  
                if markers[pos_x//200][pos_y//200] == 0: 
                    markers[pos_x//200][pos_y//200] = player
                    player *= -1
                    check_winner()
                    
    if game_over == True:
        draw_winner(winner)
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False  
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                markers = []
                pos = []
                player = 1
                winner = 0
                game_over = False
                for x in range(3):
                    row = [0]*3
                    markers.append(row)

    pygame.display.update()


pygame.quit()