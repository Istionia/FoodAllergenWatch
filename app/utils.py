# app/utils.py
from scrapers.scraper_allrecipes import scrape_allrecipes_recipes_by_country
from scrapers.scraper_epicurious import scrape_epicurious_recipes_by_country
from scrapers.scraper_seriouseats import scrape_serious_eats_recipes_by_country

big_9_allergens = [
    "peanut", "tree nut", "milk", "egg", "wheat", 
    "soy", "fish", "shellfish", "sesame"
]

def check_for_allergens(ingredients):
    """
    Checks if any of the ingredients contain the big 9 allergens.
    
    Parameters:
        ingredients (list): A list of ingredient strings.
        
    Returns:
        list: A list of detected allergens.
    """
    detected_allergens = []
    for allergen in big_9_allergens:
        for ingredient in ingredients:
            if allergen in ingredient.lower():
                detected_allergens.append(allergen)
                break
    return detected_allergens

def analyze_country_cuisine(country):
    # Scrape recipes from multiple sources
    allrecipes_recipes = scrape_allrecipes_recipes_by_country(country)
    epicurious_recipes = scrape_epicurious_recipes_by_country(country)
    seriouseats_recipes = scrape_serious_eats_recipes_by_country(country)

    # Combine recipes from all sources
    recipes = allrecipes_recipes + epicurious_recipes + seriouseats_recipes
    allergen_distribution = {}

    # Analyze allergens in the recipes
    for recipe in recipes:
        allergens = check_for_allergens(recipe['ingredients'])
        for allergen in allergens:
            if allergen in allergen_distribution:
                allergen_distribution[allergen] += 1
            else:
                allergen_distribution[allergen] = 1
    
    return allergen_distribution