from flask import request, render_template, redirect, url_for, Flask
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
import User
import tlsql

app = Flask(__name__)

app.secret_key = b'jugemjugemgokonosurikirekaijarisuigyono'
login_manager = LoginManager()
login_manager.init_app(app)

login_status = []


@app.route('/')
@login_required
def home_action():
    tweets = []
    for i in tlsql.view():
        tweets.append(i)
    return render_template('home.html', tweets=tweets)


@app.route('/', methods=['POST'])
def tweet_action():
    tlsql.tweet(request.form['message'])
    return home_action()


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_action():
    if tlsql.login(request.form['username'], request.form['password']) == "ok":
        login_user(request.form['username'],)
        return redirect(url_for('home_action'))
    return render_template('login.html', unmatch=True)


@app.route('/signup')
def signup_form():
    return render_template('newuser.html')


@app.route('/signup', methods=['POST'])
def signup_action():
    tlsql.user_insert(request.form['username'], request.form['password'], request.form['Email'])
    return home_action()


@login_manager.user_loader
def load_user(user_id):
    return User()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
