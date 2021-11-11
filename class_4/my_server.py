from flask import Flask, request

app = Flask("something")


@app.route('/whatismyname', methods=['GET', 'POST', 'DELETE'])
def hello():
    my_score = 1
    if request.method == 'GET':
        return "mazda, citroen, chevrolet"
    elif request.method == 'POST':
        return "saved new car"
    else:
        return "<h1>" + str(my_score) + "</h1>"

@app.route('/')
def my_func():
    return "hello and welcome to the world of games"

@app.route('/cars')
def hello():
    my_score = 1
    if request.method == 'GET':
        return "c'est mes voitures"
    elif request.method == 'POST':
        return "saved new car"
    else:
        return "<h1>" + str(my_score) + "</h1>"


app.run(host="0.0.0.0", port=5001, debug=True)