from flask import Flask, redirect, render_template, session, request, url_for, flash, make_response
from email_validator import validate_email, EmailNotValidError
import logging
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail, Message

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
app.logger.setLevel(logging.DEBUG)
app.logger.critical('This is a critical message')
app.logger.error('This is an error message')
app.logger.warning('This is a warning message')
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USER'] = 'tomchu12345@gmail.com'
app.config['MAIL_PASSWORD'] = 'yawrxglzowycccup'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = 'hzdkv@example.com'
toolbar = DebugToolbarExtension(app)
mail = Mail(app)

@app.route('/')
def hello_world():  # put application's code here
    # return 'Hello World!'
    test: dict = {"name": "this is a test"}
    print(url_for("static", filename="style.css"))
    print(url_for("hello_world"))
    response = make_response(render_template('index.html', test=test))
    response.set_cookie('username', 'tomchu12345')
    session['username'] = 'tomchu12345'
    return response


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/contact/complete', methods=['GET', 'POST'])
def contact_complete():
    if request.method == 'POST':
        is_valid = True
        username = request.form['username']
        email = request.form['email']
        description = request.form['description']
        if not username:
            flash('please enter username')
            is_valid = False
        if not email:
            flash('please enter email')
            is_valid = False
        try:
            validate_email(email)
        except EmailNotValidError:
            flash('please enter valid email')
            is_valid = False
        if not description:
            flash('please enter description')
            is_valid = False

        if not is_valid:
            return redirect(url_for('contact'))
        flash('success')
        return redirect(url_for('contact_complete'))

    send_email("this is a test", "tomchu12345@gmail.com", "chu_liang_han@hotmail", "happy subscription", "this is a test")
    return render_template('contact_complete.html')


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=[recipients])
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

if __name__ == '__main__':
    app.run()
