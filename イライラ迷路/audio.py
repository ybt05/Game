from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

pygame.init()
outWav = pygame.mixer.Sound("wav/out.wav")
startWav = pygame.mixer.Sound("wav/start.wav")
finishWav = pygame.mixer.Sound("wav/finish.wav")
bgm = pygame.mixer.Sound("wav/bgm.wav")
bgm.set_volume(0.1)
bgm.play(loops = -1)
startWav.set_volume(0.5)