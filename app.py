from flask import Flask, render_template, abort, request
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

animals = [
    {'id':1, 'Name': 'Nelly', 'Age': '5 weeks', 'Bio': 'I am a tiny kitten rescued by the good people.'},
    {'id':2, 'Name': 'Yuki', 'Age': '3 weeks', 'Bio': 'I am a handsome gentle-cat. I like to dressup in bow ties.'},
    {'id':3, 'Name': 'Basker', 'Age': '1 year', 'Bio': 'I love barking. But, I love my friends more.'}
        ]

users = {"fakiri@gmail.com": "123456", "ismail@email.com": "azerty"}

@app.route("/")
def home():
    return render_template("home.html", animals=animals)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    # form.is_submitted()    form.validate()    form.validate_on_submit()
    if form.validate_on_submit():
        for u_email, u_password in users.items():
            if u_email == form.email.data and u_password == form.password.data:
                return render_template("login.html", form=form, message="Successfully Logged In")
        return render_template("login.html", form=form, message="Incorrect Email or Password")
    elif form.errors:
        print(form.errors.items())  # return dict()
        print(form.email.errors)    # return list()
        print(form.password.errors) # return list()

    return render_template("login.html", form=form)

# Static routing
@app.route("/about")
def about():
    return render_template("about.html")

# Dynamic routing
@app.route("/details/<int:animal_id>")     # String (default), int, float, path (Strings with slashes), uuid.
def animal_details(animal_id):
    animal = next((animal for animal in animals if animal["id"] == animal_id), None)
    if animal is None:
        abort(404, description="No animal was Found with the given ID")
    return render_template("details.html", animal=animal)

if __name__ == "__main__":
    app.run()
