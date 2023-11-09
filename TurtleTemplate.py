# Import the Turtle Graphics module
import turtle
import random
import time

# Define program constants
WIDTH = 800
HEIGHT = 800
DELAY = 200
T_Size = 80
karma =0

offsets = {
    "up" :(0, 20),
    "down":(0, -20),
    "left":(-20, 0),
    "right":(20, 0)
}

def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("left"), "Left")
    screen.onkey(lambda: set_snake_direction("right"), "Right")

def set_snake_direction(direction):
    global snake_direction
    if direction == "up":
        if snake_direction != "down":
            snake_direction = "up"
    elif direction == "down":
        if snake_direction != "up":
            snake_direction = "down"
    elif direction == "left":
        if snake_direction != "right":
            snake_direction = "left"
    elif direction == "right":
        if snake_direction != "left":
            snake_direction = "right"

def game_loop():
        my_turtle.clearstamps()

        new_head = snake[-1].copy()
        new_head[0] += offsets[snake_direction][0] 
        new_head[1] += offsets[snake_direction][1]

        if new_head in snake or new_head[0] < -WIDTH/2 or new_head[0] > WIDTH / 2  \
            or new_head[1] < -HEIGHT/2 or new_head[1] > HEIGHT/2 :
            reset()
        else:
            snake.append(new_head)

            if not food_collision():
                snake.pop(0)
            for s in snake:
                my_turtle.goto(s[0],s[1])
                my_turtle.stamp()

            screen.title(f"Snake Game. Score: {score} Karma: {karma}, Rank: {get_karmic_rank()}")
            screen.update()

            turtle.ontimer(game_loop,DELAY)

def get_karmic_rank():
    global karma
    if karma > 10 or karma < -10:
        rank = "Trancendent"
    elif karma < 3 and karma > -3:
        rank = "Snake"
    elif karma <= 5 and karma >= 3:
        rank = "Holy Drake"
    elif karma <= 7 and karma >= 6:
        rank = "Celestial Dragon"
    elif karma <= 10 and karma > 7:
        rank = "Karmic Dragon God"
    elif karma >= -5 and karma <= -3:
        rank = "Darkness Drake"
    elif karma >= -7 and karma <= -6:
        rank = "Infernal Dragon"
    elif karma >= -10 and karma <= -8:
        rank = "Abyss Dragon God"
    return rank
def food_collision():
    global target_pos_b, target_pos_g, score, DELAY , karma
    if get_distance(snake[-1], target_pos_g) < T_Size/5+10:
        score +=1
        karma +=1
        DELAY -= 20
        target_pos_b = get_random_pos()
        target_pos_g = get_random_pos()
        target1.goto(target_pos_g)
        target2.goto(target_pos_b)
        return True
    elif get_distance(snake[-1], target_pos_b) < T_Size/2+10:
        score +=1
        DELAY -= 20
        karma -=1
        target_pos_b = get_random_pos()
        target_pos_g = get_random_pos()
        target1.goto(target_pos_g)
        target2.goto(target_pos_b)
        return True
    return False

def get_distance(p1, p2):
    x1,y1 = p1
    x2,y2 = p2
    return ((y2-y1)**2 + (x2-x1)**2) **0.5

def get_random_pos():
    x = random.randint(-WIDTH/2 + T_Size, WIDTH/2 - T_Size)
    y = random.randint(-HEIGHT/2+T_Size, HEIGHT/2 - T_Size)
    return (x,y)

        

def reset():
    global score, snake, snake_direction, target_pos_g, target_pos_b, DELAY, karma
    score =0
    DELAY = 200
    turtle.hideturtle()
    my_turtle.hideturtle()
    target1.hideturtle()
    target2.hideturtle()
    turtle.color("white")
    if karma < -3:
        screen.bgpic("EvilDragon.png")
        turtle.write(get_karmic_rank(), font=("Verdana",
                                    25, "normal"))
    elif karma > 3:
        screen.bgpic("GoodDragon.png")

        turtle.write(get_karmic_rank(), font=("Verdana",
                                    25, "normal"))
    else:
        screen.bgpic("snake.png")
        turtle.write(get_karmic_rank(), font=("Verdana",
                                    50, "normal"))
    screen.update()
    turtle.clear()
    turtle.color("black")
    time.sleep(4)
    turtle.showturtle()
    my_turtle.showturtle()
    target1.showturtle()
    target2.showturtle()
    karma = 0
    screen.bgpic("nopic")
    screen.update()

    snake = [[0,0], [20,0],[40,0],[60,0]]
    snake_direction = "down"
    target_pos_g = get_random_pos()
    target_pos_b = get_random_pos()
    target1.goto(target_pos_g)
    target2.goto(target_pos_b)
    game_loop()
    

# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Snake Game")
screen.bgcolor("Black")
screen.tracer(0)

#Add event handlers
screen.listen()
bind_direction_keys()




# Create a turtle to do your bidding
my_turtle = turtle.Turtle()
my_turtle.shape("circle")
my_turtle.color("white")
my_turtle.penup()

#Targets
target1 = turtle.Turtle()
target1.shape("circle")
target1.color("blue")
target1.shapesize(T_Size/50)
target1.penup()

target2 = turtle.Turtle()
target2.shape("circle")
target2.color("red")
target2.shapesize(T_Size/20)
target2.penup()


reset()

# This statement (or an equivalent) is needed at the end of all your turtle programs.
turtle.done()