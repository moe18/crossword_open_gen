from selenium import webdriver
import selenium

from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.fleetingimage.com/wij/xyzzy/13-pp.html'

resp = urllib.request.urlopen(url)
soup = BeautifulSoup(resp)

days = []
for link in soup.findAll('a')[:-1]:
    days.append(link.string)


driver = webdriver.Chrome(executable_path=r'/Users/mordechaichabot/Downloads/chromedriver')
driver.get(url)

for day in days:
    link = driver.find_element_by_link_text(str(day))
    try:
        link.click()
    except selenium.common.exceptions.ElementClickInterceptedException:
        pass