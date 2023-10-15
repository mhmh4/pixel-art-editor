import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

CANVAS_WIDTH = 200
CANVAS_HEIGHT = 300
CANVAS_PIXEL_SIZE = 25


class Canvas:
    def __init__(self, width, height, pixel_size):
        self.width = width
        self.height = height
        self.pixel_size = pixel_size

        self.pixels = [
            ["#ffffff" for _ in range(self.width // self.pixel_size)]
            for _ in range(self.height // self.pixel_size)
        ]

    def draw(self, screen):
        x = 0
        y = 0
        for row in self.pixels:
            x = 0
            for color in row:
                pygame.draw.rect(
                    screen, color, pygame.Rect(x, y, self.pixel_size, self.pixel_size)
                ),
                pygame.draw.rect(
                    screen,
                    "gray",
                    pygame.Rect(x, y, self.pixel_size, self.pixel_size),
                    1,
                ),
                x += self.pixel_size
            y += self.pixel_size

    def fill(self, pos):
        i = pos[1] // self.pixel_size
        j = pos[0] // self.pixel_size
        if i < 0 or i >= len(self.pixels) or j < 0 or j >= len(self.pixels[0]):
            return
        self.pixels[i][j] = "#000000"


class ColorPicker:
    COLOR_PREVIEW_SIZE = 20

    def __init__(self):
        self.colors = ["black", "red", "blue", "green"]

    def draw(self, screen):
        x = 0
        for color in self.colors:
            pygame.draw.rect(
                screen, color, pygame.Rect(x, CANVAS_HEIGHT, self.COLOR_PREVIEW_SIZE, self.COLOR_PREVIEW_SIZE)
            )
            x += self.COLOR_PREVIEW_SIZE


def run():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT, CANVAS_PIXEL_SIZE)
    color_picker = ColorPicker()

    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            mouse_state = pygame.mouse.get_pressed()
            if mouse_state[0]:
                pos = pygame.mouse.get_pos()
                canvas.fill(pos)

            screen.fill("white")

            canvas.draw(screen)
            color_picker.draw(screen)

            pygame.display.flip()

            clock.tick(60)
    except KeyboardInterrupt:
        print()
        pass
    finally:
        pygame.quit()


if __name__ == "__main__":
    run()
