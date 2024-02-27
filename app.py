from flask import Flask, request, render_template, session, jsonify
import os
from item_data_scraper import ItemDataScraper



# Creamos una instancia de flask
app = Flask(__name__)

# Define the base function
@app.route('/')
def index():
    return None

# Create an object function that accesses the web page and extracts the info from a MercadoLibre item
@app.route('/object', methods=["POST", "GET"])
def get_data_object():
    # Check if the method is POST
        # Create a json variable named data
        # Select the key for the url
        # Create the object
    # Returns the result of the data_scrap Method
    
    if request.method == "POST":
        data = request.json
        link = data["url"]
        try:
            scraper = ItemDataScraper(link)
            return scraper.data_scrap()
        except Exception as e:
            print(f"the exception was: {e}")
            return None

# Implementation of future features
@app.route('/search')
def get_info_pages():
    pass

# Keeps the program running and selects the port and host for our app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="6000")
    # app.run(debug=True)


