import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
guessed_states = []
unguessed_states = states
while len(guessed_states) < 50:
    size_g_s = len(guessed_states)
    answer_state = screen.textinput(title=f"{size_g_s}/50 states correct", prompt="What's another state's name?").title()
    print(answer_state)
    if answer_state == "Exit":
        break
    if answer_state in states and answer_state not in guessed_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color("black")
        row = data[data.state == answer_state]
        x = int(row.x)
        y = int(row.y)
        t.goto(x, y)
        t.write(answer_state)
        guessed_states.append(answer_state)
        unguessed_states.remove(answer_state)

    data2_dict = {"state": unguessed_states}
    data2 = pandas.DataFrame(data2_dict)
    data2.to_csv("states_to_learn.csv")






# turtle.mainloop()
