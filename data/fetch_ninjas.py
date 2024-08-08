import os
import requests

api_key = os.getenv('NINJAS_API_KEY')
url = "https://api.api-ninjas.com/v1/recipe"

def fetch_ninjas_recipes(query):
    headers = {
        "X-Api-Key": api_key
    }
    
    params = {
        "query": query
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        recipes = response.json()
        formatted_recipes = []
        for recipe in recipes:
            formatted_recipes.append({
                "name": recipe.get("title"),
                "ingredients": recipe.get("ingredients"),
                "instructions": recipe.get("instructions"),
            })
        return formatted_recipes
    else:
        print(f"Failed to fetch recipes: {response.status_code}")
        return None
