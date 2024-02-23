from flask import Flask, request, render_template, session, jsonify
import os
from item_data_scraper import ItemDataScraper



# Creamos una instancia
app = Flask(__name__)


@app.route('/')
def index():
    return "Hola bro"

@app.route('/object', methods=["POST", "GET"])
def get_data_object():
    
    
    if request.method == "POST":
        
        data = request.json
        link = data["link"]
        
        try:
            scraper = ItemDataScraper(link)
            return scraper.data_scrap()
            
        except Exception as e:
            print(f"the exception was: {e}")
            return None

@app.route('/search')
def get_info_pages():
    pass


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="6000")
    # app.run(debug=True)