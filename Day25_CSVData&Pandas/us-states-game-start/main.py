from turtle import Turtle, Screen
import pandas as pd
import turtle


def add_state(state_name, x, y):
    state = Turtle(visible=False)
    state.penup()
    state.speed('fastest')
    state.goto(x, y)
    state.write(arg=state_name, move=False, align='center')
    states_guessed.append((state, state_name))


states_guessed = []

states_info = pd.read_csv(
    r'Day25_CSVData&Pandas\us-states-game-start\50_states.csv')
states_names = states_info.state.to_list()

screen = Screen()
screen.title("U.S. States Game")
image = r"Day25_CSVData&Pandas\us-states-game-start\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(
    title="Guess the State", prompt="What's another state's name?").title()

while len(states_guessed) < 50:

    if answer_state == 'Exit':
        states_list = [state[1] for state in states_guessed]
        states_to_learn = [
            state for state in states_names if state not in states_list]
        new_df = pd.DataFrame(states_to_learn)
        save_path = r'Day25_CSVData&Pandas\us-states-game-start\states_to_learn.csv'
        new_df.to_csv(save_path)
        break

    if answer_state in states_names:
        state_row = states_info[states_info.state == answer_state]
        x_coord, y_coord = int(
            state_row.x.item()), int(state_row.y.item())
        add_state(answer_state, x_coord, y_coord)
    answer_state = screen.textinput(
        title=f"{len(states_guessed)}/50 States Correct", prompt="What's another state's name?").title()
