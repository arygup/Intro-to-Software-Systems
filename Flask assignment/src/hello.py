from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

#@app.route('/', methods=['GET'])
#def hello():
#    return 'hello :)'

@app.route('/admin/')
def hello_admin():
    return 'hello admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return render_template('hello.html', name=guest)
    return 'hello guest %s' % guest

@app.route('/hello/<name>', methods=['GET'])
def hello_name(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    return redirect(url_for('hello_guest', guest=name))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print("we got POST")
        user = request.form['name']
        return redirect(url_for('hello_name', name=user))
    user = request.args.get('name')
    return redirect(url_for('hello_name', name=user))

@app.route('/hello/<int:num>', methods=['GET'])
def numx10(num):
    return render_template('num.html', num=num)

#@app.route('/hello/<int:num>', methods=['GET'])
#def numx10(num):
#    return '%s' % (num*10)


@app.route('/')
def index():
    return """<html> <body> <form action = "http://localhost:5000/login" method = "post" > <p> Enter name </p> <p><input type = "text" name = "name" /></p> <p><input type = "submit" value="submit" /></p> </form> </body> </html>"""


@app.route('/static')
def stat():
    return render_template('static.html')

if __name__ == '__main__':
    app.run(debug=True)
