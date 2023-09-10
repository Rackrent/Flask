from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
@app.route("/hello")
@app.route("/hello/<user>")
def hello_world(user=None):
    user = user or 'Krishna'
    return render_template('hello_world.html',user = user)
if __name__ == "__main__":
    app.run(port=5000, debug=True)