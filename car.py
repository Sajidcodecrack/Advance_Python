import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Racing Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Car properties
car_width = 50
car_height = 100
car_x = width // 2 - car_width // 2
car_y = height - car_height - 10
car_speed = 5

# Enemy properties
enemy_width = 50
enemy_height = 50
enemy_speed = 5

# Clock
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont(None, 55)

def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()

def message_display(text):
    large_text = pygame.font.Font(None, 80)
    TextSurf, TextRect = text_objects(text, large_text)
    TextRect.center = ((width / 2), (height / 2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()
    pygame.time.wait(2000)

    game_loop()

def crash():
    message_display("You Crashed!")

def game_loop():
    global car_x  # Declare car_x as a global variable
    car_x_change = 0

    # Enemy starting position
    enemy_x = random.randrange(0, width - enemy_width)
    enemy_y = -enemy_height

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car_x_change = -car_speed
                elif event.key == pygame.K_RIGHT:
                    car_x_change = car_speed

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    car_x_change = 0

        car_x += car_x_change

        # Boundaries for the car
        if car_x < 0:
            car_x = 0
        elif car_x > width - car_width:
            car_x = width - car_width

        # Update enemy position
        enemy_y += enemy_speed

        # Draw everything on the screen
        screen.fill(white)
        pygame.draw.rect(screen, black, [car_x, car_y, car_width, car_height])
        pygame.draw.rect(screen, black, [enemy_x, enemy_y, enemy_width, enemy_height])

        # Check for collision
        if car_y < enemy_y + enemy_height:
            if car_x > enemy_x and car_x < enemy_x + enemy_width or car_x + car_width > enemy_x and car_x + car_width < enemy_x + enemy_width:
                crash()

        # If enemy goes off the screen, reset its position
        if enemy_y > height:
            enemy_y = -enemy_height
            enemy_x = random.randrange(0, width - enemy_width)

        pygame.display.update()
        clock.tick(60)

# Start the game loop
game_loop()
