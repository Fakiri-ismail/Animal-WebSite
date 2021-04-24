from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Paws Rescue Center 🐾"

# Static routing
@app.route("/about")
def about():
    return "We are a non-profit organization working as an animal rescue. " \
           "We aim to help you connect with the purrfect furbaby for you! " \
           "The animals you find on our website are rescued and rehabilitated animals. " \
           "Our mission is to promote the ideology <<Adopt,don't Shop>>"

# Dynamic routing
@app.route('/square/<int:number>')      # String (default), int, float, path (Strings with slashes), uuid.
def show_square(number):
    return "Square of "+ str(number) +" is: "+ str(number * number)

if __name__ == "__main__":
    app.run()