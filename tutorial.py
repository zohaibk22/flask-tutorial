from flask import Flask,  redirect, url_for

app = Flask(__name__)


@app.route('/home')
def home():
    return "<h1>Hello this is the main page</h1>"

@app.route('/test/<name>')
def user(name):
    return f'Hello {name}!'


@app.route("/admin")
def admin():
    return redirect(url_for('user', name="Admin!"))


if __name__ == '__main__':
    app.run()