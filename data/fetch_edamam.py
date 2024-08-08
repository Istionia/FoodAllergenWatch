import os
# use this to make GET requests
import requests

def fetch_edamam_recipes(query, country=None):
    # Access app ID
    app_id = os.getenv('EDAMAM_APP_ID')
    # Access API key
    api_key = os.getenv('EDAMAM_API_KEY')
    # Access point
    url = ' https://api.edamam.com/api/recipes/v2'
    params = {
        "q": query,
        "type": "public",
        "app_id": app_id,
        "app_key": api_key,
        "cuisineType": country if country else "any",
    }

    response = requests.get(url, params=params)

    # If request was successful...
    if response.status.code == 200:
        # ...Convert to JSON
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
    else:
        print(f"Failed to fetch recipes: {response.status_code}")
        return None


