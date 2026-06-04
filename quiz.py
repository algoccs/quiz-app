from flask import Flask, redirect, url_for, session, request, render_template
from database import get_next_question, get_quises

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SuperClaveSecreta'

def start_quiz(quiz_id):
    session['quiz'] = quiz_id
    session['prev_question'] = 0

def end_quiz():
    session.clear()

def index():
    if request.method == 'GET':
        quises_list = get_quises()
        return render_template('index.html', quises=quises_list)
    else:
        quiz = request.form.get('quiz')
        start_quiz(quiz)
        return redirect(url_for('test'))

def test():
    result = get_next_question(session['prev_question'], session['quiz'])
    if result is None or result == 0:
        return redirect(url_for('result'))
    else:
        session['prev_question'] = result[0]
        return f"<h1>Quiz: {session['quiz']} <br> {result[1]}</h1>"

def result():
    return 'Aqui se muestra el resultado!'

app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
app.add_url_rule('/test', 'test', test)
app.add_url_rule('/result', 'result', result)

if __name__ == "__main__":
    app.run(debug=True)