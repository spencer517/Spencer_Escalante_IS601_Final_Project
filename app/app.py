from flask import Flask, Markup

# Create Flask's `app` object
app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return Markup("<h1>Hello World!</h1>")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
