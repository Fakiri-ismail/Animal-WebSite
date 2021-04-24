from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    animals = [{'Image':'1.jpg',
                'Name': 'Nelly',
                'Age': '5 weeks',
                'Bio': 'I am a tiny kitten rescued by the good people at Paws Rescue Center.'},
               {'Image':'2.jpg',
                'Name': 'Yuki',
                'Age': '3 weeks',
                'Bio': 'I am a handsome gentle-cat. I like to dressup in bow ties.'},
               {'Image':'3.jpg',
                'Name': 'Basker',
                'Age': '1 year',
                'Bio': 'I love barking. But, I love my friends more.'}
               ]
    return render_template("home.html", animals=animals)


# Static routing
@app.route("/about")
def about():
    return render_template("about.html")


# Dynamic routing
@app.route('/<int:number>')  # String (default), int, float, path (Strings with slashes), uuid.
def show_square(number):
    return "Square of " + str(number) + " is: " + str(number * number)


if __name__ == "__main__":
    app.run()
