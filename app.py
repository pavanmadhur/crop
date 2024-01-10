from flask import Flask, render_template,jsonify,request
import pickle

app= Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prediction',methods = ['GET','POST'])
def prediction():
    if request.method=='POST':
        nitro = request.form.get('nitrogen')
        phos = request.form.get('phosphorus')
        kp = request.form.get('potassium')
        tem = request.form.get('temperature')
        hum = request.form.get('humidity')
        ph = request.form.get('ph')
        rain = request.form.get('rainfall')
        print(nitro,phos,kp,tem,hum,ph,rain)
        with open('model.pkl','rb') as model_file:
            mlmodel = pickle.load(model_file)
        res = mlmodel.predict([[float(nitro),float(phos),float(kp),float(tem),float(hum),float(ph),float(rain)]])
        print(res)
        conn = sqilte1.connect('cropdata.db')
        cur = conn.cursor()
        cur.excute('''Insert intro crop values()''')

        return render_template('result.html',res=res[0])
    else:
        return render_template('prediction.html')


    
if __name__=='__main__':
    app.run(host="0.0.0.0",port=5342)




