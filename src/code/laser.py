import pygame 

class Laser(pygame.sprite.Sprite):
	def __init__(self,pos,speed,screen_height):
		super().__init__()
		self.image = pygame.Surface((3,20))
		self.length = 20
		self.image = self.create_gradient_surface(40,40)
		self.rect = self.image.get_rect(center = pos)
		self.speed = speed
		self.height_y_constraint = screen_height

	def destroy(self):
		if self.rect.y <= -50 or self.rect.y >= self.height_y_constraint + 50:
			self.kill()

	def update(self):
		self.rect.y += self.speed
		self.destroy()

	def create_gradient_surface(self, width, length):
		gradient_surface = pygame.Surface((width, length), pygame.SRCALPHA)

		for i in range(length):
			yellow_component = int(255 * (1 - i / length))
			alpha = 255 

			pygame.draw.line(gradient_surface, (255, yellow_component, 0, alpha), (width // 2, i), (width // 2, i + 1))

		return gradient_surface