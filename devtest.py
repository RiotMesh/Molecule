import pygame

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init()

sound = pygame.mixer.Sound("system/sounds/print.wav")

while True:
    sound.play()
    input()