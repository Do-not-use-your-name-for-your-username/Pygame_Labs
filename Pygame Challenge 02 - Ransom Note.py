# -----------------------------------------------------------------------------
# TEXT & FONT LAB - RANSOM NOT
# 
# Use your new knowledge of text in Pygame to make a ransom note similar to the picture above.
# 
# You use whatever fonts you want as long as you use at least 1 custom font.
# 
# The message can say whatever you want as long as it is school safe (remember the code of conduct).
# 
# Lab Requirements:
# LEVEL 3
# Use at least 3 different font styles
# Use 3 different colours
# Write a message that is school safe and does not have anyone’s personal information (including names)

# LEVEL 4
# Everything listed in level 3 
# Use at least 4 different font styles
# Use 4 different colours

# LEVEL 4+
# Everything listed in level 4
# Use a custom downloaded font
# 
# Recommended Lessons:
# Github
# Thonny
# Pygame Intro
# Pygame Window
# Pygame Game Loop
# Pygame Drawing
# Pygame Colours
# Pygame Text & Fonts
# 
# 
# Challenge Difficulty:**
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
    
 
windowWidth = 800
windowHeight = 800
window = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()


while True:
    
    ev = pygame.event.poll()    
    if ev.type == pygame.QUIT:  
        break     
    window.fill((255,255,255))

#transparent_surface = pygame.Surface(window.get_size(), pygame.SRCALPHA)

    font1 = pygame.font.Font("Milk Cake.otf", 48)
    font2 = pygame.font.Font("DarlingGirlDemoRegular.ttf", 32)
    font3 = pygame.font.Font("Game Of Squids.ttf", 20)
    font4 = pygame.font.Font("Snowy Delight.otf", 60)

    text_surface1 = font1.render('Greetings!', True, (255,0,0))
    text_surface2 = font2.render('Wanna see an if statment?', True, (255,100,100))
    text_surface3 = font3.render('if you do not give me a 95 or higher in this class', True, (255,0,100))
    text_surface4 = font4.render('I will be very, very angry', True, (0,0,0))
    
#text_rect = text_surface.get_rect(center=(250,250))

    window.blit(text_surface1, (100,200))
    window.blit(text_surface2, (200,300))
    window.blit(text_surface3, (100,400))
    window.blit(text_surface4, (200,500))

#window.blit(transparent_surface,(0,0))

    pygame.display.flip()
#clock.tick(60) # Force frame rate to 60fps or lower


pygame.quit()