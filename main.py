from flask import Flask
from data import db_session
from data.jobs import Jobs
from data.users import User
from random import randint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    db_sess.add(user)
    db_sess.commit()

    for i in range(1, 4):
        user = User()
        user.surname = f'Surname{i}'
        user.name = f'Name{i}'
        user.age = randint(18, 100)
        user.position = f'example_position{i}'
        user.speciality = f'speciality{i}'
        user.address = f'example_module{i}'
        user.email = f'example_email{i}@mars.org'
        db_sess.add(user)
        db_sess.commit()

    # app.run()


if __name__ == '__main__':
    main()