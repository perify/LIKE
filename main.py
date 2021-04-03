from flask import request, render_template, Flask, redirect

import tlsql
import login

app = Flask(__name__)
app.secret_key = 'fadjksjladsfa'


@app.route('/', methods=['GET', 'POST'])
def home():
    if not login.is_login():
        return redirect('/sign_in')
    tweets = []

    if request.method == 'GET':
        for i in tlsql.view():
            tweets.append(i)
        return render_template('home.html', tweets=tweets)

    if request.method == 'POST':
        if not request.form['message']:
            for i in tlsql.view():
                tweets.append(i)
            return render_template('home.html', tweets=tweets)
        tlsql.tweet(request.form['message'], login.get_user())
        for i in tlsql.view():
            tweets.append(i)
        return render_template('home.html', tweets=tweets)


@app.route('/like/<int:interger>')
def like(interger):
    tlsql.like(interger, 0)
    return redirect('/')


# TODO not login.get_user()>user_number. user_number>user_number. debugging because (interger 0)


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        if login.try_login(request.form['username'], request.form['password']):
            return redirect('/')
        return render_template('login.html', unmatch=True)


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('newuser.html')

    if request.method == 'POST':
        if tlsql.user_insert(request.form['username'], request.form['password'],
                             request.form['Email']) == 'uniqueerror':
            return 'unique error'
        else:
            return home()


@app.route('/sign_out', methods=['GET'])
def sign_out():
    login.try_logout()
    return redirect('/sign_in')
