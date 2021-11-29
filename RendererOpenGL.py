#Universidad del Valle de Guatemala
#Graficas por Computadoras
#Fernando José Garavito Ovando 18071
#Proyecto No. 4

#Import
import pygame
from pygame.locals import *
from gl import Renderer
import shaders
from math import sin, cos

deltaTime = 0.0




def move_up(board):
    for x in range(board.shape[0]):
        for y in range(board.shape[1]):
            if board[x, y] == 1:
                if x > 0:
                    board[x, y] = 0
                    board[x - 1, y] = 1
                    return
                else:
                    print("Movimiento invalido")

def move_down(board):
    for x in range(board.shape[0]):
        for y in range(board.shape[1]):
            if board[x, y] == 1:
                if x < board.shape[0] - 1:
                    board[x, y] = 0
                    board[x + 1, y] = 1
                    return
                else:
                    print("Movimiento invalido")

pygame.init()
clock = pygame.time.Clock()
screensize = (500, 500)
screen = pygame.display.set_mode(screensize, DOUBLEBUF | OPENGL)

r = Renderer(screen)
r.setShaders(shaders.vertex_shader, shaders.fragment_shader)
r.createobjects()

cubo1 = 0
cubo2 = 0
rotar = 0

isRunning = True
while isRunning:

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        cubo1 -= 2 * deltaTime
    if keys[pygame.K_d]:
        cubo1 += 2 * deltaTime
    if keys[pygame.K_w]:
        cubo2 -= 2 * deltaTime
    if keys[pygame.K_s]:
        cubo2 += 2 * deltaTime
    if keys[pygame.K_w]:
        cubo1 -= 2 * deltaTime
    if keys[pygame.K_s]:
        cubo1 += 2 * deltaTime
        
    if keys == pygame.K_UP:
        rotar += 5
    if keys == pygame.K_DOWN:
        rotar -= 5
    if keys == pygame.K_UP:
        rotar += 5
    if keys == pygame.K_DOWN:
        rotar -= 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isRunning = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_1:
                r.filledMode()
            elif ev.key == pygame.K_2:
                r.wireframeMode
            elif ev.key == pygame.K_ESCAPE:
                isRunning = False

    r.translatecube(cubo1, 0, cubo2)

    r.render()
    pygame.display.flip()
    clock.tick(60)
    deltaTime = clock.get_time() / 1000

pygame.quit()
