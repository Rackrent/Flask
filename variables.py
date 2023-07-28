from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def all():
    return "<html><head>This is a page to be visible by all</body></html>"
@app.route('/vint/<int:age>')
def for_int(age):
    print("this is a page for int")
    return "the age is %d"%age
@app.route('/vfloat/<float:temp>')
def for_float(temp):
    return "the temperature is %f" %temp
@app.route('/vstring/<string:name>')
def for_string(name):
    return "Hello %s"%name

if (__name__ == "__main__"):
    app.run(debug=True)
