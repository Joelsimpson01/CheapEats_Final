from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)
Bootstrap(app)


class food_items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_1 = db.Column(db.String(50))
    item_2 = db.Column(db.String(50))
    item_3 = db.Column(db.String(50))
    item_4 = db.Column(db.String(50))
    item_5 = db.Column(db.String(50))
    item_6 = db.Column(db.String(50))
    item_7 = db.Column(db.String(50))
    item_8 = db.Column(db.String(50))
    item_9 = db.Column(db.String(50))
    item_10 = db.Column(db.String(50))


class recipe_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe = db.Column(db.String(50))
    item_1 = db.Column(db.String(50))
    item_2 = db.Column(db.String(50))
    item_3 = db.Column(db.String(50))
    item_4 = db.Column(db.String(50))
    item_5 = db.Column(db.String(50))


class user_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))


# Tells the program what render template to goto under what domain
@app.route('/')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/start')
def start():
    return render_template('start.html')


@app.route('/TutorialPage1')
def tutorial():
    return render_template('Tutorial page 1.html')  # render a template


@app.route('/Recipies')
def recipies():
    return render_template('Recipies.html')  # render a template


@app.route('/Recipies_Instructions')
def recipies_Instructions():
    return render_template('Recipies_Instructions.html')  # render a template

@app.route('/list_updated')
def list_updated():
    oml = recipe_data.query.get(1)
    return render_template('list_updated.html', oml=oml)  # render a template


@app.route('/Recipie_LetsCook')
def recipies_LetsCook():
    return render_template('Recipie_LetsCook.html')  # render a template


@app.route('/List')
def list():
    return render_template('List.html')  # render a template


@app.route('/Favourites')
def favourites():
    return render_template('Favourites.html')  # render a template


@app.route('/loading')
def load():
    return render_template('loading.html')  # render a template


@app.route('/MeatandFish')
def meatandfish():
    meat_items = food_items.query.get(1)
    return render_template('meatitems.html', meat_items=meat_items)  # render a template


@app.route('/DairyandEggs')
def dairy():
    dairy_items = food_items.query.get(2)
    return render_template('dairyandeggs.html', dairy_items=dairy_items)  # render a template


@app.route('/CookingOil')
def welcome8():
    oil_items = food_items.query.get(3)
    return render_template('cookingoil.html', oil_items=oil_items)  # render a template


@app.route('/Sauces')
def sauces():
    sauce_items = food_items.query.get(4)
    return render_template('sauces.html', sauce_items=sauce_items)  # render a template


@app.route('/FruitandVeg')
def fruit():
    fruit_items = food_items.query.get(5)
    return render_template('fruitandveg.html', fruit_items=fruit_items)  # render a template


@app.route('/WheatandGrains')
def wheat():
    wheat_items = food_items.query.get(6)
    return render_template('wheatandgrains.html', wheat_items=wheat_items)  # render a template


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
