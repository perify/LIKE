from flask import session
import tlsql


def is_login():
    return 'login' in session


def try_login(user, password):
    userlist = {}
    for i in tlsql.userlist():
        userlist[i[0]] = i[1]
    if user not in userlist: return False
    if userlist[user] != password: return False
    session['login'] = user
    return True


def try_logout():
    session.pop('login', None)
    return True


def get_user():
    if is_login(): return session['login']
    return 'not login'
