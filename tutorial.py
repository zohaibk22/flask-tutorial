from flask import Flask,  redirect, url_for, render_template

app = Flask(__name__)


@app.route('/home/<name>')
def home(name):
    return render_template('index.html', content=name, r="Khan")

@app.route('/test/<name>')
def user(name):
    return f'Hello {name}!'


@app.route("/admin")
def admin():
    return redirect(url_for('user', name="Admin!"))


if __name__ == '__main__':
    app.run(host='localhost', port=3000)