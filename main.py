from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# noinspection SpellCheckingInspection
app.config['SECRET_KEY'] = 'dd26f2b76681eb602fb0d8c3a6ddcf12'

posts = [
    {
        'author': 'Corey Shaffer',
        'title': 'Blog post 1',
        'content': 'Blog 1  content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Bill Gates',
        'title': 'My way',
        'content': 'My way  content',
        'date_posted': 'April 20, 2019'
    },
    {
        'author': 'Tim Cook',
        'title': 'My apple',
        'content': 'My apple  content',
        'date_posted': 'April 20, 2020'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    # noinspection SpellCheckingInspection
    return render_template('about.html', title="Aaaabout")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
