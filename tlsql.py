import mysql.connector
import datetime
import dockerdb
import login

conn = mysql.connector.connect(host=dockerdb.db_twitter_local_data[0],
                               user=dockerdb.db_twitter_local_data[1],
                               password=dockerdb.db_twitter_local_data[2],
                               database=dockerdb.db_twitter_local_data[3])
cursor = conn.cursor()


def tweet(string, username):
    cursor.execute(
        'INSERT INTO tweet (username,tweet_time,tweet) values("{}","{}","{}")'.format(username,
                                                                                      datetime.datetime.today(),
                                                                                      string))
    conn.commit()


def view():
    tweet_list = []
    cursor.execute('SELECT * FROM tweet')
    for i in cursor.fetchall():
        i = list(i)
        i.append(like_count(i[0]))
        tweet_list.append(i)
    tweet_list.sort(reverse=True)
    return tweet_list


def like_count(interger):
    x = 0
    cursor.execute(f'SELECT count(tweet_number) FROM likes where tweet_number = {interger}')
    for i in cursor.fetchall():
        x = i
    return int(x[0])


def like(interger, user_number):
    try:
        cursor.execute(
            'INSERT INTO likes (tweet_number,user_number,like_time) values("{}","{}","{}")'.format(interger,
                                                                                                   user_number,
                                                                                                   datetime.datetime.today()))

        conn.commit()
    except mysql.connector.errors.IntegrityError:
        cursor.execute('DELETE FROM likes where (tweet_number= {} and user_number = {})'.format(interger, user_number))


# TODO: build password_hash system


def user_insert(username, password, email):
    after_hash, salt = login.hash_password(password)
    try:
        cursor.execute(
            'INSERT INTO users (username,password,email,salt) values("{}","{}","{}","{}")'.format(username, after_hash, email, salt))
        conn.commit()

    except mysql.connector.errors.IntegrityError:
        return 'uniquerror'


def userlist():
    users = []
    cursor.execute('select * from users')
    for i in cursor.fetchall():
        users.append(i)
    return users


def user_search(num):
    cursor.execute(f'select * from users where num = {num}')
    return cursor.fetchall()[0]


def delete(interger):
    cursor.execute('DELETE FROM tweet where num={}'.format(interger))
