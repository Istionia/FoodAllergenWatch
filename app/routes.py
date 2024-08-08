# app/routes.py

from flask import Blueprint, render_template, request
from . import app
# Import the function for fetching the Edamam API
from data.fetch_edamam import fetch_edamam_recipes
from data.fetch_ninjas import fetch_ninjas_recipes
from .utils import check_for_allergens
from .utils import analyze_country_cuisine

main = Blueprint('main', __name__)

@main.route('/edamam_recipes', methods=['GET'])
def edamam_recipes():
    # Get the search query from the URL
    query = request.args.get('query', 'chicken') # Default to 'chicken' if no query is provided
    # Fetch the recipes from the API 
    recipes = fetch_edamam_recipes(query)
    # Render the data using a template  
    return render_template('recipes.html', recipes=recipes)

@main.route('/ninjas_recipes', methods=['GET'])
def ninjas_recipes():
    # Get the search query from the URL
    query = request.args.get('query', 'chicken')
    # Fetch the recipes from the API 
    recipes = fetch_ninjas_recipes(query)
    # Render the data using a template
    return render_template('recipes.html', recipes=recipes)

@main.route('/allergen-check', methods=['GET'])
def allergen_check():
    # Get the dish name and country from the query parameters
    query = request.args.get('q')
    country = request.args.get('country')

    # If no query is provided, render the template with default values
    if not query:
        return render_template('allergen_check.html', percentage=None, query="", country=country)

    # Fetch recipes based on the query and country
    recipes = fetch_edamam_recipes(query, country), fetch_ninjas_recipes(query)
    
    # Count the total number of recipes fetched
    total_recipes = len(recipes)
    
    # Initialize the percentage variable
    if total_recipes == 0:
        percentage = 0  # No recipes found
    else:
        # Count the number of recipes that contain allergens
        recipes_with_allergens = sum(
            1 for recipe in recipes if check_for_allergens(recipe.get('ingredientLines', []))
        )
        # Calculate the percentage of recipes containing allergens
        percentage = (recipes_with_allergens / total_recipes) * 100

    # Render the allergen check results in the template
    return render_template('allergen_check.html', percentage=percentage, query=query, country=country)

@main.route('/cuisine_analysis', methods=['GET'])
def cuisine_analysis():
    country = request.args.get('country', 'italy')
    allergen_distribution = analyze_country_cuisine(country)
    
    return render_template('cuisine_analysis.html', country=country, allergen_distribution=allergen_distribution)

# Register the Blueprint
app.register_blueprint(main)