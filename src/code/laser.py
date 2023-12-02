import pygame 

class Laser(pygame.sprite.Sprite):
	def __init__(self,pos,speed,screen_height):
		super().__init__()
		self.image = pygame.Surface((4,20))
		self.length = 20
		self.image.fill('green')
		self.rect = self.image.get_rect(center = pos)
		self.speed = speed
		self.height_y_constraint = screen_height

	def destroy(self):
		if self.rect.y <= -50 or self.rect.y >= self.height_y_constraint + 50:
			self.kill()

	def update(self):
		self.rect.y += self.speed
		self.destroy()

	def create_gradient_surface(self,length):
		gradient_surface = pygame.Surface((4, length), pygame.SRCALPHA)

		for i in range(length):
			alpha = int(255 * (1 - i / length)) 
			pygame.draw.line(gradient_surface, (0, 255, 0, alpha), (2, i), (2, i + 1))

		return gradient_surface