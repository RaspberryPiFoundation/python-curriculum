INTRO
-----

In this game, we revisit Felix and Herbert, who we played with our first Code Club!  This time however, we will be writing the game using Python.

In our code, we are going to make use of two 'modules' to help us:

"PyGame": This is a module that provides everything we need to draw graphics, use sprites and play sounds. All the things you need for a game!
"codeclub": This is a some code to make our code a little simpler. It is provided for you as "codeclub.py".  You can look in this file to see how it works, but you don't need to understand it to write this game.

You are also provided with a script to get you started, called "felix0.py". You do need to understand this script, as you will be writing more code to go here.

felix0.py contains the following code:

#Import Modules
import pygame, codeclub
from pygame.locals import *

This section just tells Python what other bits of code we want to use - pygame and codeclub.

def main():

This "defines" a function (part of a program) called main. All the code below this line that are idented (start with spaces) are part of this "main" function.

#Initialize Everything
    pygame.init()
    screensize = (800, 600)
    screen = pygame.display.set_mode(screensize)
    
This is just setting up the pygame code, and telling it to use a window that 800 pixels wide, and 600 pixels high. You can change these numbers to change the size of the game window.

#create the wallpaper, and make it fill the screen
    wallpaper = codeclub.load_image('hall.jpg')
    wallpaper = pygame.transform.scale(wallpaper, (screensize))
    background = pygame.Surface(screensize)
    background.blit(wallpaper, (0, 0))
    
Here we load an image for the background, scaling (stretching) it to the right size to fill the window, then drawing it as a background (blit means copying a image from one place to another).

After this, we create a clock - we are going to use this to make sure the game doesn't run quickly!

#Main Loop
    while True:
    
In Scratch, we wrote lots of script that automatically ran when an event happened (like recieving a message, or clicking the green flag). In this game we have one script that loops forever deciding what other functions to call. This is called the "main loop".  The code "while True" is the same as using a "forever" block in Scratch.

There are 2 more sections of code in the main loop. The section marked "#Handle input events" makes sure we can exit the game by closing the window or pressing Escape - After all, we probably don't really want our main loop to run forever! The "#Draw everything" section redraws the background and puts in on the screen. This will be important later when we have a cat chasing a mouse all over the background!

Try running this script.  Do you get a sensible sized window, and the correct picture filling it?  Can you finish the game by pressing 'Esc'?

Step 1 - Let's get Herbert to be our mouse!
-------------------------------------------
Firstly we need to create a mouse sprite, set it's costume and size, and make it follow the mouse pointer.

To create Herbert, in the section marked "#Prepare game objects", add the code:

    herbert = codeclub.sprite()
    herbert.set_costume('mouse1.png', 60)
    allsprites = pygame.sprite.Group(herbert)

Make sure this code is idented (start each line with 4 spaces), so that it is part of the main function! This code creates a new "codeclub sprite' called herbert, loads the image "mouse1.png" its costume, sets its size to 60, and adds it to a group called "allsprites" (we'll see why later!).

To make Herbert follow the mouse pointer, add a new section in the main loop, before "#draw everything":

    #Move the sprites
        herbert.move_to(pygame.mouse.get_pos())
        
 Again - be careful with the indentation - this needs to be inside the "while True" loop, but not inside the "for event..." statement
 
 Finally, Python won't draw Herbert in his new place unless we tell it to, so add a statement in the "#Draw verything" block, after the background blit:
 
         allsprites.draw(screen)
         
 This will draw all the sprites in the "allsprites" group - which at the moment is only Herbert!
 
 Test your code!  Do you have a mouse that you can move around the screen? Did you notice that you also have the normal mouse pointer on top of herbert? You can remove this by adding a statement in the "#Initialize everything" block:
 
     pygame.mouse.set_visible(0)

Step 2 - We need a cat!
-----------------------
Now we need to create Felix and get him to chase herbert.

To create Felix, in the section marked "#Prepare game objects", add the code:

    felix = codeclub.sprite()
    felix.set_costume('cat1-a.gif', 100)
    allsprites = pygame.sprite.Group((herbert, felix))
    
 The last line of this code is instead of the similar line you already had, which must come AFTER you have created both Felix and Herbert.
 
 Now we have Felix, we need to make him chase Herbert.  In the "#Move the sprites" block you created, add the code:
 
        felix.point_towards(herbert)
        felix.move_unless_frozen(2)
        
 We can also now add a statement to make sure Herbert keeps an eye on Felix. In the same block of code add:
 
 Test your code! Do you have a cat chasing a mouse?  Are both sprite sensible sizes?  Does Felix move at about the right speed?  Can you make him move more quickly? Does Herbert always face towards Felix?
 
 Step 3 - Felix catches Herbert
 ------------------------------
 Let's add some code to work out when Herbert's been caught. When he is, we'll make Felix freeze for a short time (so Herbert has a chance to run away), and say 
 that he's caught him.  Add some code after the "#Move the sprites" block:
 
        #See whether Felix has caught Herbert
        if felix.has_caught(herbert):
            felix.freeze(20)
            felix.say("I've got you!", 60)
            
 Although we have told Felix to say something, Python won't draw this on the screen unless we tell it to. So in the "#Draw everything" block, add the statement:
 
         felix.speak(screen)
         
 Test your code!  Does Felix stop and shout when he catches Herbert? Are the lengths of time he stands still and shouts for about right? Can you change these?
 
 
 Step 4 - Keeping score
 ----------------------
 A game is no fun, unless you know when you've beat your friends!  So we need a score, and a highscore. The score should start at 0 and go up as long as you keep Herbert out of Felix's way. If Herbert gets caught, we should take a large chunk of score away while making sure it doesn't go below 0. We should also keep track of the highest it got to.
 
 Let's start off by using a couple of variables, and starting them off at 0. In the "#Prepare game objects" section, add the code:
 
     score = 0
     highscore = 0
     
 Next we increase the score each time through the loop. We can check on the highscore here as well. Before the "#Draw everything" block, add a new block of code:
 
     #update score
        score = score + 1
        if score > highscore:
            highscore = score
            
We already have an "if" statement to detect when Herbert has been caught, so we can add the code to reduce the score to this. After the statement where we tell Felix to say "I've got you!", add some more code:

            score = score - 1000
            if score < 0:
                score = 0
                
Be careful with the indentation here - this code needs to be part of the "if" statement, or you'll never get a highscore!

Now we have the score, we need to write it on the screen so the player can see what it is! Like a wordprocessor PyGame can print text in many different fonts, so we first need to create a font to use. We only need to do this once, so can do it before the main loop, in the "#Prepare Game Objects" block:

    font = pygame.font.Font(None, 36)
    
Now we can use this font to format the score, then 'blit' it onto the screen. In the "#Draw everything" block, add:

        score_text = font.render("Score :" + str(score), 1, (10, 10, 10))
        highscore_text = font.render("High Score :" + str(highscore), 1, (10, 10, 10))
        screen.blit(score_text, (0, 0))
        screen.blit(highscore_text, (0, 25))
        
Test you code!  Does the score print correctly?  Does it go up while you play the game?  What happens when Felix catches Herbert?  Is losing 1000 too much?  Do you ever get a negative score - even if Hebert is rubbish at running away?

And Finally!
------------
Enjoy playing the game!  Can you think of any way to make it better?  You may notice that the title bar of the game window says "pygame window".  You could change this with a statement like:

    pygame.display.set_caption('Felix and Herbert')   







 
 