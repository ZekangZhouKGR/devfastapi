from flask import Flask, request

app = Flask(__name__)

@app.route('/hello/<username>')
def hello(username):
    return f'Hello, {username}!'

if __name__ == '__main__':
    app.run(debug=True)