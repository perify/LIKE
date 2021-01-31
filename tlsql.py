import mysql.connector
import datetime
import sys
import localdb

conn = mysql.connector.connect(host=localdb.db_twitter_local_data[0],
                               user=localdb.db_twitter_local_data[1],
                               password=localdb.db_twitter_local_data[2],
                               database=localdb.db_twitter_local_data[3])
cursor = conn.cursor()


def tweet(string):
    cursor.execute(
        'INSERT INTO tweet (id,teatime,tweet) values("tatsu","{}","{}")'.format(datetime.datetime.today(), string))
    conn.commit()


def view():
    bin = []
    cursor.execute('SELECT * FROM tweet')
    for i in cursor.fetchall():
        bin.append(i)
    bin.sort(reverse=True)
    return bin

def like(interger):
    cursor.execute('UPDATE tweet set likec=likec+1 where num = {}'.format(interger))


def Del(interger):
    cursor.execute('DELETE FROM tweet where num={}'.format(interger))


def exit():
    exitsql()
    sys.exit()


# def password_hash(string):
#    string.encode('utf-8')
#    string = bcrypt.hashpw(string,salt=bcrypt.gensalt(rounds=12,prefix=b'2a'))
#    return string

# TODO: build password_hash system


def user_insert(ID, PASSWORD, EMIL):
    cursor.execute('INSERT INTO users values("{}","{}","{}")'.format(ID, PASSWORD, EMIL))
    conn.commit()


def userlist():
    cursor.execute('select * from users')
    for i in cursor.fetchall():
        print(i)
    conn.commit()


def exitsql():
    cursor.close()
    conn.close()


def login(ID, PASSWORD):
    login_bin = []
    cursor.execute('select * from users where ID=\'{}\''.format(ID))
    for i in cursor.fetchall():
        login_bin.append(i)
    if login_bin[0][1] == PASSWORD:
        # login complete!!
        login_if = "ok"
    else:
        login_if = "no"

    return login_if

