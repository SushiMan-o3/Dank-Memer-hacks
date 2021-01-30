from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html') 

@app.route("/information", methods=['GET', 'POST'])
def shop():
    return render_template('shop.html') 

@app.route("/help", methods=['GET', 'POST'])
def help():
    return render_template('help.html') 

@app.route("/test", methods=['GET', 'POST'])
def test():
    return render_template('/others/thank-you.html') 

if __name__ == "__main__":
    app.run(debug = True)
