import pygame
import random
import time

#Window parameters
window_width = 800
window_height = 600

#snake parameters
block_size = 20
pygame.font.init()
score_font = pygame.font.SysFont("courier", 20)
score = 0

#color define
white = (255, 255, 255)
red = (255, 0, 0)

#initialize pygame
pygame.init()

#set up display
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Python Python Game")

#set up clock
clock = pygame.time.Clock()

#snake and comestibles initialization
snake_position = [[window_width//2, window_height//2]]#list of lists
snake_speed = [0, block_size]
teleport_walls = True #enabled to allow teleporting through walls

#snake comestibles generated

