# Here we write the code for the dep;oyment and createion of the server.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home ():
    return render_template("index.html")

@app.route('/predict', methods= ['POST'])
def perdict():
    email_text = request.form.get('email-content')
    
    # Here do all the work of predection
    # Prerocessing and predection like calling a fuction can be done
    # Usee pickel etc for loading the content ...
    predection = predict(email_text)
    predection = 1 if predection == 1 else -1
    
    return render_template('index.html', predection = predection, text= email_text)

def predict(text):
    from random import choice
    # Currently giving a random ans
    # 0->ham, 1-> spam
    return choice([0, 1])

if __name__ == '__main__':
    app.run(debug=True)
