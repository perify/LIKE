from flask import request, render_template, redirect, url_for, Flask
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
import tlsql

app = Flask(__name__)

app.secret_key = b'jugemjugemgokonosurikirekaijarisuigyono'
login_manager = LoginManager()
login_manager.init_app(app)

login_status = []


class User(UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in tlsql.users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in tlsql.users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == tlsql.users[email]['password']

    return user


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
    # if tlsql.login(request.form['username'], request.form['password']) == "ok":
    tlsql.user_load()
    email = request.form['email']
    if request.form['password'] == tlsql.users[email]['password']:
        user = User()
        user.id = email
        login_user(user)
        return redirect(url_for('home_action'))

    return render_template('login.html', unmatch=True)


@app.route('/signup')
def signup_form():
    return render_template('newuser.html')


@app.route('/signup', methods=['POST'])
def signup_action():
    tlsql.user_insert(request.form['username'], request.form['password'], request.form['Email'])
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
