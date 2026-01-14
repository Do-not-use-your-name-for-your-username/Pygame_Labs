# -----------------------------------------------------------------------------
# GAMESTATE LAB - MENU
# 
# Use your new knowledge of drawing and colours with Pygame to make this a full screen of a plaid pattern.
# 
# Lab Requirements:
# LEVEL 3
# A minimum of 3 possible unique backdrops
# A minimum of 2 buttons that when clicked will change the view of the user
# A method to return to the main menu
# HTML Buttons
# Uses gamestates
# LEVEL 4
# A minimum of 4 possible unique windows
# A minimum of 3 buttons that when clicked will change the backdrop or view of the user
# A method to return to the main menu
# Use gamestates
# Collision detection style buttons
# LEVEL 4+
# Everything listed in level 3 and 4
# Add sound effects when the button is pressed or add a mouseover effect to the button (the button highlights or changes looks when the mouse goes over the locations of the button)
# Recommended Lessons:
# Recommended Lessons:
# Github
# Thonny
# Pygame Intro
# Pygame Window
# Pygame Game Loop
# Pygame Drawing
# Pygame Colours
# Pygame Images
# Pygame Animation
# Pygame Sounds
# Pygame The Game Loop
# Pygame Events
# Pygame Gamestates
# Pygame Collision Detection
# Pygame Sprites
# 
# Challenge Difficulty:****
# 
# Remember the purpose of this challenge is to help you practice Pygame coding not to find code online or copy from your friends! This challenge will be checked for Plagiarism.
# 
# Upload your code to github when finished
# 
# Good luck!
#-----------------------------------------------------------------------------

import pygame
pygame.init

pygame.font.init()

windowWidth = 1280
windowHeight = 719
speed = 5

clock = pygame.time.Clock()
window = pygame.display.set_mode((windowWidth, windowHeight))
font1 = pygame.font.Font("Milk Cake.otf", 48)

background = pygame.image.load("menuscreen.png")

gamestate = "menu"
mousePressed = False

button = pygame.Rect(630,360,100,200)
button2 = pygame.Rect(630,590,100,200)
button3 = pygame.Rect(930,590,100,200)


while True:
    
    ev = pygame.event.poll()    
    mouseX, mouseY = pygame.mouse.get_pos() #gets position of mouse
    
    text_surface1 = font1.render('MENU', True, (255,0,0))
    window.blit(text_surface1, (100,200)) 
    menu_rect = text_surface1.get_rect(100,200)

    if ev.type == pygame.QUIT:  
        break        
    if ev.type == pygame.MOUSEBUTTONDOWN:
        mousePressed = True
    else: 
        mousePressed = False

    if gamestate == "menu":

        text_surface2 = font1.render('play', True, (255,0,0))
        window.blit(text_surface1, (500,200)) 
        menu_rect = text_surface1.get_rect(500,200)

        text_surface2 = font1.render('instructions', True, (255,0,0))
        window.blit(text_surface1, (500,500)) 
        menu_rect = text_surface1.get_rect(500,500)

        if mousePressed == True:

            if button.collidepoint:
                gamestate = "instructions"
                print(gamestate)
            if button2.collidepoint:
                gamestate = "play"
                print(gamestate)
            if button2.collidepoint:
                gamestate = "exit"
                print(gamestate)
            
            pygame.display.flip()
            clock.tick(60)
    
pygame.quit()

