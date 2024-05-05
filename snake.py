import pygame
import sys
import random
from pygame.math import Vector2

class Snake:
	def __init__(self):
		self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
		self.direction = Vector2(0,0)
		self.new_block = False

		self.head_up = pygame.transform.scale(pygame.image.load('Snake/headup.png').convert_alpha(), (cell_size, cell_size))
		self.head_down = pygame.transform.scale(pygame.image.load('Snake/headdown.png').convert_alpha(), (cell_size, cell_size))
		self.head_right = pygame.transform.scale(pygame.image.load('Snake/headright.png').convert_alpha(), (cell_size, cell_size))
		self.head_left = pygame.transform.scale(pygame.image.load('Snake/headleft.png').convert_alpha(), (cell_size, cell_size))
        
        # Load and scale the snake tail images
		self.tail_up = pygame.transform.scale(pygame.image.load('Snake/taildown.png').convert_alpha(), (cell_size, cell_size))
		self.tail_down = pygame.transform.scale(pygame.image.load('Snake/tailup.png').convert_alpha(), (cell_size, cell_size))
		self.tail_right = pygame.transform.scale(pygame.image.load('Snake/tailleft.png').convert_alpha(), (cell_size, cell_size))
		self.tail_left = pygame.transform.scale(pygame.image.load('Snake/tailright.png').convert_alpha(), (cell_size, cell_size))

        # Load and scale the snake body images
		self.body_vertical = pygame.transform.scale(pygame.image.load('Snake/verticalbody.png').convert_alpha(), (cell_size, cell_size))
		self.body_horizontal = pygame.transform.scale(pygame.image.load('Snake/horizontalbody.png').convert_alpha(), (cell_size, cell_size))

		self.body_tr = pygame.transform.scale(pygame.image.load('Snake/bodytr.png').convert_alpha(), (cell_size, cell_size))
		self.body_tl = pygame.transform.scale(pygame.image.load('Snake/bodytl.png').convert_alpha(), (cell_size, cell_size))
		self.body_br = pygame.transform.scale(pygame.image.load('Snake/bodybr.png').convert_alpha(), (cell_size, cell_size))
		self.body_bl = pygame.transform.scale(pygame.image.load('Snake/bodybl.png').convert_alpha(), (cell_size, cell_size))
		

	def draw_snake(self):
		self.update_head_graphics()
		self.update_tail_graphics()

		for index,block in enumerate(self.body):
			x_pos = int(block.x * cell_size)
			y_pos = int(block.y * cell_size)
			block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

			if index == 0:
				screen.blit(self.head,block_rect)
			elif index == len(self.body) - 1:
				screen.blit(self.tail,block_rect)
			else:
				previous_block = self.body[index + 1] - block
				next_block = self.body[index - 1] - block
				if previous_block.x == next_block.x:
					screen.blit(self.body_vertical,block_rect)
				elif previous_block.y == next_block.y:
					screen.blit(self.body_horizontal,block_rect)
				else:
					if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
						screen.blit(self.body_tl,block_rect)
					elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
						screen.blit(self.body_bl,block_rect)
					elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
						screen.blit(self.body_tr,block_rect)
					elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
						screen.blit(self.body_br,block_rect)

	def update_head_graphics(self):
		head_relation = self.body[1] - self.body[0]
		if head_relation == Vector2(1,0): self.head = self.head_left
		elif head_relation == Vector2(-1,0): self.head = self.head_right
		elif head_relation == Vector2(0,1): self.head = self.head_up
		elif head_relation == Vector2(0,-1): self.head = self.head_down

	def update_tail_graphics(self):
		tail_relation = self.body[-2] - self.body[-1]
		if tail_relation == Vector2(1,0): self.tail = self.tail_left
		elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
		elif tail_relation == Vector2(0,1): self.tail = self.tail_up
		elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

	def move_snake(self):
		if self.new_block == True:
			body_copy = self.body[:]
			body_copy.insert(0,body_copy[0] + self.direction)
			self.body = body_copy[:]
			self.new_block = False
		else:
			body_copy = self.body[:-1]
			body_copy.insert(0,body_copy[0] + self.direction)
			self.body = body_copy[:]

	def add_block(self):
		self.new_block = True


	def reset(self):
		self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
		self.direction = Vector2(0,0)


