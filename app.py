from flask import Flask, render_template as render
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
@app.route('/home/')
def home():
    # return f"<h1>Hello There</h1> {escape(username)}"
    return render('home.html')


if __name__ == "__main__":
    app.run()


