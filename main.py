import turtle
import pandas

screen = turtle.Screen()
screen.title("United States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
words = turtle.Turtle()
score = 0
guessed_states = []

data = pandas.read_csv('50_states.csv')
new_data = data.to_dict()
while score < 50:
    answer = screen.textinput(title=f'{score} / 50', prompt="What's another state? ").title()
    if answer == 'Exit':
        missing_states = [state for state in data['state'] if state not in guessed_states]
        new_states = pandas.DataFrame(missing_states)
        new_states.to_csv('states_to_learn.csv')
        break
    for state in data['state']:
        if answer == state:
            guessed_states.append(answer)
            x = int(data[data.state == answer].x)
            y = int(data[data.state == answer].y)
            words.hideturtle()
            words.penup()
            words.goto(x, y)
            words.write(state)
            score += 1

if score == 50:
    print("You Win!")
