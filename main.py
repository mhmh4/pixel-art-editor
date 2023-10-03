# Example file showing a basic pygame "game loop"
import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

PIXEL_SIZE = 25


class Canvas:
    def __init__(self, width, height, pixel_size):
        self.width = width
        self.height = height
        self.pixel_size = pixel_size

        self.pixels = [
            ["#ffffff" for _ in range(self.height // self.pixel_size)]
            for _ in range(self.width // self.pixel_size)
        ]

    def draw(self, screen):
        for x in range(0, self.width, self.pixel_size):
            for y in range(0, self.height, self.pixel_size):
                pygame.draw.rect(
                    screen,
                    "gray",
                    pygame.Rect(x, y, self.pixel_size, self.pixel_size),
                    1,
                )


# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

canvas = Canvas(200, 300, 25)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    canvas.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
