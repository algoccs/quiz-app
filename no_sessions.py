from flask import Flask, redirect, url_for, session
from database import get_next_question

quiz, prev_question = 1, 0

app = Flask(__name__)

def index():
    global quiz, prev_question
    quiz = 1
    prev_question = 0
    return '<a href="/test">Click para iniciar el questionario!</a>'

def test():
    global prev_question
    result = get_next_question(prev_question, quiz)
    if result is None or result == 0:
        return redirect(url_for('result'))
    else:
        prev_question = result[0]
        return f'{result}'

def result():
    return 'Aqui se muestra el resultado!'

app.add_url_rule('/', 'index', index)
app.add_url_rule('/test', 'test', test)
app.add_url_rule('/result', 'result', result)

if __name__ == "__main__":
    app.run()
