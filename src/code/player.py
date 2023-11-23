import pygame 
from laser import Laser

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,constraint,speed):
		super().__init__()
		self.image = pygame.image.load('../graphics/player.png').convert_alpha()
		self.rect = self.image.get_rect(midbottom = pos)
		self.speed = speed
		self.max_x_constraint = constraint
		self.ready = True
		self.laser_time = 0
		self.laser_cooldown = 600

		self.lasers = pygame.sprite.Group()

		self.laser_sound = pygame.mixer.Sound('../audio/laser.wav')
		self.laser_sound.set_volume(0.5)
	def get_input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			self.rect.x += self.speed
		elif keys[pygame.K_LEFT]:
			self.rect.x -= self.speed

		if keys[pygame.K_SPACE] and self.ready:
			self.shoot_laser()
			self.ready = False
			self.laser_time = pygame.time.get_ticks()
			self.laser_sound.play()

