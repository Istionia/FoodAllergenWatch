# routes.py
from flask import Blueprint, render_template, request
from .models import User, Item
from data.fetch_edamam import fetch_edamam_recipes
from data.fetch_ninjas import fetch_ninjas_recipes
from .utils import check_for_allergens, analyze_country_cuisine

main = Blueprint('main', __name__)

@main.route('/')
def index():
    users = User.query.all()
    items = Item.query.all()
    return render_template('index.html', users=users, items=items)

@main.route('/edamam_recipes', methods=['GET'])
def edamam_recipes():
    query = request.args.get('query', 'chicken')
    recipes = fetch_edamam_recipes(query)
    return render_template('recipes.html', recipes=recipes)

@main.route('/ninjas_recipes', methods=['GET'])
def ninjas_recipes():
    query = request.args.get('query', 'chicken')
    recipes = fetch_ninjas_recipes(query)
    return render_template('recipes.html', recipes=recipes)

@main.route('/allergen-check', methods=['GET'])
def allergen_check():
    query = request.args.get('q')
    country = request.args.get('country')
    if not query:
        return render_template('allergen_check.html', percentage=None, query="", country=country)
    recipes = fetch_edamam_recipes(query, country) + fetch_ninjas_recipes(query)
    total_recipes = len(recipes)
    if total_recipes == 0:
        percentage = 0
    else:
        recipes_with_allergens = sum(
            1 for recipe in recipes if check_for_allergens(recipe.get('ingredientLines', []))
        )
        percentage = (recipes_with_allergens / total_recipes) * 100
    return render_template('allergen_check.html', percentage=percentage, query=query, country=country)

@main.route('/cuisine_analysis', methods=['GET'])
def cuisine_analysis():
    country = request.args.get('country', 'italy')
    allergen_distribution = analyze_country_cuisine(country)
    return render_template('cuisine_analysis.html', country=country, allergen_distribution=allergen_distribution)