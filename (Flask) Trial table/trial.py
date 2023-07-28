from flask import Flask, render_template, request

# Create the Flask instance and pass the Flask
# constructor the path of the correct module
app = Flask(__name__)
@app.route('/', methods=['GET'])
def trial():
    if request.method == 'GET':
        if request.args.get('num')==None:
            # return render_template('wrong.html')
            return render_template('first.html')
        elif request.args.get('num')=='':
            return "<html> <body> <h1> Cant compute an empty number </body></html>"
        else:
            sum=[]
            n = request.args.get('num')
            for i in range(1,11):

                print("iiiiiiii",i)
                tv=n*i
                print(n,"*",i,'=',tv)


            return render_template('one.html',num=n,tnum=tv)
if (__name__ == "__main__"):
    app.run(debug=True)
