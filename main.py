import turtle
import pandas
import time

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def state_goto(x, y, state_name):
    state_turtle = turtle.Turtle()
    state_turtle.penup()
    state_turtle.hideturtle()
    state_turtle.goto(x, y)
    state_turtle.write(state_name)


data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    time.sleep(0.5)
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",
                                    prompt="What's another state name?")
    if answer_state.lower() == "exit":
        break
    if answer_state:
        answer_state = answer_state.title()
    if answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        state_goto(int(state_data.x), int(state_data.y), answer_state)

missed_states = [state for state in states if state not in guessed_states]
missed_states_dict = {"state": missed_states}

df = pandas.DataFrame(missed_states_dict)
df.to_csv("missed_states.csv")

screen.exitonclick()
