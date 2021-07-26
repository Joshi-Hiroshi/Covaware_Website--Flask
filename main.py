from flask import Flask, render_template, request, redirect , flash , url_for


app=Flask(__name__)
app.config['SECRET_KEY'] = 'babaBlackSheep$123'

#Main Home Route
@app.route("/")
def home():
    return render_template("index.html")

app.run(debug=True)