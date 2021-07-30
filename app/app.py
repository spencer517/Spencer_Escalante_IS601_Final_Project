from flask import Flask, Markup, render_template

# Create Flask's `app` object
app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return render_template("index.html", title='index')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
