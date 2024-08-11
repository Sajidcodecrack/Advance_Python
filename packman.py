import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pac-Man")

# Colors
yellow = (255, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# Pac-Man properties
pacman_radius = 30
pacman_angle = 45  # Initial angle of Pac-Man's mouth
pacman_speed = 5
pacman_direction = "right"

# Object properties
object_radius = 20
object1_position = [random.randint(50, width-50), random.randint(50, height-50)]
object2_position = [random.randint(50, width-50), random.randint(50, height-50)]

clock = pygame.time.Clock()

def draw_pacman(x, y):
    pygame.draw.circle(win, yellow, (x, y), pacman_radius)
    if pacman_direction == "right":
        pygame.draw.polygon(win, black, [(x, y)] + get_mouth_points(x, y, pacman_angle))

def draw_objects():
    pygame.draw.circle(win, red, (object1_position[0], object1_position[1]), object_radius)
    pygame.draw.circle(win, blue, (object2_position[0], object2_position[1]), object_radius)

def get_mouth_points(x, y, angle):
    points = []
    for i in range(-angle, angle + 1):
        radians = math.radians(i)
        points.append((x + int(pacman_radius * math.cos(radians)), y + int(pacman_radius * math.sin(radians))))
    return points

def check_collision(x1, y1, x2, y2, radius):
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance < pacman_radius + radius

def game_loop():
    global pacman_angle
    x, y = width // 2, height // 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > pacman_radius:
            x -= pacman_speed
            pacman_direction = "left"
        if keys[pygame.K_RIGHT] and x < width - pacman_radius:
            x += pacman_speed
            pacman_direction = "right"
        if keys[pygame.K_UP] and y > pacman_radius:
            y -= pacman_speed
            pacman_direction = "up"
        if keys[pygame.K_DOWN] and y < height - pacman_radius:
            y += pacman_speed
            pacman_direction = "down"

        # Check collision with objects
        if check_collision(x, y, object1_position[0], object1_position[1], object_radius):
            object1_position = [random.randint(50, width-50), random.randint(50, height-50)]
        if check_collision(x, y, object2_position[0], object2_position[1], object_radius):
            object2_position = [random.randint(50, width-50), random.randint(50, height-50)]

        win.fill(black)
        draw_objects()
        draw_pacman(x, y)

        pygame.display.flip()
        clock.tick(30)

game_loop()
