from flask import Flask, render_template, url_for
from dash import Dash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)


app.config['SECRET_KEY'] = '50ca4236457f508d05f3a4e229723b55'

# @app.route('/')
# def home():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)


posts = [
    {
        'author' : 'Vignesh',
        'title': 'Blog Post 1',
        'content': 'First post context',
        'date_posted': 'April 20, 2018'
    },
    {
        'author' : 'Brahadeesh',
        'title': 'Blog Post 2',
        'content': 'Second post context',
        'date_posted': 'April 21, 2018'
    }
]

@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', posts = posts, title = 'about')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register', form = form)

@app.route('/login')
def register():
    form = RegistrationForm()
    return render_template('login.html', title = 'Login', form = form)

if __name__ == '__main__':
    app.run(debug=True)


 