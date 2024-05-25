class ScoreBoard:
    def __init__(self):
        self.score = 0

    def increment(self):
        self.score += 1

    def reset(self):
        self.score = 0

    def display_final_score(self, lcd):
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr("Game Over")
        lcd.move_to(0, 1)
        lcd.putstr(f"Score: {self.score}")
