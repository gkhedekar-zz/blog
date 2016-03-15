from flask import Flask, render_template
import MySQLdb
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('welcome.html')


if __name__ == "__main__":
	app.run(debug=True)