from flask import Flask, redirect, url_for, request
app = Flask(__name__)
  
@app.route('/<name>')
def name(name):
    x = int(name)
    if(x >= 50):
        return "yes input is greater than 50"
    return 'input is not greater than 50' 
  
@app.route('/calc/sum',methods = ['POST', 'GET'])  
def calc_sum():     
    if request.method == 'POST':
      n1 = request.form['num1']
      n2 = request.form['num2']
      if (n1.isdigit() and n2.isdigit):
        return '%d' %(int(n1)+int(n2))

@app.route('/calc/multiply',methods = ['POST', 'GET'])  
def calc_multiply():     
    if request.method == 'POST':
      n1 = request.form['num1']
      n2 = request.form['num2']
      if (n1.isdigit() and n2.isdigit):
        return '%d' %(int(n1)*int(n2))


if __name__ == '__main__':
   app.run(debug = True)