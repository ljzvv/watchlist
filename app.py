from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>hello Totoro!</h1><img src="http://helloflask.com/totoro.gif"/><p>欢迎你来到我的网页程序Watchlist!</P>'
