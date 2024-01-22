import pygame
import random

#initial variables needed
playerX = []
invaderImage = []
invaderX = []
invaderY = []
invaderXchange = []
invaderYchange = []
invaderCount = 8
gameOver = False 

running = True

pygame.init()

while running :
#Controls movement of invader
def invaderMovementHandler() :
    for i in range(invaderCount):
        if invaderY[i] >= 450:
            if abs(playerX-invaderX[i]) < 80:
                for j in range(invaderCount):
                    invaderY[j] = 2000
                gameOver()
                break

        if invaderX[i] >= 735 or invaderX[i] <= 0:
            invaderXchange[i] *= -1
            invaderY[i] += invaderYchange[i] 