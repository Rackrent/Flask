from flask import Flask
app= Flask(__name__)
def about():
    return "this is the about stuff"
app.add_url_rule("/about","about",about)
if __name__ =="__main__":
    app.run(debug = True)