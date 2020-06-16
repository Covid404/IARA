
from selenium import *
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import sys


browser = webdriver.Firefox()
browser.get('https://www.sistemas.pa.gov.br/compraspara/public/licitacao_list.xhtml')


select = browser.find_element_by_name('search_form:entidade_administrativa')

options = [x.get_attribute('value') for x in select.find_elements_by_tag_name("option")]


print("ESCOLHA UMA OPÇÃO")
for index, option in enumerate(options):
    print(f"{index}: {option}")



select = Select(select)
select.select_by_value(options[96])

element = browser.find_element_by_id('search_form:search_button')
webdriver.ActionChains(browser).click(element).perform()


table_id = browser.find_element_by_id('result_form:list_data')

rows = table_id.find_elements_by_tag_name("tr")

for row in rows:
    col = row.find_elements_by_tag_name('td')[1]
    print(col.text)

#print(element)




#trs = browser.find_elements_by_tag_name("td")

#for tr in trs:
    #print(tr.text)
