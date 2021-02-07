from flask import request, render_template, Flask

import tlsql

app = Flask(__name__)


@app.route('/')
def home_action():
    tweets = []
    for i in tlsql.view():
        tweets.append(i)
    return render_template('home.html', tweets=tweets)


@app.route('/', methods=['POST'])
def tweet_action():
    tweets = []
    tlsql.tweet(request.form['message'])
    for i in tlsql.view():
        tweets.append(i)
    return render_template('home.html', tweets=tweets)


@app.route('/login')
def login_form():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_action():
    if tlsql.login(request.form['username'], request.form['password']) == "ok":
        return home_action()
    return render_template('login.html', unmatch=True)


@app.route('/signup')
def signup_form():
    return render_template('newuser.html')


@app.route('/signup', methods=['POST'])
def signup_action():
    tlsql.user_insert(request.form['username'], request.form['password'], request.form['Email'])
    return home_action()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
