README for app.py

Note: All tests were conducted on zsh shell with app.py running on localhost port 5000

Description: Project allows three POST endpoints that do the following:

1

/is-point-covered
Inputs: a point in the JSON format {"x":"(int)","y":"(int)"}
Outputs: boolean value

Tests:
# curl -d '{"x":"3","y":"4"}' -H 'Content-Type: application/json' -X POST localhost:5000/is-point-covered
# returns false

# curl -d '{"x":"5","y":"10"}' -H 'Content-Type: application/json' -X POST localhost:5000/is-point-covered
#returns true

2

/point-covered-by
Inputs: a point in the JSON format {"x":"int","y":"int"}
Outputs: JSON container with the ids of the rectangles that the point is on

Tests:
# curl -d '{"x":"5","y":"10"}' -H 'Content-Type: application/json' -X POST localhost:5000/point-covered-by
# returns Rectangle id 1

# curl -d '{"x":"9","y":"5"}' -H 'Content-Type: application/json' -X POST localhost:5000/point-covered-by
# returns Rectangle ids 1,2

# curl -d '{"x":"40","y":"25"}' -H 'Content-Type: application/json' -X POST localhost:5000/point-covered-by
# returns Rectangle id 3

# curl -d '{"x":"1","y":"1"}' -H 'Content-Type: application/json' -X POST localhost:5000/point-covered-by
# returns an empty list

3

/random-covered-point
Inputs: A valid rectangle in JSON dict with keys x1,x2,y1,y2
Outputs: A random point in the JSON container with two int values

Tests: 
# curl -d '{Rectangle}' -H 'Content-Type: application/json' -X POST localhost:5000/random-covered-point
# Replace Rectangle with your points
# {"y2":"4","x1":"1","y1":"1","x2":"4"}
Returns a random point
# {"y2":"0","x1":"0","y1":"0","x2":"0"}
Returns error