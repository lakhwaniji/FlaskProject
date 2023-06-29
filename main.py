from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail,Message
import backend
app = Flask(__name__)
app.config["SECRET_KEY"]="myapplication23"
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = "lovelakhwani181@gmail.com"
app.config["MAIL_PASSWORD"] = "opwknicnotrptrdn"

mail=Mail(app)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        occupation = request.form["occupation"]
        backend.insert_record(first_name,last_name,email,occupation,date)

        message_body=f"Thank you for your submission, {first_name}."\
                     f"Here are your data: {first_name} \n {last_name} \n {date} \n"\
                     f"Thank you"
        message=Message(subject="New Form Submission",
                        sender=app.config["MAIL_USERNAME"],
                        recipients=[email],
                        body=message_body)
        mail.send(message)
        flash(f"{first_name} your form has been submitted sucessfully")
    return render_template("index.html")

if __name__=="__main__":
    '''with app.app_context():
        db.create_all()'''
    app.run(debug=True, port=5001)

