#Python
#SQL
#HTML + CSS + JS + jQuery + botstrap
#VUE 前后端分离准备ls

from flask import Flask

app = Flask(__name__)

@app.route('/index')
def index():
    return 'Hello World'

if __name__ == "__main__":
    app.run()