import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import (
     
        LINE_WIDTH,
        ASTEROID_MIN_RADIUS
        )

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
       self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        
        new_angle = random.uniform(20, 50)
        split_a_vector = self.velocity.rotate(new_angle)
        split_b_vector = self.velocity.rotate(0 - new_angle)
        split_radius = self.radius - ASTEROID_MIN_RADIUS  
        
        split_a = Asteroid(self.position[0], self.position[1], split_radius)
        split_a.velocity = split_a_vector * 1.2
        split_b = Asteroid(self.position[0], self.position[1], split_radius)
        split_b.velocity = split_b_vector * 1.2
        

