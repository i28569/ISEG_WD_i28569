from flask import Flask, request, make_response, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)

@app.route('/')
def index():
    response = make_response('Hello World!')
    response.headers['Content-Type'] = 'text/plain'
    return response

@app.route('/users/<user>')
def show_user(user):
    return f'Hello {user} and welcome to my first web application!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    user = 'test'
    password = 'test'
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
    if user == 'test' and password == 'test':
        return 'Login successful'
    else:
        return 'Invalid username or password'

@app.route('/t')
def index_template():
    name = 'Ricardo'
    return render_template('index.html',name=name)


class NameForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route("/form", methods=["GET", "POST"])
def form():
    form = NameForm()
    if request.method == "POST" and form.validate_on_submit():
        name = form.name.data
        return "Hello " + name
    return render_template("form.html",form=form)

app.config["SECRET_KEY"] = "test_key"


if __name__ == '__main__':
    app.run()