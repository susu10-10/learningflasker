from flask import Flask, redirect, render_template, flash, url_for
from forms import NamerForm, Register

app = Flask(__name__)
# add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# secret key
app.config['SECRET_KEY'] = 'vibes'
# initialize the database
# db = SQLAlchemy(app)

# create a route decorator
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


# create Custom Error pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server(e):
    return render_template('500.html'), 500


# create name page
@app.route('/name', methods=['GET','POST'])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash('Form Submitted Successfully')
        return redirect(url_for('continue_name', usr=name))
    else:
        return render_template('name.html', form=form, name=name)

@app.route("/<usr>")
def continue_name(usr):
    usr = usr
    usr2 = f"<strong>{usr}</strong>"
    form = Register()
    return render_template('name2.html', usr=usr, form=form, usr2=usr2)