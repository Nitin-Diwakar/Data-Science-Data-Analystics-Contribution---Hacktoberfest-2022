from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

@app.route("/contact")
def contact():
    output = request.form.to_dict()
    name = output["name"]
    return render_template('')
if __name__ == "__main__":
    app.run(debug= True, port = 5000)

