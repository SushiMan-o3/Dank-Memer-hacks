from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html') 

@app.route("/information", methods=['GET', 'POST'])
def about():
    return render_template('information.html') 

@app.route("/help", methods=['GET', 'POST'])
def help():
    return render_template('help.html') 

if __name__ == "__main__":
    app.run(debug = True)
