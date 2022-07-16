from flask import Flask, render_template

app = Flask(__name__)

# create a route decorator
@app.route('/')
def index():
    return "<h2>Let's try this again!</h2>"


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