# app/routes.py

from flask import Blueprint, render_template, request
from . import app
# Import the function for fetching the Edamam API
from data.fetch_edamam import fetch_recipes
from .utils import check_for_allergens

main = Blueprint('main', __name__)

@main.route('/recipes', methods=['GET'])
def recipes():
    # Get the search query from the URL
    query = request.args.get('query', 'chicken') # Default to 'chicken' if no query is provided
    # Fetch the recipes from the API 
    recipes = fetch_recipes(query)
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
    recipes = fetch_recipes(query, country)
    
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


# Register the Blueprint
app.register_blueprint(main)