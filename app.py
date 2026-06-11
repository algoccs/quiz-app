from flask import Flask, redirect, url_for, session, request, render_template
from database import get_next_question, get_quises
from random import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SuperClaveSecreta'

def start_quiz(quiz_id):
    session['quiz'] = quiz_id
    session['prev_question'] = 0
    session['correct'] = 0
    session['totals'] = 0

def end_quiz():
    session.clear()

def check_answer():
    answer = request.form.get('ans_text')
    correct_answer = session.get('prev_correct_answer')

    if answer:
        session['totals'] += 1
        if answer == correct_answer:
            session['correct'] += 1

def cal_stats(correct, totals):
    if totals > 0:
        return round((correct / totals) * 100, 2)
    return 0

def index():
    if request.method == 'GET':
        start_quiz(-1)
        quises_list = get_quises()
        return render_template('index.html', quises=quises_list)
    else:
        quiz = request.form.get('quiz')
        start_quiz(quiz)
        return redirect(url_for('test'))

def test():
    if 'quiz' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        check_answer()

    result = get_next_question(session['prev_question'], session['quiz'])
    question_name = result[1]
    options = list(result[2:6]) # BARAJAR ESA LISTA CON SHUFFE
    # shuffle(options)

    if result is None or result == 1:
        return redirect(url_for('result'))

    session['prev_correct_answer'] = result[2]
    session['prev_question'] = result[0]

    return render_template('test.html',pregunta=question_name, opciones=options)


def result():
    if 'totals' not in session:
        end_quiz()
        return redirect(url_for('index'))

    totals = session['totals']
    correct = session['correct']
    incorrect = totals - correct
    percentage = cal_stats(correct, totals)

    return render_template('result.html',
                            totales=totals,
                            correctas=correct,
                            incorrectas=incorrect,
                            porcentaje=percentage
                            )
    

app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
app.add_url_rule('/test', 'test', test, methods=['GET', 'POST'])
app.add_url_rule('/result', 'result', result)

if __name__ == "__main__":
    app.run(debug=True)
