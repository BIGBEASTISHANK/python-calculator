from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
        equation = str(request.form['equation'])
        result = str(eval(equation))
        return render_template('webcalc.html', result=f'Result: {result}')
    return render_template('index.html')

app.run(debug=True)