class Food:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        screen.blit(self.image, fruit_rect)

    def randomize(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x,self.y)
        self.image_path = random.choice(["Food/burger.png", "Food/cheesecake.png", "Food/chocolate.png",
		 "Food/hotdog.png", "Food/burger.png", "Food/taco.png","Food/waffle.png", "Food/bacon.png", "Food/burrito.png",
		 "Food/applepie.png", "Food/bagel.png", "Food/bread.png","Food/chicken.png", "Food/cookies.png", "Food/donut.png",
		 "Food/gingerbread.png", "Food/icecream.png", "Food/jelly.png","Food/meatballs.png", "Food/nacho.png", "Food/pancakes.png",
		 "Food/pizza.png", "Food/popcorn.png", "Food/pudding.png","Food/ramen.png", "Food/strawberrycake.png", "Food/spaghetti.png",
		 "Food/sushi.png", "Food/steak.png"]) 
        self.image = pygame.image.load(self.image_path).convert_alpha()


class Main:
	def __init__(self):
		self.snake = Snake()
		self.fruit = Food()

	def update(self):
		self.snake.move_snake()
		self.check_collision()
		self.check_fail()

	def draw_elements(self):
		self.draw_grass()
		self.fruit.draw_fruit()
		self.snake.draw_snake()
		self.draw_score()

	def check_collision(self):
		if self.fruit.pos == self.snake.body[0]:
			self.fruit.randomize()
			self.snake.add_block()
		for block in self.snake.body[1:]:
			if block == self.fruit.pos:
				self.fruit.randomize()

	def check_fail(self):
		if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
			self.game_over()

		for block in self.snake.body[1:]:
			if block == self.snake.body[0]:
				self.game_over()
		
	def game_over(self):
		self.snake.reset()

	def draw_grass(self):
		grass_color = (165, 105, 189 )
		for row in range(cell_number):
			if row % 2 == 0: 
				for col in range(cell_number):
					if col % 2 == 0:
						grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
						pygame.draw.rect(screen,grass_color,grass_rect)
			else:
				for col in range(cell_number):
					if col % 2 != 0:
						grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
						pygame.draw.rect(screen,grass_color,grass_rect)			

	def draw_score(self):
		score_text = str(len(self.snake.body) - 3)
		score_surface = game_font.render(score_text,True,(56,74,12))
		score_x = int(cell_size * cell_number - 60)
		score_y = int(cell_size * cell_number - 40)
		score_rect = score_surface.get_rect(center = (score_x,score_y))
		sandwich_rect = sandwich.get_rect(midright = (score_rect.left,score_rect.centery))
		bg_rect = pygame.Rect(sandwich_rect.left,sandwich_rect.top,sandwich_rect.width + score_rect.width + 6,sandwich_rect.height)

		pygame.draw.rect(screen,(229, 232, 232),bg_rect)
		screen.blit(score_surface,score_rect)
		screen.blit(sandwich,sandwich_rect)
		pygame.draw.rect(screen,(56,74,12),bg_rect,2)

	

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
cell_size = 30
cell_number = 25
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()
sandwich = pygame.image.load('Food/sandwich.png').convert_alpha()
game_font = pygame.font.Font('Font/SuperWoobly.ttf', 25)
pygame.display.set_caption("Gourmando: The Snake")
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)
pygame.mixer.music.load('Music/Night_Shade.mp3')
pygame.mixer.music.set_volume(0.1)
# Play music with infinite loop
pygame.mixer.music.play(-1)

main_game = Main()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == SCREEN_UPDATE:
			main_game.update()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				if main_game.snake.direction.y != 1:
					main_game.snake.direction = Vector2(0,-1)
			if event.key == pygame.K_RIGHT:
				if main_game.snake.direction.x != -1:
					main_game.snake.direction = Vector2(1,0)
			if event.key == pygame.K_DOWN:
				if main_game.snake.direction.y != -1:
					main_game.snake.direction = Vector2(0,1)
			if event.key == pygame.K_LEFT:
				if main_game.snake.direction.x != 1:
					main_game.snake.direction = Vector2(-1,0)

	screen.fill((142, 68, 173))
	main_game.draw_elements()
	pygame.display.update()
	clock.tick(60)