import os
from abc import ABC, abstractmethod
import pygame
pygame.font.init()   # enable the fonts
pygame.mixer.init()  # enable sounds


class BasicSetup(ABC):
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 500

    GREY_COLOR = (97, 97, 97)
    BLUE_COLOR = (0, 0, 255)
    GREEN_COLOR = (200, 255, 0)

    FPS = 60

    SCORE_FONT = pygame.font.SysFont('arial', 30)
    WINNER_FONT = pygame.font.SysFont('arial', 60)

    GOAL_SOUND = pygame.mixer.Sound(os.path.join('.', 'assets', 'goal.mp3'))
    GOAL_SOUND.set_volume(0.5)  # lower volume
    HIT_BALL_SOUND = pygame.mixer.Sound(os.path.join('.', 'assets', 'hit_ball.mp3'))
    GOAL_SOUND.set_volume(0.3)  # lower volume
    INITIATE_AFTER_GOAL_SOUND = pygame.mixer.Sound(os.path.join('.', 'assets', 'initiate_after_goal.mp3'))
    WIN_SOUND = pygame.mixer.Sound(os.path.join('.', 'assets', 'win_sound.mp3'))

    MOVEMENT_VELOCITY = 5
    BULLET_VELOCITY = 8

    PIECE_WIDTH = 75
    PIECE_HEIGHT = 75
    GREEN_PIECE_IMAGE = pygame.image.load(os.path.join('.', 'assets', 'blue.png'))
    BLUE_PIECE_IMAGE = pygame.image.load(os.path.join('.', 'assets', 'blue.png'))

    BACKGROUND = pygame.image.load(os.path.join('.', 'assets', 'background.jpg'))

    PLAYER_1_KEYS = [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s]  # left, right, up, down
    PLAYER_2_KEYS = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    BORDER = pygame.Rect(WINDOW_WIDTH // 2 - 5, 0, 10, WINDOW_HEIGHT)  # only int

    def __init__(self):
        self.window = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Football 1v1')

        # transform images before display
        self.green_piece = pygame.transform.rotate(
            pygame.transform.scale(self.GREEN_PIECE_IMAGE,
                                   (self.PIECE_WIDTH, self.PIECE_HEIGHT)), 0)
        self.blue_piece = pygame.transform.rotate(
            pygame.transform.scale(self.BLUE_PIECE_IMAGE,
                                   (self.PIECE_WIDTH, self.PIECE_HEIGHT)), 0)
        self.background = pygame.transform.scale(self.BACKGROUND,
                                                 (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        # circles for pieces in order to use the rectangles for movement later
        self.green = pygame.Rect(100, 200, self.PIECE_WIDTH, self.PIECE_HEIGHT)  # x, y, width, height
        self.purple = pygame.Rect(350, 200, self.PIECE_WIDTH, self.PIECE_HEIGHT)  # x, y, width, height

        # score
        self.green_score = 0
        self.blue_score = 0

    @staticmethod
    def update_after_any_change():
        pygame.display.update()

    @abstractmethod
    def draw_window(self):
        pass

    @abstractmethod
    def run_game(self):
        pass
