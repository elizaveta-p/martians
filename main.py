from flask import Flask, render_template
from werkzeug.utils import redirect

from data import db_session
from data.jobs import Jobs
from data.users import User
from random import randint
import datetime

from forms.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    # db_sess = db_session.create_session()
    # job = Jobs()
    # job.team_leader = 1
    # job.job = 'deployment of residential modules 1 and 2'
    # job.work_size = 1.5
    # job.collaborators = '2, 3'
    # job.start_date = datetime.datetime.now()
    # job.is_finished = False
    # db_sess.add(job)
    # db_sess.commit()

    app.run()


@app.route('/')
def index():
    db_sess = db_session.create_session()
    res = db_sess.query(Jobs).all()
    return render_template('index.html', jobs=res)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            email=form.email.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            modified_data=datetime.datetime.now()
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    main()