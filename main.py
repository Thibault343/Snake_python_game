'''
Name: Snake
Description: A simple snake game
Author: Sayte
'''

# Importations
import pygame, sys
# Variables
run = True
width = 800
height = 600
size = (width, height)
green = (0, 255, 0)
snake_position = [100,50]
direction = ["", ""]

# initialize the game
pygame.init()

rect_1 = pygame.Rect(10, 10, 10, 10)


clock = pygame.time.Clock()

# Create the display window
screen = pygame.display.set_mode(size)

# Functions

while run:
    clock.tick(10)

    screen.fill((0, 0, 0))

    key = pygame.key.get_pressed()

    if key[pygame.K_UP] == True:
        direction.append("UP")
    if key[pygame.K_DOWN] == True :
        direction.append("DOWN")
    if key[pygame.K_LEFT] == True :
        direction.append("LEFT")
    if key[pygame.K_RIGHT] == True:
        direction.append("RIGHT")
    if direction[-1] == "UP" :
        rect_1.y -= 10
    if direction[-1] == "DOWN":
        rect_1.y += 10
    if direction[-1] == "LEFT":
        rect_1.x -= 10
    if direction[-1] == "RIGHT":
        rect_1.x += 10
    print(direction[-1])
            
    pygame.draw.rect(screen, green, rect_1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
    pygame.display.flip()
