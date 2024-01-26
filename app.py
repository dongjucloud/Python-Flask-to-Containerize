# app.py

from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'

@app.route('/home')
def home():
    if 'username' in session:
        return redirect(url_for('play_game'))
    else:
        return render_template('index.html', title='Let`s play flask-game', content='welcome!')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('play_game'))
    else:
        return render_template('login.html', title='Login')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/play_game', methods=['GET', 'POST'])
def play_game():

    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        guess = int(request.form['guess'])
        target_number = session.get('target_number', -1)

        if target_number == -1:
            target_number = random.randint(1, 100)
            session['target_number'] = target_number

        if guess == target_number:
            result = 'Congratulations! You guessed the correct number.'
            session.pop('target_number', None)
        elif guess < target_number:
            result = 'Try again! The number is higher.'
        else:
            result = 'Try again! The number is lower.'

        return render_template('play_game.html', title='Play Game', result=result)

    return render_template('play_game.html', title='Play Game', result=None)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
