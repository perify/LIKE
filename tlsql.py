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
        'INSERT INTO tweet (id,teatime,tweet) values("tatsu","{}","{}")'.format(datetime.datetime.today(), string))
    conn.commit()


def view():
    tweet_list = []
    cursor.execute('SELECT * FROM tweet')
    for i in cursor.fetchall():
        tweet_list.append(i)
    tweet_list.sort(reverse=True)
    return tweet_list


def like(interger):
    cursor.execute('UPDATE tweet set likec=likec+1 where num = {}'.format(interger))


def delete(interger):
    cursor.execute('DELETE FROM tweet where num={}'.format(interger))

# def password_hash(string):
#    string.encode('utf-8')
#    string = bcrypt.hashpw(string,salt=bcrypt.gensalt(rounds=12,prefix=b'2a'))
#    return string

# TODO: build password_hash system


def user_insert(id, password, email):
    cursor.execute('INSERT INTO users values("{}","{}","{}")'.format(id, password, email))
    conn.commit()


def userlist():
    cursor.execute('select * from users')
    for i in cursor.fetchall():
        print(i)
    conn.commit()


def exitsql():
    cursor.close()
    conn.close()


def login(id, password):
    login_bin = []
    cursor.execute('select * from users where ID=\'{}\''.format(id))
    for i in cursor.fetchall():
        login_bin.append(i)
    if login_bin[0][1] == password:
        # login complete!!
        login_if = "ok"
    else:
        login_if = "no"

    return login_if
