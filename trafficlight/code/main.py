from machine import Pin, PWM
from time import sleep

red_led = Pin(20, Pin.OUT)
yellow_led = Pin(19, Pin.OUT)
green_led = Pin(18, Pin.OUT)


button = Pin(14, Pin.IN, Pin.PULL_DOWN)

RED = 0
RED_AMBER = 1
GREEN = 2
AMBER = 3

current_state = RED

def update_lights(state):
    if state == RED:
        red_led.value(1)
        yellow_led.value(0)
        green_led.value(0)
    elif state == RED_AMBER:
        red_led.value(1)
        yellow_led.value(1)
        green_led.value(0)
    elif state == GREEN:
        red_led.value(0)
        yellow_led.value(0)
        green_led.value(1)
    elif state == AMBER:
        red_led.value(0)
        yellow_led.value(1)
        green_led.value(0)

def next_state():
    global current_state
    if current_state == RED:
        current_state = RED_AMBER  # Red & Amber after red
    elif current_state == RED_AMBER:
        current_state = GREEN  # Green follows r & a 
    elif current_state == GREEN:
        current_state = AMBER  # Amber follows green
    elif current_state == AMBER:
        current_state = RED  # Red follows amber
    update_lights(current_state)

while True:
    if button.value() == 1:
        next_state()  
        sleep(0.5)  

    sleep(0.1)  

