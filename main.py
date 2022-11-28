import pygame
from files.basic_setup import BasicSetup
pygame.font.init()   # enable the fonts
pygame.mixer.init()  # enable sounds


class NewGame(BasicSetup):
    def run_game(self):
        run = True

        while run:
            self.clock.tick(self.FPS)

            # exit condition
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()   # when we press the x it will actually close the game

            self.draw_window()

        # instead of quitting the game it is restarting by re-initiating!
        game = NewGame()
        game.run_game()


new_game = NewGame()
new_game.run_game()
