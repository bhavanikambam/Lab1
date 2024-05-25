from machine import Pin, PWM
import time

class Buzzer:
    def __init__(self, pin):
        self.buzzer = PWM(Pin(pin))

    def play_tone(self, frequency, duration):
        self.buzzer.freq(frequency)
        self.buzzer.duty_u16(1000)
        time.sleep(duration)
        self.buzzer.duty_u16(0)

    def happy_sound(self):
        self.play_tone(1000, 0.5)

    def sad_sound(self):
        self.play_tone(200, 1.0)

    def stop(self):
        self.buzzer.duty_u16(0)
