#!/usr/bin/env python
'''

For this exercise, draw a random number of randomly-sized sprites with a random color, random initial position, and random direction

'''
import sys, logging, pygame, random
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' 

logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)

screen_size = (800,600)
FPS = 60
red = (255,0,0)
black = (0,0,0)
colors = [(134,142,150),(250,82,82),(230,73,128),(190,75,219),(121,80,242),(76,110,245),(34,138,230),(21,170,191),(18,184,134),(64,192,87),(130,201,30),(250,176,5),(253,126,20),(233,236,239),(255,236,153),(163,218,255)]


class Block(pygame.sprite.Sprite):
	def __init__(self, color, size, position, direction):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface(size)
		self.image.fill(color)
		self.rect = self.image.get_rect()
		(self.rect.x,self.rect.y) = position
		self.direction = direction

	def update(self):
		(dx,dy) = self.direction
		self.rect.x += dx
		self.rect.y += dy
		(WIDTH,HEIGHT) = screen_size
		if self.rect.left > WIDTH:
			self.rect.right = 0
		if self.rect.right < 0:
			self.rect.left = WIDTH
		if self.rect.top > HEIGHT:
			self.rect.bottom = 0
		if self.rect.bottom < 0:
			self.rect.top = HEIGHT


def main():
	pygame.init()
	screen = pygame.display.set_mode(screen_size)
	clock = pygame.time.Clock()

	blocks = pygame.sprite.Group()
	for b in range(1,random.randint(1,44)):
		block = Block(random.choice(colors),(random.randint(2,50),random.randint(2,50)),(random.randint(100,200),random.randint(100,200)),(random.randint(-1,10),random.randint(-1,4)))
		blocks.add(block)


	while True:
		clock.tick(FPS)
		screen.fill(black)


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit(0)

		blocks.update()
		blocks.draw(screen)
		pygame.display.flip()

if __name__ == '__main__':
	main()