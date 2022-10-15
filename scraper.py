import self as self
from bs4 import BeautifulSoup
import requests


class FuelOil():

    """Class that scraping the current fueloil price from the www"""

    def calc_fuel(self):

        """Function that scraping the specific data from https://www.tecson.de """

        url = f'https://www.tecson.de/heizoelpreise.html'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table', attrs={'class': 'line'})
        rows = table.find_all('tr')
        fuel_oil_price_data = rows[0].text.split()
        self.daily_fuel_oil_price = fuel_oil_price_data[4]
        self.unit = fuel_oil_price_data[5]

    def print_price(self):

        """print function for the informations"""

        print("the current price for fuel oil is: ", self.daily_fuel_oil_price, self.unit)




FuelOil.calc_fuel(self)
FuelOil.print_price(self)







