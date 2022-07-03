import pygame
pygame.init()  # inicia o pygame
# =======================================================================
# toca a musica mp3
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
pygame.event.wait()
# =======================================================================
