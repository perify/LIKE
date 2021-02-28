from flask import request, render_template, Flask

import tlsql

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    tweets = []

    if request.method == 'GET':
        for i in tlsql.view():
            tweets.append(i)
        return render_template('home.html', tweets=tweets)

    elif request.method == 'POST':
        tlsql.tweet(request.form['message'])
        for i in tlsql.view():
            tweets.append(i)
        return render_template('home.html', tweets=tweets)


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':
        if tlsql.login(request.form['username'], request.form['password']) == "ok":
            return home()
        return render_template('login.html', unmatch=True)


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('newuser.html')

    elif request.method == 'POST':
        tlsql.user_insert(request.form['username'], request.form['password'], request.form['Email'])
        return home()
