## ws_MercadoLibre


### **Description**

ws_MercadoLibre is a Python-based web scraping tool designed specifically for extracting data from MercadoLibre.com. It simplifies the process of retrieving information such as pricing, product details, and the rating from a specific item on the MercadoLibre platform.


### **Key Features**

* Customizable Data Extraction: Specify the item you're interested in, and ws_MercadoLibre will retrieve the relevant data for you.
* Python-based Scraping: Utilizes popular libraries such as BeautifulSoup4, Requests, and Flask for efficient and accurate scraping.
* Dockerized Environment: Offers seamless deployment and scalability with Docker integration.
* Collaborative Development: Developed by a team of experienced data engineers—Braulio, Frank, and Carlos—benefiting from diverse expertise and collaborative efforts.


### **Technologies Used**

- **Python**: Versatile and easy to learn programming language.
    - **Modules**:

         - **BeautifulSoup4**: Python library to extract data from HTML and XML.

         - **Requests**: Python library to perform HTTP requests. \
         
         - **Flask**: Lightweight Python framework for creating web applications \
         
         - **httpio**: Python library that allows you to access files served over HTTP as file-like objects

- **Docker**: Platform for creating, deploying and running containerized applications.

### **Installation**

* Clone the repository.
* Open Docker and make sure that the Docker engine has started.
* Open the terminal in the repository folder.
* Run the following commands:

    * `docker compose up --build`

* Now you can do requests to the api by sending a json with the following format:
    * {"url" : "https://www.your_mercadolibre_url.com.mx/"} 
    * It is important to mention that the URL is associated to the specific MercadoLibre product from which you want to extract its information.
    * You can do requests using any application that allows testing of web APIs.
* To finish the program you can run in the same terminal:
    * `docker compose down`

### Additional Information

If you are not familiar with Docker, Python or any other tools mentioned before. You can visit the following websites:

- [Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

- [Get started with Docker](https://www.docker.com/get-started/)

- [Download Python](https://www.python.org/downloads/)

- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

- [Requests Documentation](https://requests.readthedocs.io/en/latest/)

- [Flask Documentation](https://flask.palletsprojects.com/en/3.0.x/)

### **Functions/Methods**

For debugging or modification of the program we share with you the functionality of each of the methods inside our class.

* **init()**

   - This is the special method which gets called when an object of a class is instantiated. This method is used to initialize the attributes of an object.

* **increase_page(search_url)**

   - This method increases the value in the base URL by 50. Takes in the URL and returns the modified URL.

* **title_scrap(url_objeto)**

   - Scrapes the title of the product page. Takes in the URL and returns the title as a string.

* **price_scrap(url_objeto)**

   - Scrapes the price of the product page. Takes in the URL and returns a list of string(s) representing the price.


   - In the scraped webpage, if there are two prices present it returns both; if there is only one price it returns that one; if there are no prices it returns None.

* **rating_scrap(url_objeto)**

   - Scrapes the average rating of the product. Takes in the URL and returns the average rating as a string.


​      If there are no ratings, it returns None.



* **images_scrap(url_objeto)**

   - Scrapes Links to the product images. Takes in the URL and returns a list with links to the product images.

* **provider_scrap(url_objeto)**

   - Scrapes provider's name. Takes in the URL and returns the name of the provider as a string.

* **description_scrap(url_objeto)**

   - Scrapes the product description. Takes in the URL and returns the text of the description as a string.

     If there are no descriptions, it returns None.



* **data_scrap(url_objeto)**

   - This function collects the scraped data of title, prices, images, rating, provider, and description from the other methods and returns this data as a dictionary.

* **scrap_all()**

   - This function collects all the data of each product item on the page and stores it in JSON format.


   - It collects the URLs of each item, scrapes the data for each link, and stores this in a single dictionary.

* **write_soup_to_file(url_objeto, file_name)**

   - This function writes the data from soup (BeautifulSoup object) into a file. It takes an URL and a filename, and writes the complete HTML text of the webpage into a file.


​      If the file already exists, it does not overwrite the file.


### Collaborators

- [Francisco Chan](https://github.com/Frank3040)
- [Braulio Pérez](https://github.com/BraulioPerez)
    - [Youtube](https://www.youtube.com/@BraulioPerez-Code)
- [Carlos Helguera](https://github.com/DeathSpain7)