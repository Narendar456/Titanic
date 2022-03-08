from flask import Flask, request,render_template
import joblib
import numpy as np
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



@app.route('/', methods=['POST', 'GET'])
def result():
    ticket_class = float(request.form['class'])
    gender = float(request.form['gender'])
    age = float(request.form['age'])
    siblings = float(request.form['siblings'])
    parents = float(request.form['parents'])
    fair = float(request.form['fair'])
    onboard = float(request.form['onboard'])
    X = np.array([ticket_class,gender,age,siblings,parents,fair,onboard]).reshape(1,-1)
    print(X)


    model=model.pkl
    Y = model.predict(X)
    pred = "survived" if Y[0]==1 else "died"

    return render_template('index.html', prediction_text='{}'.format(pred))


if __name__ =="__main__":
    app.run(debug=True, port=5623)
