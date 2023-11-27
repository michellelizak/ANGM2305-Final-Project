import pygame, sys
from player import Player
import obstacle
from alien import Alien

class Game:
	
	def __init__(self):
		# Player setup
		player_sprite = Player((screen_width / 2,screen_height),screen_width,5)
		self.player = pygame.sprite.GroupSingle(player_sprite)

		#obstacle setup
		self.shape = obstacle.shape
		self.block_size = 6
		self.blocks = pygame.sprite.Group()
		self.obstacle_amount = 4
		self.obstacle_x_positions = [num for num in range(self.obstacle_amount)]
		self.create_multiple_obstacles(*self.obstacle_x_positions, x_start = screen_width / 15, y_start = 480)

		#alien setup
		self.aliens = pygame.sprite.Group()
		self.alien_setup(rows = 6, cols = 8)

	def create_obstacle(self,x_start,y_start,offset_x):
		for row_index, row in enumerate(self.shape):
			for col_index,col in enumerate(row):
				if col == 'x':
					x = x_start + col_index * self.block_size +  offset_x
					y = y_start + col_index * self.block_size 
					block = obstacle.Block(self.block_size,(241,79,80),x,y)
					self.blocks.add(block)

	def create_multiple_obstacles(self,*offset,x_start, y_start):
		for offset_x in offset:
			self.create_obstacle(x_start,y_start,offset_x)

	def alien_setup(self,rows,cols):
		for row_index, row in enumerate(rows):
			for col_index, col in enumerate(cols):
				x = col_index
				y = row_index 
				alien_sprite = Alien('red',x,y)
				self.aliens.add(alien_sprite)

	def run(self):
		self.player.update()
		self.player.sprite.lasers.draw(screen)
		self.player.draw(screen)

if __name__ == '__main__':
	pygame.init()
	screen_width = 600
	screen_height = 600
	screen = pygame.display.set_mode((screen_width,screen_height))
	clock = pygame.time.Clock()
	game = Game()


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		screen.fill((30,30,30))
			
		pygame.display.flip()
		clock.tick(60)