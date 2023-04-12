from flask import Flask,render_template,request
import numpy as np 
import pickle
app = Flask(__name__)
Model = pickle.load(open(r'rdf.pkl', 'rb'))
@app.route('/') # rendering the html template
def home():
    return render_template('home.html')
@app.route('/submit',methods=["POST","GET"])# route to show the predictions in aweb UI
def submit():
    # reading the input given by the user
    input_feature=[int(x) for x in request.form.values() ]
    #input_feature=np.transpose(input_feature)
    input_feature-[np.array(imput_feature)] 
    print(input_feature)
    names=['Gender','Married','Dependents','Education','ApplicantIncome','CoapplicantIncome','LoadAmount','Loan_Amount_Term','Credit_History','Property_Area']
    data=pandas.DataFrame(input_frature,columns=names)
    print(data)
    #data_scaled=scale.fit_transform(data)
    #data=pandas.DataFrame(,columns=names)
    # predictions using the loaded model file
    prediction=model.predict(data)
    print(prediction)
    prediction=int(prediction)
    print(type(prediction))
    if(prediction==0):
        return render_template("output.html",result="Loan will not be Approved")
    else:
        return render_template("output.html",result="Loan Will be approved")
        # showing the predictions results in a UI
if __name__=="__main__":
    # app.run(host='0.0.0.0',port=8000,debug=true)  # running the app
   
     app.run(debug=False)
       



