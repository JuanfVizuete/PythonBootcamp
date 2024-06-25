import turtle
import pandas


def write_state(x, y, answer_state):
    #print(x, y)
    turtle_state = turtle.Turtle()
    turtle_state.penup()
    turtle_state.hideturtle()
    turtle_state.goto(x, y)
    turtle_state.write(answer_state)


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states_file = pandas.read_csv("50_states.csv")
states_dict = states_file.to_dict()
#print(states_dict)
states = states_file.state.to_list()
print(states)
correct_answers = []
title_guess = "Guess the State"
game_is_on = True

while game_is_on:
    # Windows to enter the name of the state to make a guess
    answer_state = screen.textinput(title=title_guess, prompt="What's another state's name?").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in correct_answers:
                missing_states.append(state)
        #print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        if answer_state not in correct_answers:
            correct_answers.append(answer_state)
            print("Correct answer")
            title_guess = f"{len(correct_answers)}/50 States Correct"
            states_data = states_file[states_file.state == answer_state]
            write_state(int(states_data.x), int(states_data.y), answer_state)
        else:
            print("You already guessed that state")
    else:
        print("Invalid answer")
    if len(correct_answers) == len(states):
        print("You finished! Congratulations!")
        game_is_on = False

# states to learn.csv



# TO GET THE COORDINATES OF EACH STATEBY MOUSE CLICK
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

screen.exitonclick()