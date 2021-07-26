from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        oop = request.form['operator']

        if oop == 'Add':
            result = num1 + num2
        elif oop == 'Multiply':
            result = num1 * num2
        elif oop == 'Substract':
            result = num1 - num2
        else:
            result = num1 // num2
        return render_template('index.html', result=f'Result = {result}')

    return render_template('index.html')

app.run(debug=True)
