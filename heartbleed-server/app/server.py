import flask
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

from flask_login import LoginManager, UserMixin
from flask_login import login_user , logout_user , current_user , login_required
 
class User(UserMixin):

    def __init__(self,username,password):
        self.username=username
        self.password=password

        #if self.id is None, the user has not been authenticated
        self.id=None

        #for now use a fixed username,password pair as only valid one
        if username=='foo' and password=='bar':
            self.id = unicode(username)

    def is_authenticated(self):
        if self.id is not None:
            return True
 
    def get_id(self):
        return self.id

class LoginForm(FlaskForm):
    name = StringField('name',validators=[DataRequired()])
    password = StringField('password',validators=[DataRequired()])

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    username = str(id)
    if username == 'foo':
        password = 'bar'
        return User(username,password)
    else:
        return None

@app.route('/index')
@app.route('/')
@login_required
def index():
    return 'Hello {}!'.format(current_user.username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        user = User(form.name.data,form.password.data)
        login_user(user)
        return flask.redirect(flask.url_for('index'))
    return flask.render_template('login.html', form=form)

if __name__ == "__main__":
    app.run()
