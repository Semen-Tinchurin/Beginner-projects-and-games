# from tkinter import *
# from tkinter import messagebox
# import time
# import random
#
# tk = Tk()
# app_running = True
#
# size_canvas_x = 768
# size_canvas_y = 768
#
#
# def on_closing():
#     global app_running
#     if messagebox.askokcancel('Quit', 'Do you want to quit?'):
#         app_running = False
#         tk.destroy()
#
#
# tk.protocol("WM_DELETE_WINDOW", on_closing)
#
# tk.title('Tic tac toe')
# tk.resizable(0, 0)
# tk.wm_attributes('-topmost', 1)
# canvas = Canvas(tk, width=size_canvas_x, height=size_canvas_y, bd=0, highlightthickness=0)
# canvas.pack()
# tk.update()
#
# s_x = 3
# s_y = 3
# step_x = size_canvas_x // s_x
# step_y = size_canvas_y // s_y
#
#
# def draw_table():
#     for i in range(0, s_x + 1):
#         canvas.create_line(0, i * step_y, size_canvas_x, i * step_y)
#     for i in range(0, s_y + 1):
#         canvas.create_line(i * step_y, 0, i * step_y, size_canvas_y)
#
#
# points = []
#
# draw_table()
#
#
# class Point:
#     def __init__(self, x, y, type):
#         self.x = x
#         self.y = y
#         self.type = type
#
#     def __str__(self):
#         return str(self.__class__) + ':' + str(self.__dict__)
#
# def draw_point(x, y, type):
#     size = 25
#     color = 'black'
#     id = 0
#     if type == 0:
#         color = 'red'
#         id = canvas.create_oval(x * step_x, y * step_y, x * step_x + step_x, y * step_y + step_y, fill=color)
#         id = canvas.create_oval(x * step_x+size, y * step_y+size, x * step_x + step_x-size, y * step_y + step_y-size, fill='white')
#     if type == 1:
#         color = 'blue'
#
#     #id = canvas.create_oval(x*step_x, y*step_y, x*step_x+step_x, y*step_y+step_y, fill=color)
#     id = canvas.create_oval(x*step_x, y*step_y, x*step_x+step_x, y*step_y+step_y, fill=color)
#
# def add_to_points(event):
#     print(event.num, event.x, event.y)
#     type = 0
#     if event.num == 3:
#         type = 1
#     points.append(Point(event.x // step_x, event.y // step_y, type))
#     draw_point(event.x // step_x, event.y // step_y, type)
#     print(" ".join(map(str, points)))
#
#
# canvas.bind_all('<Button-1>', add_to_points)
# canvas.bind_all('<Button-3>', add_to_points)
#
# while app_running:
#     if app_running:
#         tk.update_idletasks()
#         tk.update()
#     time.sleep(0.005)

import pygame
import sys


def check_win(mas, sign):
    zeroes = 0
    for row in mas:
        zeroes += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if zeroes == 0:
        return 'Piece'
    return False


pygame.init()
size_block = 100
margin = 15
width = heigth = size_block * 3 + margin * 4

size_window = (width, heigth)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption('Tic tac toe')

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
mas = [[0] * 3 for i in range(3)]
query = 0
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = '0'
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query = 0
            screen.fill(black)
    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'x':
                    color = red
                elif mas[row][col] == '0':
                    color = green
                else:
                    color = white
                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == red:
                    pygame.draw.line(screen, white, (x + 10, y + 10), (x + size_block - 10, y + size_block - 10), 3)
                    pygame.draw.line(screen, white, (x + size_block - 10, y + 10), (x + 10, y + size_block - 10), 3)
                elif color == green:
                    pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2 - 7, 3)
    if (query - 1) % 2 == 0:
        game_over = check_win(mas, 'x')
    else:
        game_over = check_win(mas, 'o')

    if game_over:
        screen.fill(black)
        font = pygame.font.SysFont('stxingai', 80)
        text1 = font.render(game_over, True, white)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y])

    pygame.display.update()
