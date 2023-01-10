from tempfile import TemporaryFile
from flask import Flask, render_template, request, redirect
from flask_mail import Mail,Message
import csv

app = Flask(__name__)
print(__name__)
mail = Mail(app)

# Rendering the home page
@app.route('/')
def homepg():
    return render_template('index.html')

# Rendering every other page (default is index.html)
@app.route('/<string:pagename>')
def extrapg(pagename="index.html"):
    return render_template(pagename)


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as db2:
        email_addr = data["email"]
        subject = data["subject"]
        message = data["info"]
        csv_write = csv.writer(db2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email_addr , subject, message])

data = []

# Render the contact page (again) - this overrides the other rendering method
@app.route('/contact.html', methods=['POST', 'GET'])
def submit_form():
    if request.method == "GET":
        return render_template('contact.html', data=data)

    data.append(request.form.to_dict())
    return redirect('/thankyou.html')
