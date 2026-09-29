from flask import Flask, render_template, request
from calculator_logic import add, subtract, multiply, divide

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        num1 = float(request.form["num1"])
        op = request.form["op"]
        num2 = float(request.form["num2"])

        if op == "+":
            result = add(num1, num2)
        elif op == "-":
            result = subtract(num1, num2)
        elif op == "*":
            result = multiply(num1, num2)
        elif op == "/":
            result = divide(num1, num2)
        else:
            result = "Invalid operator"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)