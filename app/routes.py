
from app import app
from flask import render_template

@app.route('/')
def index():
    
    favorite_foods = ['ice cream', 'reuben sandwiches', 'east coast pizza', "Mom's Apple Pie", 'Chili']
    return render_template('index.html', favorite_foods=favorite_foods)


@app.route('/favorites')
def favorites():
    return render_template('favorites.html')