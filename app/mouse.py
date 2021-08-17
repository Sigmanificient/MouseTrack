import time
from threading import Thread

import mouse
import pygame

from app import REFRESH_EVENT


class Mouse:

    def __init__(self):
        self.pos = (0, 0)
        self.is_running = True
        self.thread = Thread(target=self.update)

    def start_listening(self):
        self.thread.start()

    def stop_listening(self):
        self.is_running = False
        self.thread.join()

    def update(self):
        while self.is_running:
            pos = mouse.get_position()

            if pos == self.pos:
                continue

            self.pos = pos
            pygame.event.post(REFRESH_EVENT)
            time.sleep(0.05)
