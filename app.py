from flask import Flask, render_template, request, jsonify
import sympy as sp
from solver import *

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    if(request.method == "GET"):
        return render_template('index.html')
    else:

        p_str = request.form['P']
        q_str = request.form['Q']
        n = float(request.form['n'])
        x_val = request.form['x']
        y_val = request.form['y']
        # print("p: ", p_str)
        # print("Q: ", q_str)
        # print("N: " ,n)
        # print("y val" ,y_val)
        solve = solve_func(p_str, q_str, n)
        if(len(x_val) != 0 and len(y_val) != 0):
            solve = solve_func_w_value(p_str, q_str, n, x_val, y_val)
        

        # print(solve)
        return render_template("solution.html", eqn = "eqn", soln = solve)


# @app.route('/process_input', methods=['POST', "GET"])
# def process_input():
#     data = request.json

#     p_str = data['P']
#     q_str = data['Q']
#     n = float(data['n'])
#     x_val = data['x']
#     y_val = data['y']
#     print("y val" ,y_val)
#     p_eq = sp.sympify(p_str)
#     q_eq = sp.sympify(q_str)


#     response = {
#         'error': '',
#         'eq': 'Your Equation',
#         'order': 'Order of the Equation',
#         'ans': 'Solution',
#         'partAns': 'Partial Solution'
#     }

#     return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
