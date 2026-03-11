from flask import Flask, render_template, redirect, url_for
from forms import RegistrationForm
from models import db, User

app = Flask(__name__)

app.config["SECRET_KEY"] = "secret123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

db.init_app(app)

# Create database
with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():

        new_user = User(
            name=form.name.data,
            email=form.email.data,
            password=form.password.data
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("success", name=form.name.data))

    return render_template("register.html", form=form)


@app.route("/success/<name>")
def success(name):
    return render_template("success.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)