#!/usr/bin/env python
"""
Extension of the PyGame sprite class and various utilities to simplify the use of PyGame for CodeClub tutorials
"""


#Import Modules
import os, pygame
from pygame.locals import *
from math import sqrt, degrees, atan, cos, sin, radians


#functions to create our resources
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image #, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join('data', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print 'Cannot load sound:', fullname
        raise SystemExit, message
    return sound



class sprite(pygame.sprite.Sprite):
    def __init__(self, x_pos = 100.0, y_pos = 100.0, speed = 4):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        self.posx = x_pos
        self.posy = y_pos
        self.direction = 0;
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect = pygame.Rect(x_pos, y_pos, 10, 10)
        self.speed = speed
        self.freeze_time = 0
        self.speak_time = 0
        self.speak_pos = (0,0)
        self.speak_font = pygame.font.Font(None, 36)
        self.speak_text = self.speak_font.render("Hello!!!", 1, (10, 10, 10))
        self.facing_right = True
        
    def set_costume(self, name, size):
        self.image = load_image(name, -1)
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect.width = self.rect.height = size
        self.facing_right = True
    
    
    def turn_right(self, degrees = 10):
        self.direction += degrees
        
    def turn_left(self, degrees = 10):
        self.direction -= degrees
        
    def point_towards(self, target):
        x_diff = target.rect.left - self.rect.left
        y_diff = target.rect.top - self.rect.top
        
        if (x_diff == 0):
	    if (y_diff <= 0):
	        self.direction = 90
	    else:
	        self.direction = 270
	elif (y_diff == 0):
	    if (x_diff <= 0):
	        self.direction = 0
	    else:
	        self.direction = 180
	else:
	    if (x_diff < 0) and (y_diff < 0):  #Up and left, 0 - 90 degrees
		self.direction = degrees(atan(float(y_diff) / float(x_diff)))
	    if (x_diff > 0) and (y_diff < 0):  #Up and right, 90 - 180 degrees
		self.direction = 90 + degrees(atan(float(x_diff) / float(-y_diff)))
	    if (x_diff > 0) and (y_diff > 0):  #Down and right, 180 - 270 degrees
		self.direction = 180 + degrees(atan(float(y_diff) / float(x_diff)))
	    if (x_diff < 0) and (y_diff > 0):  #Down and left, 270 - 360 degrees
		self.direction = 270 + degrees(atan(float(-x_diff) / float(y_diff)))
	# Now ensure the Sprite is faceing the correct way (look left / right only)	
        if (self.rect.left > target.rect.left) and self.facing_right == True:
            self.facing_right = False
            self.image = pygame.transform.flip(self.image, 1, 0)
        if (self.rect.left < target.rect.left) and self.facing_right == False:
            self.facing_right = True
            self.image = pygame.transform.flip(self.image, 1, 0)

    def move_to(self, pos):
        self.rect.center = pos
            
    def move(self, distance = 1):
	x_diff = -cos(radians(self.direction)) * distance
	y_diff = -sin(radians(self.direction)) * distance
	self.posx += x_diff
	self.posy += y_diff
	self.rect.topleft = self.posx, self.posy
	self.rect.clamp(self.area)
	
    def move_unless_frozen(self, distance):
        "Moves in current direction"
        if self.freeze_time == 0:
	    self.move(distance)
        else:
            self.freeze_time = self.freeze_time - 1

    def freeze(self, time):
        "Stand still for the specified time"
        self.freeze_time = time
    
    def say(self, words, time):
        self.speak_text = self.speak_font.render(words, 1, (10, 10, 10))
        self.speak_pos = self.rect.topright
        self.speak_time = time
    
    def speak(self, screen):
        if self.speak_time > 0:
            self.speak_time = self.speak_time - 1
            screen.blit(self.speak_text, self.rect.topright)

    def has_caught(self, target):
        "Detect when Felix catches Herbert - only returns true when he first hits"
        hitbox = self.rect.inflate(-30, -15)
        return (hitbox.colliderect(target.rect) and self.freeze_time == 0)