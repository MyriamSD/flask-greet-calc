# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def one_add(a, b):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)
    



@app.route('/sub')
def two_sub(a, b):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a, b)
    return str(result)



@app.route('/mult')
def three_mult():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a, b)
    return str(result)


@app.route('/div')
def four_div():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a, b)
    return str(result)


operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }
"""
1.Make a dictionairy with keys that correspond to the imported operation
2.Create route with a dynamic variabe for the url
3. define function that takes one parameter 'oper'
4. a is equal to the integer version of whatever is passed into 'a' during search
5. b is equal to the integer version of whatever is passed into 'b' during search
  for results:
6. Oper will be passed into brackets to retrieve the value of opratoes which corresponds to a function imported from operations.py
7. (a, b) is added as the parameters for the extracted function
8. return the result as a string
"""

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)