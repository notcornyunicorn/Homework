import datetime

from flask import Flask
from flask import url_for, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    urls = {'главная (эта страница)': url_for('index'),
            'опрос': url_for('stress')}
    return render_template('index.html', urls = urls)

@app.route('/stress')
def stress():
    if request.args:
        name = request.args['name']
        age = request.args['age']
        region = request.args['region']
        first_question = request.args['1question']
        second_question = request.args['2question']
        third_question = request.args['3question']
        fourth_question = request.args['4question']
        fifth_question = request.args['5question']
        sixth_question = request.args['6question']
        seventh_question = request.args['7question']
        eighth_question = request.args['8question']
        ninth_question = request.args['9question']
        tenth_question = request.args['10question']
    return render_template('question.html')

if __name__ == '__main__':
    app.run(debug=True)

