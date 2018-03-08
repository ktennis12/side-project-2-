Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> """
SpritesInLists

Description: You click and a random sprite will appear 
"""

import pygame
import random
import tsk

pygame.init()


window = pygame.display.set_mode([500, 500])

window.fill((255, 255, 255))

sprite_list = []

AI = tsk.Sprite("AirInventor2.png", 243, 217)
AS = tsk.Sprite("AstronautSpin.png", 226, 226)
Boulder = tsk.Sprite("Boulder.png", 164, 163)
Cat = tsk.Sprite("Cat.png", 200, 200)
Oragutan = tsk.Sprite("OrangutanBlue.png", 94, 141)

sprite_list.append(AI)
sprite_list.append(AS)
sprite_list.append(Boulder)
sprite_list.append(Cat)
sprite_list.append(Oragutan)

click = True
while click:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            click = False
        if len(sprite_list) == 0:
            print("Goodbye ")
            break
            
        
        if event.type == pygame.K_DOWN:
            select = random.randint(0, len(sprite_list) - 1)
        
            
            mouse_x, mouse_y = pygame.mouse.get_pos()            
            
            sprite_list[select].draw()
            sprite_list.remove(sprite_list[select])
            pygame.display.flip()
            
    

            

