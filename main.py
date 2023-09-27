# Example file showing a basic pygame "game loop"
import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

PIXEL_SIZE = 25


def draw_canvas(screen):
    for x in range(0, SCREEN_WIDTH, PIXEL_SIZE):
        for y in range(0, SCREEN_HEIGHT, PIXEL_SIZE):
            pygame.draw.rect(
                screen, "gray", pygame.Rect(x, y, PIXEL_SIZE, PIXEL_SIZE), 1
            )


# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    draw_canvas(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
