# -----------------------------------------------------------------------------
# IMAGE LAB - IMAGE COLLAGE
# 
# Use your new knowledge of drawing and colours with Pygame to make this a full screen of a plaid pattern.
# 
# Lab Requirements:
# LEVEL 3
# Use at least 3 different images to create a collage
# You can repeat the same images must use other commands to change the look (example, tint)

# LEVEL 4
# Everything listed in level 3 
# Create a scene with images

# LEVEL 4+
# Everything listed in level 4
# Randomize or animate something

# Recommended Lessons:
# P5.js intro
# P5.js drawing
# P5.js colour
# 
# Challenge Difficulty:**
# 
# Remember the purpose of this challenge is to help you practice Pygame coding not to find code online or copy from your friends! This challenge will be checked for Plagiarism.
# 
# Upload your code to githun when finished
# 
# Good luck!
#-----------------------------------------------------------------------------

import pygame
pygame.init

windowWidth = 1280
windowHeight = 720
window = pygame.display.set_mode((windowWidth, windowHeight))

window.fill((0,0,0))

earth = pygame.image.load("earth-resized.png")
window.blit(earth,(800,200))

teto = pygame.image.load("kasane-teto.png")
window.blit(teto,(100,100))

weight = pygame.image.load("teto-heavy.png")
window.blit(weight,(300,300))

running = True
while running:

    ev = pygame.event.poll()   
    for event in pygame.event.get(): 
        if ev.type == pygame.QUIT:  
            running = False     

    pygame.display.flip()
 
pygame.quit()