"""
scraper_allrecipes.py

This module provides functionality to scrape recipes from AllRecipes by country.
It fetches the HTML content of the AllRecipes pages, parses the recipe information,
and extracts details such as the recipe title, ingredients, and link to the detailed recipe page.

Functions:
    get_country_url(country): Get the URL suffix for a given country.
    fetch_page_content(url): Fetch the HTML content of a given URL.
    parse_recipes(soup): Parse the HTML soup to extract recipe information.
    fetch_ingredients(link): Fetch the ingredients from a detailed recipe page.
    scrape_allrecipes_recipes_by_country(country): Scrape recipes from AllRecipes by country.

Example usage:
    recipes = scrape_allrecipes_recipes_by_country('italy')
    for recipe in recipes:
        print(recipe['title'])
        print(recipe['ingredients'])
        print(recipe['link'])
        print("---")
"""

import requests
from bs4 import BeautifulSoup

def get_country_url(country):
    """
    Get the URL suffix for a given country.

    Args:
        country (str): The name of the country.

    Returns:
        str: The URL suffix for the country, or None if the country is not supported.
    """
    country_urls = {
        'france': '721/world-cuisine/european/french/',
        'china': '695/world-cuisine/asian/chinese/',
        'mexico': '728/world-cuisine/latin-american/mexican/'
    }
    return country_urls.get(country.lower())

def fetch_page_content(url):
    """
    Fetch the HTML content of a given URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the page, or None if the request fails.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Failed to retrieve data: {e}")
        return None

def parse_recipes(soup):
    """
    Parse the HTML soup to extract recipe information.

    Args:
        soup (BeautifulSoup): The BeautifulSoup object containing the parsed HTML.

    Returns:
        list: A list of dictionaries, each containing recipe information.
    """
    recipes = []
    recipe_cards = soup.find_all('article', class_='fixed-recipe-card')
    
    for card in recipe_cards:
        title_element = card.find('span', class_='fixed-recipe-card__title-link')
        if title_element:
            title = title_element.text.strip()
            link = card.find('a', class_='fixed-recipe-card__title-link')['href']
            ingredients = fetch_ingredients(link)
            recipes.append({
                'title': title,
                'ingredients': ingredients,
                'link': link
            })
    return recipes

def fetch_ingredients(link):
    ingredients = []
    page_content = fetch_page_content(link)
    if page_content:
        recipe_soup = BeautifulSoup(page_content, 'html.parser')
        ingredient_elements = recipe_soup.find_all('span', class_='ingredients-item-name')
        ingredients = [ingredient.text.strip() for ingredient in ingredient_elements]
    return ingredients

def scrape_allrecipes_recipes_by_country(country):
    base_url = "https://www.allrecipes.com/recipes/"
    country_url = get_country_url(country)
    
    if not country_url:
        print(f"Country {country} is not supported.")
        return []
    
    full_url = f"{base_url}{country_url}"
    page_content = fetch_page_content(full_url)
    
    if not page_content:
        return []
    
    soup = BeautifulSoup(page_content, 'html.parser')
    recipes = parse_recipes(soup)
    
    return recipes

# Example usage
if __name__ == "__main__":
    recipes = scrape_allrecipes_recipes_by_country('malaysia')
    for recipe in recipes:
        print(recipe['title'])
        print(recipe['ingredients'])
        print(recipe['link'])
        print("---")