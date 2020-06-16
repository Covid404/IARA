
from selenium import *
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import sys
import time


my_profile = webdriver.FirefoxProfile()
my_profile.set_preference("pref.downloads.disable_button.edit_actions", True)
my_profile.set_preference("browser.helperApps.neverAsk.openFile", 'application/zip')
my_profile.set_preference("browser.download.useDownloadDir", True);

browser = webdriver.Firefox(firefox_profile=my_profile)



#webdriver.FireFoxProfile().profile.setPreference("pref.downloads.disable_button.edit_actions", true);

#browser.get('https://www.sistemas.pa.gov.br/compraspara/public/licitacao_list.xhtml')
#browser.get('http://www.transparencia.pr.gov.br/pte/compras/dispensasInexigibilidade?windowId=e9c')
browser.get('https://www.google.com/search?ei=hPnoXpmCHKjN5OUP4ve20AE&q=aquisi%C3%A7ao+por+dispensa+de+licita%C3%A7ao+parana+covid+19&oq=aquisi%C3%A7ao+por+dispensa+de+licita%C3%A7ao+parana+covid+19&gs_lcp=CgZwc3ktYWIQAzIFCCEQoAE6CAghEBYQHRAeOgUIABCxAzoECAAQQzoFCAAQgwE6AggAOgcIABCxAxBDOgwIABCxAxBDEEYQ-QE6BAgAEAo6CggAELEDEEYQ-QE6BwgAEEYQ-QE6BggAEBYQHjoHCCEQChCgAVD6T1jzlQFgmKABaANwAHgAgAGSBIgBlXySAQsyLTMyLjE2LjMuMZgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwiZ1NXK5obqAhWoJrkGHeK7DRoQ4dUDCAs&uact=5')
#result = browser.find_elements_by_xpath("//ol[@id='rso']/li")[0] #//make a list of results and get the first one
#result.find_element_by_xpath("./div/h3/a").click()# //click its href

results = browser.find_elements_by_xpath('//div[@class="r"]/a/h3')  # finds webresults
results[0].click()



time.sleep(10)
download = browser.find_element_by_id('formPesquisa:lnkDownloadBD')
download.click()
#webdriver.ActionChains(browser).click(download).submit()





#select = browser.find_element_by_name('search_form:entidade_administrativa')
'''
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

'''
