import logging
import logging.config
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


def reset_frame(screen):
    screen.fill((255, 255, 255))
    pygame.display.update()


def main():
    """Main Game Function"""

    DEBUG = False

    logging.config.fileConfig('logging/log_settings.conf')
    # logging.info("Beginning Script")

    pygame.init()
    gameDisplay = pygame.display.set_mode((800,600))
    pygame.display.set_caption('CONNECT 4')

    running = True
    while running:

        # Quit Application
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Toggle Debug
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F3:
                    DEBUG = not DEBUG

            reset_frame(gameDisplay)

            Mouse_x, Mouse_y = pygame.mouse.get_pos()
            if DEBUG:
                font = pygame.font.Font(pygame.font.get_default_font(), 24)
                text_surface = font.render('X:{} Y:{}'.format(Mouse_x, Mouse_y), True, (0, 0, 0))
                gameDisplay.blit(text_surface, (0,0))
                pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
