# FoodAllergenWatch

FoodAllergenWatch is a web-based application designed to help users identify potential allergens in recipes from various cuisines. It scrapes recipes from popular websites and uses APIs to provide a comprehensive analysis of allergen presence by dish and country.

## Features

- **Search for Recipes**: Find recipes by dish name and country of origin.
- **Allergen Detection**: Identify common allergens (e.g., nuts, gluten, dairy) in recipes.
- **Data Analysis**: View the percentage of recipes containing specific allergens by country and dish.
- **User-Friendly Interface**: Simple and intuitive web interface for easy navigation and search.

## Project Structure

FoodAllergenWatch/
├── app/
│ ├── init.py
│ ├── models.py
│ ├── routes.py
│ ├── utils.py
│ ├── static/
│ │ ├── css/
│ │ │ └── styles.css
│ │ ├── js/
│ │ │ └── scripts.js
│ ├── templates/
│ │ └── index.html
├── scrapers/
│ ├── init.py
│ ├── scraper_allrecipes.py
│ ├── scraper_epicurious.py
│ ├── scraper_yummly.py
├── data/
│ ├── init.py
│ ├── fetch_edamam.py
│ ├── fetch_spoonacular.py
├── migrations/
├── venv/
├── config.py
├── run.py
├── requirements.txt
├── .env
└── README.md


## Getting Started

### Prerequisites

- Python 3.8+
- `virtualenv`
- PostgreSQL (or any other SQL database)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/FoodAllergenWatch.git
   cd FoodAllergenWatch

2. Set up a virtual environment:

bash

virtualenv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the dependencies:

bash

pip install -r requirements.txt

4. Set up your .env file with the necessary environment variables:

plaintext

SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
EDAMAM_API_KEY=your_edamam_api_key
SPOONACULAR_API_KEY=your_spoonacular_api_key

5. Initialize the database:

bash

    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade

## Running the Application

1. Start the Flask development server:

    bash

python run.py

2. Open your browser and navigate to http://127.0.0.1:5000 to use the application.

### Deploying on Vercel

1. Install the Vercel CLI:

    bash

npm install -g vercel

2. Log in to Vercel:

bash

vercel login

3. Create a vercel.json configuration file in your project root:

json

{
  "version": 2,
  "builds": [
    {
      "src": "run.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/run.py"
    }
  ]
}

4. Deploy the application:

bash

vercel

5. Follow the prompts to complete the deployment. Once deployed, Vercel will provide you with a URL where you can access your application.

# Usage

    Enter the name of a dish and the country of origin in the search form.
    Click "Search" to see the list of potential allergens found in recipes for that dish.

# Contributing

Contributions are welcome! Please follow these steps:

    Fork the repository.
    Create a new branch (git checkout -b feature-branch).
    Make your changes.
    Commit your changes (git commit -am 'Add new feature').
    Push to the branch (git push origin feature-branch).
    Create a new Pull Request.

# License

This project is licensed under the [Cooperative Non-Violent Public License v4](https://scancode-licensedb.aboutcode.org/cooperative-non-violent-4.0.html). See the LICENSE file for details.

# Acknowledgements

    Thanks to the providers of the recipe data and APIs used in this project.
    Inspired by the need for better food allergen awareness.