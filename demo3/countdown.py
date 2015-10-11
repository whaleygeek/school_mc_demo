import pygame
import time

pygame.mixer.init()

s1        = pygame.mixer.Sound("1.wav")
s2        = pygame.mixer.Sound("2.wav")
s3        = pygame.mixer.Sound("3.wav")
s4        = pygame.mixer.Sound("4.wav")
s5        = pygame.mixer.Sound("5.wav")
squeak    = pygame.mixer.Sound("squeak.wav")
explosion = pygame.mixer.Sound("explosion.wav")
final     = pygame.mixer.Sound("finalCountdown.wav")
alert     = pygame.mixer.Sound("alert2.wav")

def count():
	sounds = [s5, s4, s3, s2, s1]
        #sounds = [s1, s3, s2, s4, s5]
	#sounds = [alert, final, s5, s4, s3, s2, s1]

	for s in sounds:
		s.play()
		time.sleep(s.get_length())

def bang():
        s = squeak
        #s = explosion
	s.play()
	time.sleep(s.get_length())

	
if __name__ == "__main__":
	count()
	bang()
