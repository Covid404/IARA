
from selenium import *
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import sys
import time


my_profile = webdriver.FirefoxProfile()
#my_profile.set_preference("pref.downloads.disable_button.edit_actions", True)
my_profile.set_preference("browser.helperApps.neverAsk.openFile", 'application/zip')

#/home/renato/HACKASERPRO/COVIS/scrap/

my_profile.set_preference("browser.download.dir", '/home/renato/HACKASERPRO/COVIS/scrap/')
my_profile.set_preference("browser.download.folderList", 2)
#my_profile.set_preference("browser.download.manager.showWhenStarting", False)
my_profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")
#my_profile.set_preference("browser.download.use_download_dir", True);
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
