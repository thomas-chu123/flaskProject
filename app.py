from flask import Flask, redirect, render_template, session, request, url_for

app = Flask(__name__)

@app.get('/')
def hello_world():  # put application's code here
    # return 'Hello World!'
    test: dict = {"name": "gogogo"}
    print(url_for("static", filename="style.css"))
    print(url_for("hello_world"))
    return render_template("index.html", test=test)

@app.get('/contact')
def contact():
    return render_template("contact.html")

@app.post('/contact/complete')
def contact_complete():
    if request.method == 'POST':
        return redirect(url_for('contact_complete'))
    return render_template('contact_complete.html')

if __name__ == '__main__':
    app.run()
