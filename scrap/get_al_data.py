
from selenium import *
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import sys
import time
import config

my_profile = webdriver.FirefoxProfile()
#my_profile.set_preference("pref.downloads.disable_button.edit_actions", True)
my_profile.set_preference("browser.helperApps.neverAsk.openFile", 'text/csv')

#/home/renato/HACKASERPRO/COVIS/scrap/

my_profile.set_preference("browser.download.dir", config.path)
my_profile.set_preference("browser.download.folderList", 2)
#my_profile.set_preference("browser.download.manager.showWhenStarting", False)
my_profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")
#my_profile.set_preference("browser.download.use_download_dir", True);
browser = webdriver.Firefox(firefox_profile=my_profile)


browser.get('http://transparencia.al.gov.br/despesa/despesas-com-covid19/')



time.sleep(2)

#Driver.Instance.FindElements(By.ClassName("btn"));
test = browser.find_elements_by_class_name('btn')

print(test)

for t in test:
	print(t.text)
	if(t.text == '.csv'):
		t.click()


time.sleep(60)
browser.quit()
#download = browser.find_element_by_id('formPesquisa:lnkDownloadBD')
#download.click()
