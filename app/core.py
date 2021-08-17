import pygame.display

from app import ALPHA, REFRESH_EVENT, WHITE
from app.mouse import Mouse
from app.transparency import setup


class AppCore:

    def __init__(self):
        self.screen = pygame.display.set_mode(
            (0, 0), 1, pygame.FULLSCREEN | pygame.NOFRAME
        )

        self.h = self.screen.get_height()
        self.w = self.screen.get_width()

        setup(pygame.display.get_wm_info()["window"], ALPHA)
        self.is_running = True

        pygame.event.set_blocked(None)
        pygame.event.set_allowed([pygame.QUIT, REFRESH_EVENT.type])

        self.mouse = Mouse()
        self.mouse.start_listening()

    def run(self):
        while self.is_running:
            self.screen.fill(ALPHA)

            x, y = self.mouse.pos

            pygame.draw.line(self.screen, WHITE, (x, y - 20), (x, 0), 2)
            pygame.draw.line(self.screen, WHITE, (x, y + 20), (x, self.h), 2)

            pygame.draw.line(self.screen, WHITE, (x - 20, y), (0, y), 2)
            pygame.draw.line(self.screen, WHITE, (x + 20, y), (self.w, y), 2)

            pygame.display.update()

            try:
                event = pygame.event.wait()
            except KeyboardInterrupt:
                event = pygame.event.Event(pygame.QUIT)

            if event.type == pygame.QUIT:
                self.mouse.stop_listening()
                self.is_running = False
