from bs4 import BeautifulSoup
import requests
import html.parser
import lxml


response = requests.get('https://www.mos.ru/pgu/ru/app/dogm/077060701/#step_1')
print(response)
bs = BeautifulSoup(response.text, 'lxml')
itog = bs.find('div', class_="esz-section-block esz-section-2114386")
print(itog)







# class="term term_orient_h fact__yesterday"