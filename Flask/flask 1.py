from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('hello.html')
@app.route('/bootstrap')
def hello():
    return render_template('bootstrap.html')
@app.route('/album')
def alu():
    return render_template('album.html')
app.run(debug=True)
# debug=True can be used to save the changes