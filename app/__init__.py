from typing import Tuple, Union

import pygame

Color = Union[Tuple[int, int, int]]

BLACK: Color = (0,) * 3
WHITE: Color = (255,) * 3
ALPHA: Color = (128,) * 3
pygame.init()

REFRESH_EVENT = pygame.event.Event(pygame.USEREVENT + 1)