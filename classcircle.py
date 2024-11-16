import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Draw Circles")

# Define the Circle class
class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Create three circle instances
circle1 = Circle(200, 150, 50, (255, 0, 0))  # Red circle
circle2 = Circle(400, 300, 75, (0, 255, 0))  # Green circle
circle3 = Circle(600, 450, 100, (0, 0, 255)) # Blue circle

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with white
    screen.fill((255, 255, 255))

    # Draw the circles
    circle1.draw(screen)
    circle2.draw(screen)
    circle3.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
