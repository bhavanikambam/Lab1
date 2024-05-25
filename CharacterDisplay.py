class CharacterDisplay:
    def __init__(self, lcd_display):
        self.lcd = lcd_display.lcd
        self.x = 0
        self.y = 1  # Bottom line of the display
        self.char = [
            0b00000,
            0b00100,
            0b00100,
            0b00100,
            0b11111,
            0b10101,
            0b00100,
            0b01010
        ]
        self.lcd.custom_char(0, bytearray(self.char))

    def update(self):
        self.draw(self.x, self.y)

    def draw(self, x, y):
        self.lcd.move_to(x, y)
        self.lcd.putchar(chr(0))  # Custom character for the human

    def get_position(self):
        return self.x, self.y

    def reset(self):
        self.x = 0
        self.y = 1
