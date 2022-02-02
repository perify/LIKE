from flask import session
import tlsql
import hashlib
import secrets


def hash_password(password, salt=secrets.token_hex(8)):
    after_hash = hashlib.sha256(str.encode(password+salt)).hexdigest()
    return after_hash, salt


def is_login():
    return 'login' in session


def try_login(user, password):
    userlist = {}
    for i in tlsql.userlist():
        userlist[i[1]] = [i[2], i[4], i[0]]
    if user not in userlist:
        return False
    if userlist[user][0] != hash_password(password, userlist[user][1])[0]:
        return False
    session['login'] = userlist[user][2]
    return True


def try_logout():
    session.pop('login', None)
    return True


def get_user():
    if is_login():
        r = tlsql.user_search(session['login'])
        if r:
            return tlsql.user_search(session['login'])[0]
        else:
            'not login'
    return 'not login'
