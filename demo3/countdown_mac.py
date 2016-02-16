import macsound as pygame
import time

pygame.mixer.init()

s1        = pygame.mixer.Sound("sounds/1.wav")
s2        = pygame.mixer.Sound("sounds/2.wav")
s3        = pygame.mixer.Sound("sounds/3.wav")
s4        = pygame.mixer.Sound("sounds/4.wav")
s5        = pygame.mixer.Sound("sounds/5.wav")
squeak    = pygame.mixer.Sound("sounds/squeak.wav")
explosion = pygame.mixer.Sound("sounds/explosion.wav")
final     = pygame.mixer.Sound("sounds/finalCountdown.wav")
alert     = pygame.mixer.Sound("sounds/alert2.wav")

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
