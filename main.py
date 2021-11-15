import pandas
data = pandas.read_csv("50_states.csv")
print(data)
states = data["state"].to_list()

import turtle
from turtle import Turtle,Screen
s = Screen()
s.title("US states")
# s.shape
image = "blank_states_img.gif"

s.addshape(image)
turtle.shape(image)
s.listen()
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)


t = Turtle()
t.speed("fastest")
t.hideturtle()
state_number = data["state"].to_list()
guessed_state = []
for i in range(0,len(data)):
    statename = s.textinput(f"{len(guessed_state)}/50 Guessed Correct","Name of State")

    if statename=="Exit":
        break
    if statename in states:
        guessed_state.append(statename)
        state_number.remove(statename)
        df = data[data.state == statename]
        df = df.reset_index()
        print(df)
        t.penup()
        t.goto(df.loc[0, "x"], df.loc[0, "y"])
        t.pendown()
        t.write(statename)

d = pandas.DataFrame(state_number)
d.to_csv("remaining.csv")


# s.exitonclick()
turtle.mainloop()
