#!/usr/bin/env python
"""
This is a Python / PyGame version of "Felix and Herbert" for CodeClub
"""

#Import Modules
import pygame, codeclub
from pygame.locals import *

def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
#Initialize Everything
    pygame.init()
    screensize = (800, 600)
    screen = pygame.display.set_mode(screensize)

#create the wallpaper, and make it fill the screen
    wallpaper = codeclub.load_image('hall.jpg')
    wallpaper = pygame.transform.scale(wallpaper, (screensize))
    background = pygame.Surface(screensize)
    background.blit(wallpaper, (0, 0))
    
#Prepare Game Objects
    clock = pygame.time.Clock()
    
#Main Loop
    while True:
        clock.tick(60)

    #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return

    #Draw Everything
        screen.blit(background, (0, 0))
        pygame.display.flip()

#Game Over


#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()
pygame.quit ()

