from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home_page():
    name = "Me Myname"
    return render_template('base.html', name=name)


# @app.route("/")
# def hello_world():
#     return render_template('hello.html')

# @app.route("/hi/<name>")
# def test2(name):
#     information = {'name': 'erik',
#                     'job': 'student',
#                     'heyyo': 3,
#                     }
#     return render_template('hello.html', myVar=name, varSecond=information)

# @app.route("/test/<name>")
# def test(name):
#     return render_template('tests.html', result=name)
