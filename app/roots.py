from flask import Blueprint, render_template, request
from . import app
from .utils import analyze_country_cuisine

main = Blueprint('main', __name__)

@main.route('/analyze_cuisine', methods=['GET'])
def analyze_cuisine():
    country = request.args.get('country')
    
    if not country:
        return render_template('analyze_cuisine.html', distribution=None)

    allergen_distribution = analyze_country_cuisine(country)

    return render_template('analyze_cuisine.html', distribution=allergen_distribution)
