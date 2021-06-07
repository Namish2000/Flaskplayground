# Developer: Namish Gali
# Date: 2021/02/18
# System Config:
#   Architecture: AArch64; ARMv8-A with x86-64 emulation
#   OS: MacOS 11
#   Terminal: zsh
#   Python version: 3.9.1
#   Flask version: 1.1.2
#   Werkzeug version: 1.0.1

# To launch application: python3 app.py
# App should run on port 5000 localhost or equivalent

from flask import Flask, request, jsonify
import random
import time

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/')
def home():
    return 'Enter an endpoint to use application :)'

class Point:
    """A class to declare a point object with x and y"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

class Rectangle:
    """ A class to manufacture rectangle objects """
    def __init__(self, *args):
        """ Initialize the Rectangle with or without a provided ID"""
        if len(args) == 3:
            self.id = args[0]
            self.top_left = args[1]
            self.bottom_right = args[2]
        elif len(args) == 2:
            self.id = None
            self.top_left = args[0]
            self.bottom_right = args[1]
        else:
            raise Exception("Enter 3 or 4 arguments")

    # get the top left coordinate
    def getTL(self):
        return self.top_left

    # get the bottom right coordinate
    def getBR(self):
        return self.bottom_right

    # get ID
    def getID(self):
        return self.id

# Global declarations of Rectangle models
endpoint1_rectangle = Rectangle(Point(5, 10), Point(10, 5))

endpoint2_rectangles = [Rectangle(1, Point(5, 10), Point(10, 5)),
                        Rectangle(2, Point(7, 7), Point(20, 2)),
                        Rectangle(3, Point(33, 45), Point(52, 23))]

# Is the point covered by endpoint1_rectangle
# Input: Positive integers
# Output: True/False
@app.route('/is-point-covered', methods=['POST'])
def is_point_covered():
    known_r = endpoint1_rectangle
    content = request.json
    x = int(content["x"])
    y = int(content["y"])
    # Inputs must be positive
    if x < 0 or y < 0:
        raise Exception("Invalid Point Coordinates")
    if request.method == 'POST':
        if (known_r.getTL().getx() <= x) and (known_r.getBR().getx() >= x) and (
                known_r.getTL().gety() >= y) and (known_r.getBR().gety() <= y):
            return jsonify(True)
        else:
            return jsonify(False)

# Do any endpoint2_rectangles cover the point
# Input: Positive integers
# Output: list of rectangle ids
@app.route('/point-covered-by', methods=['POST'])
def point_covered_by():
    content = request.json
    x = int(content["x"])
    y = int(content["y"])
    if x < 0 or y < 0:
        raise Exception("Invalid Point Coordinates")
    ids = []
    if request.method == 'POST':
        # Cycles through endpoint2_rectangles container and tests to see if points are within the rectangle bounds
        for i in range(len(endpoint2_rectangles)):
            if (endpoint2_rectangles[i].getTL().getx() <= x) and (endpoint2_rectangles[i].getBR().getx() >= x) and (
                    endpoint2_rectangles[i].getTL().gety() >= y) and (endpoint2_rectangles[i].getBR().gety() <= y):
                ids.append(endpoint2_rectangles[i].getID())
    return jsonify("Covered by Rectangle ID:", ids)

# Random point inside a rectangle
# Input: Valid points given with JSON dictionary keys: x1,x2,y1,y2
# Output: random x and y coordinate
@app.route('/random-covered-point', methods=['POST'])
def random_covered_point():
    if request.method == 'POST':
        content = request.json
        x1 = int(content["x1"])
        y1 = int(content["y1"])
        x2 = int(content["x2"])
        y2 = int(content["y2"])
        if x1 < 0 or y1 < 0:
            raise Exception("Invalid Rectangle Points")
        # Checks if points make valid rectangle
        if x2 <= x1 or y2 <= y1:
            raise Exception("Invalid Rectangle Points")
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        return jsonify(x, y)

if __name__ == '__main__':
    app.run(debug=True)
