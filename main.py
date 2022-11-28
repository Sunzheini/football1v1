import pygame
from files.basic_setup import BasicSetup
pygame.font.init()   # enable the fonts
pygame.mixer.init()  # enable sounds


class NewGame(BasicSetup):

    def draw_window(self):
        # self.window.fill(self.GREY_COLOR)  # RGB
        self.window.blit(self.background, (0, 0))
        pygame.draw.rect(self.window, self.GREY_COLOR, self.BORDER)  # draw the border

        green_player_score_text = self.SCORE_FONT.render(str(self.green_score), True, self.GREEN_COLOR)
        self.window.blit(green_player_score_text, (10, 10))
        blue_player_score_text = self.SCORE_FONT.render(str(self.blue_score), True, self.BLUE_COLOR)
        self.window.blit(blue_player_score_text, (self.WINDOW_WIDTH - blue_player_score_text.get_width()-10, 10))

        self.window.blit(self.green_piece, (50, 50))  # always draw after filling the screen
        self.window.blit(self.blue_piece, (100, 100))

        self.update_after_any_change()

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
