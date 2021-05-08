from flask import Flask, render_template, request
import indeedscrape

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def home_post():
    if request.method == "POST":
        keyword = request.form['input']
        return "Done!"

if __name__ == '__main__':
    app.run(debug=True)