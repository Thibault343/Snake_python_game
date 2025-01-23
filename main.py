'''
Name: Snake
Description: A simple snake game
Author: Sayte
'''

# Importations
import pygame, sys, random
# Variables
run = True
width = 800
height = 600
size = (width, height)
green = (0, 255, 0)
snake_position = [[100,50]]
direction = [""]
fruit_placed = False
fruit_position = [random.randint(0, (width//10) - 1) * 10, random.randint(0, (height//10) - 1) * 10]
rect_1 = pygame.Rect(snake_position[0][0],snake_position[0][1], 10, 10)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake")

# initialize the game
pygame.init()


# Functions

def drawrect():
    for pos in snake_position:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # Define the speed of the game
    clock.tick(10)
    # Fill the screen with black color
    screen.fill((0, 0, 0))
    # Check for the key pressed
    key = pygame.key.get_pressed()  
    if snake_position[0][0] >= width or snake_position[0][0] < 0 or snake_position[0][1] >= height or snake_position[0][1] < 0:
        run = False
    # Check for the direction of the snake
    if key[pygame.K_UP] == True and direction[-1] != "DOWN":
        direction.append("UP")
    if key[pygame.K_DOWN] == True and direction[-1] != "UP":
        direction.append("DOWN")
    if key[pygame.K_LEFT] == True and direction[-1] != "RIGHT": 
        direction.append("LEFT")
    if key[pygame.K_RIGHT] == True and direction[-1] != "LEFT":
        direction.append("RIGHT")

    # Move the snake
    if direction[-1] == "UP" :
        snake_position[0][1] -= 10
    if direction[-1] == "DOWN":
        snake_position[0][1] += 10
    if direction[-1] == "LEFT":
        snake_position[0][0] -= 10
    if direction[-1] == "RIGHT":
        snake_position[0][0] += 10
    print(snake_position)
    # Check if the snake has eaten the fruit
    snake_position.insert(0, list(snake_position[0]))
    if snake_position[0] == fruit_position:
        fruit_placed = False
    else:
        snake_position.pop()

    if fruit_placed == False:
        fruit_position = [random.randint(0, (width//10) - 1) * 10, random.randint(0, (height//10) - 1) * 10]
        fruit_placed = True

    
    drawrect()

    pygame.display.flip()
