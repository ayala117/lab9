import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Program")
screen.fill(WHITE)

drawing = False
shape = "circle"
color = BLACK
radius = 20
rect_start = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                shape = "circle"
            elif event.key == pygame.K_r:
                shape = "rectangle"
            elif event.key == pygame.K_e:
                shape = "eraser"
            elif event.key == pygame.K_s:
                shape = "square"
            elif event.key == pygame.K_t:
                shape = "right_triangle"
            elif event.key == pygame.K_y:
                shape = "equilateral_triangle"
            elif event.key == pygame.K_h:
                shape = "rhombus"
            elif event.key == pygame.K_1:
                color = BLACK
            elif event.key == pygame.K_2:
                color = RED
            elif event.key == pygame.K_3:
                color = GREEN
            elif event.key == pygame.K_4:
                color = BLUE

        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            if shape == "rectangle":
                rect_start = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if shape == "rectangle" and rect_start:
                rect_end = event.pos
                width = abs(rect_end[0] - rect_start[0])
                height = abs(rect_end[1] - rect_start[1])
                pygame.draw.rect(screen, color, (min(rect_start[0], rect_end[0]), min(rect_start[1], rect_end[1]), width, height))
                rect_start = None

        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                x, y = event.pos
                if shape == "circle":
                    pygame.draw.circle(screen, color, (x, y), radius)
                elif shape == "eraser":
                    pygame.draw.circle(screen, WHITE, (x, y), radius)
                elif shape == "square":
                    pygame.draw.rect(screen, color, (x - 20, y - 20, 40, 40))
                elif shape == "right_triangle":
                    points = [(x, y), (x - 20, y + 40), (x + 20, y + 40)]
                    pygame.draw.polygon(screen, color, points)
                elif shape == "equilateral_triangle":
                    points = [(x, y - 30), (x - 25, y + 15), (x + 25, y + 15)]
                    pygame.draw.polygon(screen, color, points)
                elif shape == "rhombus":
                    points = [(x, y - 25), (x - 25, y), (x, y + 25), (x + 25, y)]
                    pygame.draw.polygon(screen, color, points)

    pygame.display.flip()

pygame.quit()
