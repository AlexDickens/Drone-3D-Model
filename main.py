from ursina import *
import random

class RotatingRectangle(Entity):
    def __init__(self):
        super().__init__()
        self.model = 'quad'
        self.color = color.white
        self.scale = (3, 1)  
        self.rotation_speed = 10  
        self.rotation_angle = random.uniform(0, 0) 
        self.rotation_delay = 0 
        self.rotation_timer = 0  

    def update(self):
        self.rotation_timer += time.dt

        if self.rotation_timer >= self.rotation_delay:
            self.rotation_angle = random.uniform(0, 180)  # Set a new random rotation angle
            self.rotation = (0, 0, self.rotation_angle)

            if random.random() < 0.01:
                self.rotation_speed = random.uniform(-30, 30)  # Randomly change rotation speed

            self.rotation_timer = 0

app = Ursina()

rotating_rect = RotatingRectangle()

def update():
    rotating_rect.update()

app.run()
