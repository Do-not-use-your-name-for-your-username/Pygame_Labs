# -----------------------------------------------------------------------------
# ANIMATION LAB - SCROLLING BACKGROUND
# 
# Use your new knowledge of drawing and colours with Pygame to make this a full screen of a plaid pattern.
# 
# Lab Requirements:
# LEVEL 3
# A background that scrolls across the screen creating the illusion of movement
# LEVEL 4+
# Everything listed in level 3 
# Multiple layers moving at different speeds to create the parallax effect, like you see to the left
# 
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
# 
# Challenge Difficulty:*
# 
# Remember the purpose of this challenge is to help you practice Pygame coding not to find code online or copy from your friends! This challenge will be checked for Plagiarism.
# 
# Upload your code to githunb when finished
# 
# Good luck!
#-----------------------------------------------------------------------------

import pygame
pygame.init

windowWidth = 1280
windowHeight = 719
speed = 5

clock = pygame.time.Clock()

window = pygame.display.set_mode((windowWidth, windowHeight))

background = pygame.image.load("city.jpg")
background2 = background

bg1X = 0
bg2X = 1280

while True:
    
    ev = pygame.event.poll()    
    if ev.type == pygame.QUIT:  
        break        

    bg1X = bg1X - speed
    bg2X = bg2X - speed

    if bg1X < -1280:
        bg1X = 1280
    if bg2X < -1280:
        bg2X = 1280

    window.blit(background, (bg1X, 0))
    window.blit(background2, (bg2X, 0))

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()