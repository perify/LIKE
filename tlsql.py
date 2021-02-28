import mysql.connector
import datetime
import dockerdb


conn = mysql.connector.connect(host=dockerdb.db_twitter_local_data[0],
                               user=dockerdb.db_twitter_local_data[1],
                               password=dockerdb.db_twitter_local_data[2],
                               database=dockerdb.db_twitter_local_data[3])
cursor = conn.cursor()


def tweet(string):
    cursor.execute(
        'INSERT INTO tweet (username,teatime,tweet) values("{}","{}","{}")'.format("tatsu", datetime.datetime.today(),
                                                                                   string))
    conn.commit()


def view():
    tweet_list = []
    cursor.execute('SELECT * FROM tweet')
    for i in cursor.fetchall():
        tweet_list.append(i)
    tweet_list.sort(reverse=True)
    return tweet_list


def like(interger):
    cursor.execute('UPDATE tweet set like_count=like_count+1 where num = {}'.format(interger))


# def password_hash(string):
#    string.encode('utf-8')
#    string = bcrypt.hashpw(string,salt=bcrypt.gensalt(rounds=12,prefix=b'2a'))
#    return string

# TODO: build password_hash system


def user_insert(username, password, email):
    cursor.execute('INSERT INTO users values("{}","{}","{}")'.format(username, password, email))
    conn.commit()


def userlist():
    users = []
    cursor.execute('select * from users')
    for i in cursor.fetchall():
        users.append(i)
    conn.commit()
    return users


def delete(interger):
    cursor.execute('DELETE FROM tweet where num={}'.format(interger))


def login(username, password):
    login_bin = []
    cursor.execute('select * from users where username=\'{}\''.format(username))
    for i in cursor.fetchall():
        login_bin.append(i)
    if login_bin[0][1] == password:
        # login complete!!
        login_if = "ok"
    else:
        login_if = "no"

    return login_if
