import pygame, sys
from player import Player
import obstacle
from alien import Alien, Extra
from random import choice, randint
from laser import Laser
import os

class Game:
	
	def __init__(self):
		# Player setup
		player_sprite = Player((screen_width / 2,screen_height),screen_width,5)
		self.player = pygame.sprite.GroupSingle(player_sprite)

		# health and score setup
		self.lives = 3
		self.live_surf = pygame.image.load('../graphics/player.png').convert_alpha()
		self.live_x_start_pos = screen_width - (self.live_surf.get_size()[0] * 2 + 20)
		self.score = 0
		self.font = pygame.font.Font('../font/Pixeled.ttf',20)
		self.highscore = 0
		
		#obstacle setup
		self.shape = obstacle.shape
		self.block_size = 6
		self.blocks = pygame.sprite.Group()
		self.obstacle_amount = 4
		self.obstacle_x_positions = [num * (screen_width / self.obstacle_amount) for num in range(self.obstacle_amount)]
		self.create_multiple_obstacles(*self.obstacle_x_positions, x_start = screen_width / 15, y_start = 480)

		#alien setup
		self.aliens = pygame.sprite.Group()
		self.alien_lasers = pygame.sprite.Group()
		self.alien_setup(rows = 6, cols = 8)
		self.alien_direction = 1

		#extra setup
		self.extra = pygame.sprite.GroupSingle()
		self.extra_spawn_time = randint(40,80)
		
		#background setup
		# pygame.transform.scale(pygame.image.load(os.path.join("graphics", "background-black.png")), (screen_width, screen_height))
		base_path = os.path.dirname(os.path.abspath(__file__))
		image_path = os.path.join(base_path, "..", "graphics", "background-black.png")
		self.BG_IMAGE = pygame.transform.scale(pygame.image.load(image_path), (screen_width, screen_height))



	def create_obstacle(self, x_start, y_start,offset_x):
		for row_index, row in enumerate(self.shape):
			for col_index,col in enumerate(row):
				if col == 'x':
					x = x_start + col_index * self.block_size + offset_x
					y = y_start + row_index * self.block_size
					block = obstacle.Block(self.block_size,(255, 204, 0),x,y)
					self.blocks.add(block)

	def create_multiple_obstacles(self,*offset,x_start,y_start):
		for offset_x in offset:
			self.create_obstacle(x_start,y_start,offset_x)

	def alien_setup(self,rows,cols,x_distance = 60,y_distance = 48,x_offset = 70, y_offset = 100):
		for row_index, row in enumerate(range(rows)):
			for col_index, col in enumerate(range(cols)):
				x = col_index * x_distance + x_offset
				y = row_index * y_distance + y_offset

				if row_index == 0: alien_sprite = Alien('yellow',x,y)
				elif 1 <= row_index <= 2: alien_sprite = Alien('green',x,y)
				else: alien_sprite = Alien('red',x,y)
				self.aliens.add(alien_sprite)

	def alien_position_checker(self):
		all_aliens = self.aliens.sprites()
		for alien in all_aliens:
			if alien.rect.right >= screen_width:
				self.alien_direction = -1
				self.alien_move_down(2)
			elif alien.rect.left <= 0:
				self.alien_direction = 1
				self.alien_move_down(2)	

	def alien_move_down(self,distance):
		if self.aliens:
			for alien in self.aliens.sprites():
				alien.rect.y += distance

	def alien_shoot(self):
		if self.aliens.sprites():
			random_alien = choice(self.aliens.sprites())
			laser_sprite = Laser(random_alien.rect.center,6,screen_height)
			self.alien_lasers.add(laser_sprite)

	def extra_alien_timer(self):
		self.extra_spawn_time -= 1
		if self.extra_spawn_time <= 0:
			self.extra.add(Extra(choice(['right','left']),screen_width))
			self.extra_spawn_time = randint(400,800)

	def check_for_highscore(self):
		if self.score > self.highscore:
			self.highscore = self.score

			with open("highscore.txt", "w") as file:
				file.write(str(self.highscore))

	def load_highscore(self):
		try:
			with open("highscore.txt", "r") as file:
				self.highscore = int(file.read())
		except FileNotFoundError:
			self.highscore = 0

	def collision_checks(self):
		#player lasers
		if self.player.sprite.lasers:
			for laser in self.player.sprite.lasers:
				#obstacles collisions
				if pygame.sprite.spritecollide(laser,self.blocks,True):
					laser.kill()

				#alien collisions
				aliens_hit = pygame.sprite.spritecollide(laser,self.aliens,True)
				if aliens_hit:
					for alien in aliens_hit:
						self.score += alien.value
						self.check_for_highscore()
					laser.kill()

				# extra collision
				if pygame.sprite.spritecollide(laser,self.extra,True):
					self.score += 500
					self.check_for_highscore()
					laser.kill()

		# alien lasers 
		if self.alien_lasers:
			for laser in self.alien_lasers:
				# obstacle collisions
				if pygame.sprite.spritecollide(laser,self.blocks,True):
					laser.kill()

				if pygame.sprite.spritecollide(laser,self.player,False):
					laser.kill()
					self.lives -= 1
					if self.lives <= 0:
						if self.lives == 0:
							self.game_over()

		# aliens
		if self.aliens:
			for alien in self.aliens:
				pygame.sprite.spritecollide(alien,self.blocks,True)

				if pygame.sprite.spritecollide(alien,self.player,False):
					self.game_over()
					
	

	def display_lives(self):
		for live in range(self.lives - 1):
			x = self.live_x_start_pos + (live * (self.live_surf.get_size()[0] + 10))
			screen.blit(self.live_surf,(x,8))

	def display_score(self):
		score_surf = self.font.render(f'score: {self.score}',False,'white')
		score_rect = score_surf.get_rect(topleft = (10,-10))
		screen.blit(score_surf,score_rect)
		highscore_text_surface = self.font.render("HIGH-SCORE", False,'white')
		screen.blit(highscore_text_surface, (10, 30, 20, 50))
		formatted_highscore = str(game.highscore).zfill(5)
		highscore_surface = self.font.render(formatted_highscore, False, 'white')
		screen.blit(highscore_surface,(200, 30, 20, 50))

	def typewriter_effec(self):





	def victory_message(self):
		if not self.aliens.sprites():
			victory_surf = self.font.render('You won!',False,'white')
			victory_rect = victory_surf.get_rect(center = (screen_width / 2, screen_height / 2))
			screen.blit(victory_surf,victory_rect)
			
	def game_over(self):

		if self.aliens.sprites():
			if self.lives <= 0:
				explosion_color = (51, 204, 204)
				explosion_radius = 70
				explosion_particles = 100

				for _ in range(explosion_particles):
					x = self.player.sprite.rect.centerx + randint(-explosion_radius, explosion_radius)
					y = self.player.sprite.rect.centery + randint(-explosion_radius, explosion_radius)
					pygame.draw.circle(screen, explosion_color, (x, y), 1)

					pygame.display.flip()
					pygame.time.delay(10)

			game_over_surf = self.font.render("GAME OVER", False, 'white')
			game_over_rect = game_over_surf.get_rect(center=(screen_width / 2, screen_height / 2))
			screen.blit(game_over_surf, game_over_rect)
			pygame.display.flip()
			pygame.time.delay(2000)  
			pygame.quit()
			sys.exit()


	def run(self):
		
		screen.blit(self.BG_IMAGE, (0, 0))

		self.player.update()
		self.alien_lasers.update()
		self.extra.update()

		self.aliens.update(self.alien_direction)		
		self.alien_position_checker()
		self.extra_alien_timer()
		self.collision_checks()

		self.player.sprite.lasers.draw(screen)
		self.player.draw(screen)
		self.blocks.draw(screen)
		self.aliens.draw(screen)
		self.alien_lasers.draw(screen)
		self.extra.draw(screen)
		self.display_lives()
		self.display_score()
		self.victory_message()


		#draw sprite groups


if __name__ == '__main__':
	pygame.init()
	screen_width = 600
	screen_height = 600
	screen = pygame.display.set_mode((screen_width,screen_height))
	clock = pygame.time.Clock()
	game = Game()



	ALIENLASER = pygame.USEREVENT + 1
	pygame.time.set_timer(ALIENLASER,800)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == ALIENLASER:
				game.alien_shoot()

		screen.fill((30,30,30))
		game.run()
			
		pygame.display.flip()
		clock.tick(60)