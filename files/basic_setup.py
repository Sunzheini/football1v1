from abc import ABC, abstractmethod
import pygame
pygame.font.init()   # enable the fonts
pygame.mixer.init()  # enable sounds


class BasicSetup(ABC):
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 500
    WINDOW_COLOR = (97, 97, 97)

    FPS = 60

    def __init__(self):
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Football 1v1')

    @staticmethod
    def update_after_any_change():
        pygame.display.update()

    def draw_window(self):
        self.window.fill(self.WINDOW_COLOR)  # RGB
        self.update_after_any_change()

    @abstractmethod
    def run_game(self):
        pass
