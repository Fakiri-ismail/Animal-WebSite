from flask import Flask, render_template, abort, request
from flask import session, redirect, url_for
from forms import LoginForm, SingUpForm, EditAnimalForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///paws.db'
db = SQLAlchemy(app)

"""Model for Animals."""
class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    age = db.Column(db.String)
    bio = db.Column(db.String)
    posted_by = db.Column(db.String, db.ForeignKey('user.id'))

"""Model for Users."""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    animals = db.relationship('Animal', backref='user')     # backref us to point to a row in User by using animal.user

db.create_all()

# mrfurrkins = Animal(name="Mr. Furrkins", age="5 years", bio="Probably napping.")
# db.session.add(mrfurrkins)
# db.session.commit()


@app.route("/")
def home():
    animals = Animal.query.all()
    return render_template("home.html", animals=animals)


@app.route("/login", methods=["GET", "POST"])
def login():
    animals = Animal.query.all()
    form = LoginForm()
    # form.is_submitted()    form.validate()    form.validate_on_submit()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data, password=form.password.data).first()
        if user is None:
            return render_template("login.html", form=form, message="Incorrect Email or Password")
        else:
            session['user'] = user.id
            return render_template("home.html", animals=animals)
    elif form.errors:
        print(form.errors.items())  # return dict()
        print(form.email.errors)  # return list()
        print(form.password.errors)  # return list()

    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('login'))  # more parameter :  _scheme='https', _external=True


@app.route("/singUp", methods=["GET", "POST"])
def singUp():
    form = SingUpForm()
    if form.validate_on_submit():
        new_user = User(fullName=form.fullName.data, email=form.email.data, password=form.password1.data)
        db.session.add(new_user)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            return render_template("signup.html", form=form, message="This Email already exists! Please Log in instead.")
        finally:
            db.session.close()

        loginForm = LoginForm()
        return render_template("login.html", form=loginForm)
    elif form.errors:
        print(form.errors.items())
        print(form.email.errors[0])
        print(form.password2.errors[0])

    return render_template("singup.html", form=form)


# Static routing
@app.route("/about")
def about():
    return render_template("about.html")


# Dynamic routing
@app.route("/details/<int:animal_id>", methods=["POST", "GET"])  # String (default), int, float, path (Strings with slashes), uuid.
def animal_details(animal_id):
    # animal = next((animal for animal in animals if animal["id"] == animal_id), None)
    form = EditAnimalForm()
    animal = Animal.query.get(animal_id)
    if animal is None:
        abort(404, description="No animal was Found with the given ID")
    if form.validate_on_submit():
        animal.name = form.name.data
        animal.age = form.age.data
        animal.bio = form.bio.data
        print(form.name.data)
        try:
            db.session.commit()
            print('ok')
        except Exception as e:
            db.session.rollback()
            return render_template("details.html", animal=animal, form=form, message="A animal with this name already exists!")
        print('ok2')
    return render_template("details.html", animal=animal, form=form)

@app.route("/delete/<int:animal_id>")
def delete_animal(animal_id):
    animal = Animal.query.get(animal_id)
    if animal is None:
        abort(404, description="No Pet was Found with the given ID")
    db.session.delete(animal)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
    animals = Animal.query.all()
    return render_template("home.html", animals=animals)


if __name__ == "__main__":
    app.run()
