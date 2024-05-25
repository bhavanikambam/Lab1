from machine import Pin, I2C
from CharacterDisplay import CharacterDisplay
from ObstacleDisplay import ObstacleDisplay
from ScoreBoard import ScoreBoard
from Buzzer import Buzzer
from pico_i2c_lcd import I2cLcd
import time

class LCDDisplay:
    def __init__(self, sda_pin, scl_pin, buzzer_pin):
        i2c = I2C(0, sda=Pin(sda_pin), scl=Pin(scl_pin), freq=400000)
        self.lcd = I2cLcd(i2c, 0x27, 2, 16)
        self.character_display = CharacterDisplay(self)
        self.obstacle_display = ObstacleDisplay(self)
        self.score_board = ScoreBoard()
        self.buzzer = Buzzer(buzzer_pin)
        self.is_running = False

    def clear(self):
        self.lcd.clear()

    def show_welcome_message(self):
        self.clear()
        self.lcd.move_to(0, 0)
        self.lcd.putstr("Welcome to")
        self.lcd.move_to(0, 1)
        self.lcd.putstr("Dino Game!")
        time.sleep(3)  # Show the message for 3 seconds

    def run(self):
        self.is_running = True
        self.buzzer.happy_sound()
        self.show_welcome_message()  # Show welcome message before starting the game
        while self.is_running:
            self.clear()
            self.obstacle_display.update()
            self.character_display.update()
            self.check_collision()
            self.update_score()
            time.sleep(0.5)  # Game speed

    def check_collision(self):
        character_x, character_y = self.character_display.get_position()
        for obs_x, obs_y, obs_type in self.obstacle_display.get_obstacles():
            if obs_x == character_x and obs_y == character_y:
                self.is_running = False
                self.buzzer.sad_sound()
                self.score_board.display_final_score(self.lcd)
                return

    def update_score(self):
        character_x, character_y = self.character_display.get_position()
        for obs_x, obs_y, obs_type in self.obstacle_display.get_obstacles():
            if obs_x < character_x:
                self.score_board.increment()
                self.obstacle_display.obstacles.remove((obs_x, obs_y, obs_type))
                break  # Increment score only once per obstacle

    def reset(self):
        self.character_display.reset()
        self.obstacle_display.reset()
        self.score_board.reset()
        self.run()
