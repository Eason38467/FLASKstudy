from flask import Flask, render_template,url_for

app = Flask(__name__)

class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def initials(self):
        return "{}. {}".format(self.firstname[0],self.lastname[0])
    def __stre__(self):
        return



@app.route('/')
@app.route('/index')
def index():
    #return 'hello world'
    return render_template('index.html', title = "this is title", text = "this is text", user= User('siyuan','xiao'))


if __name__ == '__main__':
    app.run(debug = True)