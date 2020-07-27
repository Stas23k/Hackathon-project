#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
from PIL import Image,ImageFilter
import time
import numpy as np
def NF_instance(parameter_blur,parameter_size):
    boxImage = OriImage.filter(ImageFilter.BoxBlur(parameter_blur))
    resizedImage = boxImage.resize([int(parameter_size*s) for s in boxImage.size])
    mode = resizedImage.mode
    data = resizedImage.tobytes()
    size = resizedImage.size
    return data,size,mode
pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('Neurofeedback Training')
icon = pygame.image.load('brain.png')
pygame.display.set_icon(icon)
screen.fill((250,250,250))
pygame.display.update()
running = True
while running:
    image = pygame.image.load(r'im2.jpg') 
    screen.blit(image,(100,40)) 
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    for i in list(zip(randVal,rand2)): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        data,size,mode = NF_instance(i[0],i[1])
        resed = pygame.image.fromstring(data,size,mode)
        res_rec = resed.get_rect(center = screen.get_rect().center)
        screen.fill((250,250,250))
        pygame.display.update()
        screen.blit(resed,res_rec)
        pygame.display.update()
        time.sleep(0.1)

