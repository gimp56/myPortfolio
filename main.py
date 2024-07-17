from flask import Flask, render_template, url_for,redirect,request
import csv

app = Flask("__name__")

@app.route("/")
def homePage():
    return render_template("index.html")

@app.route("/<page_name>")
def html_page(page_name):
    return render_template(page_name)

def csv_writer(data):
    with open("database.csv","a",newline="") as database:
        writer = csv.writer(database,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        writer.writerow([email,subject,message])

@app.route("/form_submit.html",methods=["GET","POST"])
def form_submit():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        csv_writer(data)
        return redirect("thankyou.html")
    else:
        return "something went wrong///........."
    

