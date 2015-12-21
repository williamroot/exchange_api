import os
from selenium import webdriver
from pyvirtualdisplay import Display
from api.models import Currency, Exchange
from decimal import Decimal

class Parser(object):
    def get_available_currencies(self):
        """
        Comes the list of available currencies.
        """
        # NOTE: virtual display is required to chromedriver
        display = Display(visible=0, size=(800, 600))
        display.start()
        driver = webdriver.Chrome()
        driver.get('http://pt.fxexchangerate.com/currency-converter.html')
        select = driver.find_element_by_id('sf')
        select_options = select.find_elements_by_tag_name('option')
        currencies = []
        for option in select_options:
            if option.get_attribute('disabled'):
                continue
            currency = Currency.objects.get_or_create(
                    iso_code=option.get_attribute('value').upper(),
                    name=option.text
            )[0]
            currency.name = option.text
            currency.save()
            currencies.append(currency)
        # quit browser and virtual display
        driver.quit()
        display.stop()
        return currencies

    def select_option(self, options, currency):
        """
        Select the option from provided dropdown.
        """
        for option in options:
            if option.get_attribute('value').upper() == currency.iso_code:
                option.click()
                break

    def get_exchange(self, source, target):
        """
        Returns the price of a currency (source) over another (target).
        """
        # NOTE: virtual display is required to chromedriver
        display = Display(visible=0, size=(800, 600))
        display.start()
        driver = webdriver.Chrome()
        driver.get('http://pt.fxexchangerate.com/currency-converter.html')
        # source
        de = driver.find_element_by_id('sf')
        de_opts = de.find_elements_by_tag_name('option')
        self.select_option(de_opts, source)
        # target
        para = driver.find_element_by_id('st')
        para_opts = para.find_elements_by_tag_name('option')
        self.select_option(para_opts, target)
        # get and parse result
        result = driver.find_element_by_id('ft')
        value = result.get_attribute('value').replace(',', '.')
        # quit browser and virtual display
        driver.quit()
        display.stop()
        return Exchange.objects.create(
            source=source,
            target=target,
            value=Decimal(value),
        )
