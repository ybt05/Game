from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

pygame.init()
button1Wav = pygame.mixer.Sound("wav/button1.wav")
button2Wav = pygame.mixer.Sound("wav/button2.wav")
startWav = pygame.mixer.Sound("wav/start.wav")
finishWav = pygame.mixer.Sound("wav/finish.wav")
bgm = pygame.mixer.Sound("wav/bgm.wav")
bgm.set_volume(0.1)
bgm.play(loops = -1)
button2Wav.set_volume(0.5)
startWav.set_volume(0.5)