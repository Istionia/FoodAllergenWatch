"""
scraper_seriouseats.py

This module contains a function to scrape recipes from the Serious Eats website based on a specified country.
It retrieves the recipe titles, ingredients, and links to the detailed recipe pages.

Dependencies:
    - requests
    - BeautifulSoup (from bs4)
    - time
    - logging

Usage Example:
    from scraper_seriouseats import scrape_serious_eats_recipes_by_country

    recipes = scrape_serious_eats_recipes_by_country('Italy')
    for recipe in recipes:
        print(recipe['title'], recipe['link'])
"""

import requests
from bs4 import BeautifulSoup
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def scrape_serious_eats_recipes_by_country(country):
    """
    Scrape recipes from Serious Eats by country.

    This function searches for recipes on the Serious Eats website based on the specified country.
    It retrieves the recipe titles, ingredients, and links to the detailed recipe pages.

    Args:
        country (str): The name of the country to search recipes for.

    Returns:
        list: A list of dictionaries, each containing the following keys:
            - 'title' (str): The title of the recipe.
            - 'ingredients' (list): A list of ingredients for the recipe.
            - 'country' (str): The country associated with the recipe.
            - 'link' (str): The URL to the detailed recipe page.
    """
    base_url = "https://www.seriouseats.com/search"
    params = {'term': country.lower()}
    recipes = []

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Failed to retrieve data for {country}: {e}")
        return recipes

    soup = BeautifulSoup(response.text, 'html.parser')
    recipe_elements = soup.find_all('article', class_='card')

    for recipe in recipe_elements:
        try:
            title = recipe.find('h4', class_='heading-content').text.strip()
            link = recipe.find('a', class_='card-asset-link')['href']
            full_link = f"https://www.seriouseats.com{link}"

            # Fetch the detailed recipe page for ingredients
            try:
                recipe_response = requests.get(full_link)
                recipe_response.raise_for_status()
            except requests.RequestException as e:
                logging.error(f"Failed to retrieve recipe page for {title}: {e}")
                continue

            recipe_soup = BeautifulSoup(recipe_response.text, 'html.parser')
            ingredients = recipe_soup.find_all('li', class_='ingredient')
            ingredients_list = [ingredient.text.strip() for ingredient in ingredients]

            recipes.append({
                'title': title,
                'ingredients': ingredients_list,
                'country': country,
                'link': full_link
            })

            # Add a delay to avoid overwhelming the server
            time.sleep(1)

        except AttributeError as e:
            logging.error(f"Error parsing recipe data: {e}")
            continue

    return recipes

