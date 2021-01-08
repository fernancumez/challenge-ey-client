from flask import Flask, render_template, request, url_for, redirect
from flask_restful import Resource, Api
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)  ## To allow direct AJAX calls

@app.route("/", methods=["GET"])
def home():
   url = "http://localhost:8000/api/books"
   res = requests.get(url)

   books = res.json()

   if res.status_code == 200:
      return render_template("index.html", books = books)

   return "I don´t understand you"


@app.route("/create-book", methods=["POST"])
def create():
   url = "http://localhost:8000/api/books"
   payload = {"isbn": request.form["isbn"], "title": request.form["title"]}
   headers = {"Content-Type": "application/json"}

   res = requests.post(url, data=json.dumps(payload), headers=headers)

   return redirect(url_for('home'))

@app.route('/delete/<id>')
def delete(id):
   url = "http://localhost:8000/api/books"

   res = requests.delete(url + "/" + id)

   return redirect(url_for('home'))

if __name__ == "__main__":
   app.run(debug = True)