import pygame 
import random

pygame.init()

SPRITE_COLOUR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOUR_CHANGE_EVENT = pygame.USEREVENT + 2
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.color('lightblue')
DARKBLUE = pygame.color('Darkblue')
MAROON =  pygame.color('maroon')
MAGENTA =pygame.color('magenta')
CORAL = pygame.color('coral')
BLACK =pygame.color('black ')

class sprite(pygame.sprite.Sprite):

    def __init__(self, colour , height , width)