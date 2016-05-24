from flask import Flask
app = Flask(__name__)


class LoginForm(Form):
        UserName = StringField('登陆',validators=[required()])
        Passwd = PasswordField('pw')
        SubmitBut = Submit('submit')


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login')
def login():

    return render_template('')


if __name__ == '__main__':
    app.run()
