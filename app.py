from operator import contains
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    ua = request.headers.get('User-Agent')
    print(ua)
    if 'mobile' in ua or 'Mobile' in ua:
        return render_template('mobile/home.html', curr_page='Home')
    else:
        return render_template('home.html', curr_page='Home')

@app.route('/recipes')
def recipes():
    ua = request.headers.get('User-Agent')
    print(ua)
    if 'mobile' in ua or 'Mobile' in ua:
        return render_template('mobile/recipes.html', curr_page='Recipes')
    else:
        return render_template('recipes.html', curr_page='Recipes')

@app.route('/stuff')
def stuff():
    ua = request.headers.get('User-Agent')
    print(ua)
    if 'mobile' in ua or 'Mobile' in ua:
        return render_template('mobile/stuff.html', curr_page='Stuff')
    else:
        return render_template('stuff.html', curr_page='Stuff')

@app.route('/about')
def about():
    ua = request.headers.get('User-Agent')
    print(ua)
    if 'mobile' in ua or 'Mobile' in ua:
        return render_template('mobile/about.html', curr_page='About')
    else:
        return render_template('about.html', curr_page='About')

if __name__ == '__main__':
    app.run()