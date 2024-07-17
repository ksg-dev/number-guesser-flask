from flask import Flask
import random

app = Flask(__name__)
TARGET = random.randint(0, 9)


@app.route("/<int:number>")
def check_number(number):
    global TARGET
    if number > TARGET:
        return("<h1 style='color:purple;'>Too high! Try again!</h1>"
               "<img src='https://media2.giphy.com/media/QyVGDyUsyMEPd7Ktqi/200.webp?cid=ecf05e47n6us6q83oflrs4n3r00rpr8n8la7tdf08x2mgy10&ep=v1_gifs_search&rid=200.webp&ct=g'>")
    if number < TARGET:
        return("<h1 style='color:red;'>Too low! Try again!</h1>"
               "<img src='https://media4.giphy.com/media/YmQLj2KxaNz58g7Ofg/giphy.webp?cid=790b76110dwpc02hhugqwrkt7bpljvrlgy63jh88grp8qliz&ep=v1_gifs_search&rid=giphy.webp&ct=g'>")
    elif number == TARGET:
        return ("<h1 style='color:green;'>Great job! You found me!</h1>"
                "<img src='https://media0.giphy.com/media/5xZoxXPRfSvZsxkD0Y/200.webp?cid=ecf05e47lcb4qos4a5ehwyyfisn2j4zvcuyr8yz4ym1a2a4f&ep=v1_gifs_search&rid=200.webp&ct=g'>")

@app.route("/")
def hello():
    print(TARGET)
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media0.giphy.com/media/fDUOY00YvlhvtvJIVm/giphy.webp?cid=ecf05e47ss94in3pyi0zdrylrltb5hv4f6rvexqnsx6nbg5u&ep=v1_gifs_search&rid=giphy.webp&ct=g'>")

if __name__ == "__main__":
    app.run(debug=True)