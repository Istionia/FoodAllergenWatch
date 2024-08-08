import os
import requests
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)

api_key = os.getenv('NINJAS_API_KEY')

if not api_key:
    raise ValueError("API key not found. Please set the NINJAS_API_KEY environment variable.")

url = "https://api.api-ninjas.com/v1/recipe"

def fetch_ninjas_recipes(query):
    """
    Fetch recipes from the API Ninjas recipe endpoint.

    Args:
        query (str): The search query for recipes.

    Returns:
        Optional[List[Dict[str, str]]]: A list of dictionaries containing recipe details, or None if the request fails.
    """
    headers = {
        "X-Api-Key": api_key
    }
    
    params = {
        "query": query
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        try:
            recipes = response.json()
            formatted_recipes = []
            for recipe in recipes:
                formatted_recipes.append({
                    "name": recipe.get("title"),
                    "ingredients": recipe.get("ingredients"),
                    "instructions": recipe.get("instructions"),
                })
            return formatted_recipes
        except ValueError as e:
            logging.error(f"Error parsing JSON response: {e}")
            return None
    else:
        logging.error(f"Failed to fetch recipes: {response.status_code} - {response.text}")
        return None
