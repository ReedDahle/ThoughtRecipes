from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', curr_page='Home')

@app.route('/recipes')
def recipes():
    return render_template('recipes.html', curr_page='Recipes')

@app.route('/stuff')
def stuff():
    return render_template('stuff.html', curr_page='Stuff')

@app.route('/about')
def about():
    return render_template('about.html', curr_page='About')

if __name__ == '__main__':
    app.run()

## a test change