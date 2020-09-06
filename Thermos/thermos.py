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


#jinjia2,  在html中可以传参， {{var}}   -------> render_template(index.html, var='hello')
#s也可使用function， {{var.fun()}}
@app.route('/')
@app.route('/index')
def index():
    #return 'hello world'
    return render_template('index.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug = False)