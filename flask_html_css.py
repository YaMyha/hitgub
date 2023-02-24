from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = 'Basik'
    phone = '111222333444'
    return render_template("hello.html", name=name, phone=phone)

app.run()