import os
# use this to make GET requests
import requests

def fetch_edamam_recipes(query, country=None):
    # Access app ID
    app_id = os.getenv('EDAMAM_APP_ID')
    # Access API key
    api_key = os.getenv('EDAMAM_API_KEY')

    # Check if environment variables are set
    if not app_id or not api_key:
        raise ValueError("EDAMAM_APP_ID and EDAMAM_API_KEY must be set as environment variables")

    # Access point
    url = ' https://api.edamam.com/api/recipes/v2'
    params = {
        "q": query,
        "type": "public",
        "app_id": app_id,
        "app_key": api_key,
        "cuisineType": country if country else "any",
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        data = response.json()
        recipes = []
        for hit in data['hits']:
            recipe = hit['recipe']
            recipes.append({
                'label': recipe['label'],
                'source': recipe['source'],
                'url': recipe['url'],
                'image': recipe['image'],
                'ingredientLines': recipe['ingredientLines'],
            })
            
            return recipes
        
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch recipes: {e}")
        return None


