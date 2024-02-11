



class ItemUrlScraper:
    def __init__(self, search_url):
        self.search_url = search_url 

    def increase_page(self, search_url):
        # input = link de búsqueda
        # funcion: aumenta en 50 el valor de la busqueda
        # output = link de busqueda modificado
        print("Increasing page")

        beginning, ending = search_url.split("_", 1)
        pattern = r'\d+'
        modified_ending = re.sub(pattern, lambda match: str(int(match.group()) + 50), ending)

        print("Page increased")
        return beginning + "_" + modified_ending