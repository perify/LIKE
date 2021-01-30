from flask import flask, request, redirect, url_for, render_template, flash, session, Flask
import tlsql

command_bin = []

while True:
    print("which do you doing?,sign in or sign up")
    command = input()

    if command is not None:
        command_bin = command.split(maxsplit=1)

        if command_bin[0] == "newuser":
            if len(command_bin) == 1:
                print("error")
            elif len(command_bin) == 2:
                newuser_bin = command_bin[1].split()
                tlsql.user_insert(newuser_bin[0], newuser_bin[1], newuser_bin[2])

        if command_bin[0] == "userlist":
            if len(command_bin) == 1:
                tlsql.userlist()

        if command_bin[0] == "debug":
            if len(command_bin) == 1:
                break

        if command_bin[0] == "login":
            if len(command_bin) == 1:
                print("error")
            elif len(command_bin) == 2:
                login_bin = command_bin[1].split()
                if tlsql.login(login_bin[0], login_bin[1]) == "ok":
                    break
                else:
                    print("君は道を間違えたようだ。戻りたまえ。")

while True:
    command = input()

    if command is not None:
        command_bin = command.split(maxsplit=1)

        if command_bin[0] == "tweet":
            if len(command_bin) == 1:
                print("error")
            else:
                tlsql.tweet(command_bin[1])

        if command_bin[0] == "view":
            tlsql.view()

        if command_bin[0] == "like":
            if len(command_bin) == 1:
                print("error")
            else:
                tlsql.like(int(command_bin[1]))

        if command_bin[0] == "exit":
            exit()

        if command_bin[0] == "del":
            if len(command_bin) == 1:
                print("error")
            elif len(command_bin) == 2:
                tlsql.Del(int(command_bin[1]))
