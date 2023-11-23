from flask import Flask,request,render_template
from datetime import date

app = Flask(__name__)

#### Saving Date today in 2 different formats
dateThisDay = date.today().strftime("%m_%d_%y")
dateThisDay2 = date.today().strftime("%d-%B-%Y")

def restore_thelines(text):
    lines = text.split('\n')
    lines = [line for line in lines if line.strip()]
    return len(lines)

@app.route('/')
def home():
 #   return '<h1>Hello from Flask & Docker</h2>'
    return render_template('home.html',dateThisDay2=dateThisDay2) 

#### This function will run when we add a new user
@app.route('/count',methods=['GET','POST'])
def count():
    text = request.form['text']
    
    words = len(text.split())
    
    paras = restore_thelines(text)

    text = text.replace('\r','')
    text = text.replace('\n','')

    chars = len(text)
    return render_template('home.html',words=words,paras=paras,chars=chars,dateThisDay2=dateThisDay2) 


if __name__ == "__main__":
    app.run(debug=True)