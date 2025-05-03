import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)

        angle_a = self.velocity.rotate(angle)
        angle_b = self.velocity.rotate(angle * -1)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_asteroid.velocity = angle_a * 1.2
        second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_asteroid.velocity = angle_b * 1.2