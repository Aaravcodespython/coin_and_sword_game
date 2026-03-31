import os

os.environ["SDL_VIDEO_WINDOW_POS"] = f"{50},{80}"

import pgzrun
import random

WIDTH = 1200
HEIGHT = 600

final_level = 10
start_level = 1
start_speed = 10
hazards = ["cartoon_arrow","cartoon_bomb","cartoon_sword","cartoon_shuriken","cartoon_spiky_ball","cartoon_cannonball","cartoon_boulder"]
game_over = False
game_complete = False
items = []
animations = []

def draw():
    global game_over,game_complete,start_level,items

    screen.blit("cartoon_forest",(0,0))

    if game_over == True:
        screen.draw.text("Game Over, you lose!",center = (WIDTH//2,HEIGHT//2),color = "red",fontsize = 150)
    
    elif game_complete == True:
        screen.draw.text("You Win!",center = (WIDTH//2,HEIGHT//2),color = "green",fontsize = 300)

    else:
        for item in items:
            item.draw()

def make_actors(num_hazards):
    #selecting the random images for actors
    actors_to_make = ["cartoon_coin"]
    for i in range(num_hazards):
        actors_to_make.append(random.choice(hazards))

    #creating actors using the selected images   
    new_actors = []
    for img in actors_to_make:
        actor = Actor(img)
        new_actors.append(actor)
    
    #positioning the actors based on gaps
    num_gap = len(new_actors)+1

        

pgzrun.go()
