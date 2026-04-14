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

    #random.shuffle(actors_to_make)
    #print(actors_to_make)

    #creating actors using the selected images   
    new_actors = []
    for img in actors_to_make:
        actor = Actor(img)
        new_actors.append(actor)
    
    #positioning the actors based on gaps
    num_gap = len(new_actors)+1
    gap_size = WIDTH//num_gap
    
    #shuffling new_actors list
    random.shuffle(new_actors)
    
    #using for loop to set coordinate of each actor by their index number and their gap size
    #enumerate() is a function applied on a list to get the list item and its index number
    for index,actor in enumerate(new_actors):
        x_pos = (index+1)*gap_size
        actor.x = x_pos
        actor.y = 0
    
    animate_actors(new_actors)

    return new_actors

def handle_game_over():
    global game_over
    game_over = True

def handle_game_complete():
    global start_level,game_complete,items,animations
    stop_animation(animations)
    if start_level == final_level:
        game_complete = True
    else:
        items = []
        animations = []
        start_level += 1


#function for animating the actors
def animate_actors(actors_to_animate):
    global animations
    
    for actor in actors_to_animate:
        current_speed = start_speed - start_level
        actor.anchor = ("center","bottom")
        animation = animate(actor,duration = current_speed,on_finished = handle_game_over,y = HEIGHT)
        animations.append(animation)    

def stop_animation(actors_to_stop_animation):
    actors_to_stop_animation

    for actor in actors_to_stop_animation:
        if actor.running:
            actor.stop()


def update():
    global items
    if len(items) == 0:
        items = make_actors(start_level)

def on_mouse_down(pos):
    global items, start_level

    for item in items:
        if item.collidepoint(pos):
            if "cartoon_coin" in item.image:
                handle_game_complete()
            else:
                handle_game_over()

pgzrun.go()
