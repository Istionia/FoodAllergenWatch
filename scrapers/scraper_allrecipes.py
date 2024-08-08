import requests
from bs4 import BeautifulSoup

def scrape_allrecipes_recipes_by_country(country):
    # Define base URL for recipes
    base_url = "https://www.allrecipes.com/recipes/"

    # Example country URLs - note that all URLs follow a specific pattern, which we'll use to scrape recipes by country or region
    country_urls = {
        'italy': '723/world-cuisine/european/italian/',
        'china': '695/world-cuisine/asian/chinese/',
        'mexico': '728/world-cuisine/latin-american/mexican/'
    }

    # Check if a country is supported
    if country.lower() not in country_urls:
        print(f"Country {country} is not supported.")
        return []
    
    # Construct the full URL
    url = f"{base_url}{country_urls[country.lower()]}"

    # Fetch the page content
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve data for {country}")
        return []
    
    # Parse the page content
    soup = BeautifulSoup(response.text, 'html.parser')

    # List to store the extracted recipe information
    recipes = []

    # Extract relevant data from each recipe card
    for recipe in recipes:
        title = recipe.find('span', class_='fixed-recipe-card__title-link').text.strip()
        ingredients = []
        
        # Note: Ingredients are usually in the recipe's detailed page, not the summary card
        link = recipe.find('a', class_='fixed-recipe-card__title-link')['href']
        
        # Fetch the detailed recipe page
        recipe_response = requests.get(link)
        if recipe_response.status_code == 200:
            recipe_soup = BeautifulSoup(recipe_response.text, 'html.parser')
            ingredient_elements = recipe_soup.find_all('span', class_='ingredients-item-name')
            ingredients = [ingredient.text.strip() for ingredient in ingredient_elements]
        
        # Append the scraped data to the list
        recipes.append({
            'title': title,
            'ingredients': ingredients,
            'country': country,
            'link': link
        })
    
    return recipes

recipes = scrape_allrecipes_recipes_by_country('france')
for recipe in recipes:
    print(recipe['title'])
    print(recipe['ingredients'])
    print(recipe['link'])
    print("---")