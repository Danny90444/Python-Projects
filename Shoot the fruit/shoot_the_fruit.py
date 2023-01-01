import pgzrun
from random import randint

apple = Actor("apple")
pineapple = Actor("pineapple")
orange = Actor("orange")
score = 0


fruits = [apple, pineapple, orange]

def draw():
    screen.clear()
    apple.draw()
    pineapple.draw()
    orange.draw()
    


def place_apple():
    for fruit in fruits:
       fruit.x = randint(10, 800)
       fruit.y = randint(10, 600)
       

def on_mouse_down(pos):
    global score
    if apple.collidepoint(pos):
        score += 1
        print("Good Shot!\n Score = {}".format(score))
        place_apple()
            
    else:
       score -= 1 
       print("Score = {}".format(score))
       place_apple()
 


place_apple()

pgzrun.go()