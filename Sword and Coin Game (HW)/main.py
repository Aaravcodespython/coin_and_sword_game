import os

os.environ["SDL_VIDEO_WINDOW_POS"] = f"{50},{80}"

import pgzrun
import random

WIDTH = 1200
HEIGHT = 600

final_level = 10
start_level = 1
start_speed = 10
other_items = ["cartoon_arrow","cartoon_bomb","cartoon_sword"]
game_over = False
game_complete = False
items = []

def draw():
    screen.blit("cartoon_forest",(0,0))


pgzrun.go()