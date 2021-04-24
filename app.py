from flask import Flask, render_template, abort

app = Flask(__name__)

animals = [
    {'id':1, 'Name': 'Nelly', 'Age': '5 weeks', 'Bio': 'I am a tiny kitten rescued by the good people.'},
    {'id':2, 'Name': 'Yuki', 'Age': '3 weeks', 'Bio': 'I am a handsome gentle-cat. I like to dressup in bow ties.'},
    {'id':3, 'Name': 'Basker', 'Age': '1 year', 'Bio': 'I love barking. But, I love my friends more.'}
        ]

@app.route("/")
def home():
    return render_template("home.html", animals=animals)


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
