import sys, pygame
import threading
import time

class Timer:

	def __init__(self, minutes, seconds):


		self.WIDTH, self.HEIGHT = 400, 200
		self.BLACK = (0, 0, 0)
		self.WHITE = (255, 255, 255)
		self.BLUE = (115, 147, 255)

		# Initialise pygame and load the alarm sound
		pygame.init()
		pygame.mixer.music.load("alarm_sound.mp3")

		# Set up window
		self.font = pygame.font.SysFont("bahnschrift", 120)
		self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		pygame.display.set_caption("Timer")

		# Set up timer
		self.seconds = seconds + (60 * minutes)
		self.start_seconds = self.seconds
		self.timer = threading.Thread(target=self.run_timer)

		# Run main loop
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

			time.sleep(1)
			self.seconds -= 1

		pygame.mixer.music.play()


	def update_screen(self):

		self.screen.fill(self.WHITE)
		self.format_time()
		self.write_text(self.time_output, (((self.WIDTH // 2) - 140, (self.HEIGHT // 2) - 10)), self.BLACK)
		self.draw_progress_bar()
		self.draw_box()


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


	def draw_progress_bar(self):

		progress = (self.start_seconds - self.seconds) / self.start_seconds
		progress_bar_rect = pygame.Rect(0, self.HEIGHT - 10, round(self.WIDTH * progress), self.HEIGHT)
		pygame.draw.rect(self.screen, self.BLUE, progress_bar_rect)


	def draw_box(self):

		box = pygame.Rect((self.WIDTH // 2) - 150, (self.HEIGHT // 2) - 75, (self.WIDTH // 2) + 107, (self.HEIGHT // 2) + 40)
		pygame.draw.rect(self.screen, self.BLACK, box, 2)




Timer(minutes=7, seconds=10)



