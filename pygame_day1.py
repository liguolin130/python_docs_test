# import pygame
# from pygame.color import THECOLORS
#
# SCREEN_RECT = pygame.Rect(20,10,1000,1000)
# screen_title = pygame.display.set_caption("guolin")
# screen = pygame.display.set_mode(SCREEN_RECT.size)
# def __screen__():
#     #pygame.draw.circle(screen, THECOLORS["red"], [100, 100], 30, 0)
#     screen.fill([255,255,255])
#     pygame.draw.circle(screen,[0,255,0],(500,300),200,1)   # 圆形cicle
#     pygame.draw.rect(screen,[255,0,0],(500,500,200,100),1) # 矩形rect
#     pygame.display.flip()
# def __game_over():
#     print("----GameOver----")
#     pygame.quit()
#     exit()
#
# while True:
#     __screen__()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             __game_over()
#
#
#


# x = np.array([1,2,3,4,5,6,7,8])
# y = np.array([3,5,7,6,2,6,10,15])
# plt.plot(x,y,'r',lw=2)

import numpy as np
import matplotlib.pyplot as plt
zhu_x = np.array([1,2,3,4,5,6,7,8])
zhu_y = np.array([13,25,17,36,21,16,10,15])
plt.bar(zhu_x,zhu_y,0.2,alpha=0.5,color='r')
plt.show()
