from flask import Flask,render_template,request
AI=Flask(__name__)

@AI.route('/wishes')
def wish():
    return render_template('wish.html')


@AI.route('/second')
def second():
    return render_template('second.html')

@AI.route('/suresh',methods=['GET','POST'])
def sureshhtml():
    if request.method=='POST':
        form_data=request.form
        #return str(form_data)
        return (form_data['name'])


    return render_template('sureshhtml.html')

if __name__=='__main__':
    AI.run(debug=True)