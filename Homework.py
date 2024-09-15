

import pgzrun
from random import randint

WIDTH = 700
HEIGHT = 700

TITLE = "Shoot the Target"

message = ""

target = Actor("target.png")
target.scale=0.005
def draw():
    screen.fill(color=(204, 43, 178))
    target.draw()
    screen.draw.text(message, center=(300, 30), fontsize=30)

def place_target():
    target.x = randint(50, WIDTH - 50)
    target.y = randint(50, HEIGHT - 50)

def on_mouse_down(pos):
    global message
    if target.collidepoint(pos):
        message = "Good Shot"
        place_target()
    else:
        message = "Missed Shot"

# Place the target initially
place_target()

pgzrun.go()