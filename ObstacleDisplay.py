import random

class ObstacleDisplay:
    def __init__(self, lcd_display):
        self.lcd = lcd_display.lcd
        self.obstacles = []
        self.max_x = 15  # Maximum x-coordinate for obstacles
        self.tree_char = [
            0b00100,
            0b01110,
            0b11111,
            0b00100,
            0b00100,
            0b00100,
            0b00100,
            0b00000
        ]
        self.bird_char = [
            0b00000,
            0b01110,
            0b10101,
            0b11111,
            0b01110,
            0b00100,
            0b00000,
            0b00000
        ]
        self.lcd.custom_char(1, bytearray(self.tree_char))
        self.lcd.custom_char(2, bytearray(self.bird_char))
        self.add_obstacle()

    def add_obstacle(self):
        obs_type = random.choice([1, 2])  # 1 for tree, 2 for bird
        y = 1 if obs_type == 1 else 0  # Tree on bottom, bird on top
        self.obstacles.append((self.max_x, y, obs_type))

    def update(self):
        new_obstacles = []
        for (x, y, obs_type) in self.obstacles:
            if x > 0:
                new_obstacles.append((x - 1, y, obs_type))
        self.obstacles = new_obstacles
        if len(self.obstacles) == 0 or (self.obstacles[-1][0] < self.max_x - 5):
            self.add_obstacle()
        self.draw()

    def draw(self):
        for (x, y, obs_type) in self.obstacles:
            self.lcd.move_to(x, y)
            self.lcd.putchar(chr(obs_type))

    def get_obstacles(self):
        return self.obstacles

    def reset(self):
        self.obstacles = []
