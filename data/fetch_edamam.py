import os
import requests

def fetch_edamam_recipes(query, country=None):
    """
    Fetch recipes from the Edamam API based on a search query and optional country filter.

    Args:
        query (str): The search query for the recipes.
        country (str, optional): The country cuisine type to filter recipes by. Defaults to None.

    Returns:
        list: A list of dictionaries containing recipe details if the request is successful.
        None: If the request fails.

    Raises:
        ValueError: If the EDAMAM_APP_ID or EDAMAM_API_KEY environment variables are not set.
    """
    # Access app ID
    app_id = os.getenv('EDAMAM_APP_ID')
    # Access API key
    api_key = os.getenv('EDAMAM_API_KEY')

    # Check if environment variables are set
    if not app_id or not api_key:
        raise ValueError("EDAMAM_APP_ID and EDAMAM_API_KEY must be set as environment variables")

    # Access point
    url = 'https://api.edamam.com/api/recipes/v2'
    params = {
        "q": query,
        "type": "public",
        "app_id": app_id,
        "app_key": api_key,
        "cuisineType": country if country else "any",
    }

    try:
        # Make the GET request to the Edamam API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Convert response to JSON
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
        # Handle any exceptions that occur during the request
        print(f"Failed to fetch recipes: {e}")
        return None