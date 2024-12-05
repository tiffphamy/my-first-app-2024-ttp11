# this is the "web_app/routes/drink_routes.py" file...

from flask import Blueprint, render_template
import requests

drink_routes = Blueprint("drink_routes", __name__)

@drink_routes.route("/drinks")
def drinks_list():
    print("DRINKS...")

    url = "https://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Non_Alcoholic"
    response = requests.get(url)

    drinks = []
    if response.status_code == 200:
        drinks_data = response.json()
        drinks = drinks_data.get("drinks", [])[:20]

    for drink in drinks:
        print(f"Drink: {drink.get('strDrink')}")

    return render_template("drinks.html", drinks=drinks)
