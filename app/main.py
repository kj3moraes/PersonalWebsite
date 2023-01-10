from tempfile import TemporaryFile
from flask import Flask, render_template, request, redirect
from flask_mail import Mail,Message
import csv

app = Flask(__name__)
print(__name__)
mail = Mail(app)

@app.route('/')
def homepg():
    return render_template('index.html')

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


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thanks.html')
        except:
            return "Did not save to database!"
    else:
        return "Something went wrong!"
