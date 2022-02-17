import sys, pygame
import threading
import time

class Timer:

	def __init__(self, minutes, seconds):

		self.WIDTH, self.HEIGHT = 400, 200

		self.BLACK = (0, 0, 0)
		self.WHITE = (255, 255, 255)

		pygame.init()

		self.font = pygame.font.SysFont(None, 120)
		self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		pygame.display.set_caption("Timer")

		self.seconds = seconds + (60 * minutes)

		self.timer = threading.Thread(target=self.run_timer)

		self.main()


	def main(self):

		self.timer.start()

		while True:

			for event in pygame.event.get():
				if event.type == pygame.QUIT:

					self.seconds = 0
					sys.exit()

			self.update_screen()


	def run_timer(self):

		while self.seconds > 0:

			self.seconds -= 1
			time.sleep(1)


	def update_screen(self):

		self.screen.fill(self.BLACK)
		self.format_time()
		self.write_text(self.time_output, (((self.WIDTH // 2) - 110, self.HEIGHT // 2)), self.WHITE)


		pygame.display.update()


	def format_time(self):

		seconds = str(self.seconds % 60)
		minutes = str(self.seconds // 60)

		seconds = ("0" + seconds) if len(seconds) < 2 else seconds
		minutes = ("0" + minutes) if len(minutes) < 2 else minutes

		self.time_output = f"{minutes}:{seconds}"


	def write_text(self, text, position, colour):
	
		text = self.font.render(text, True, colour)
		text_rect = text.get_rect(midleft=position)
		self.screen.blit(text, text_rect)



Timer(minutes=2, seconds=30)



