import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    BLACK = (0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(BLACK)     # <- fixed: call fill on screen, not standalone
        pygame.display.flip()  # <- needed to actually show the fill

if __name__ == "__main__":
    main()
