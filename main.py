from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()

PROXY = "51.158.68.68:8811" # IP:PORT or HOST:PORT

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)
chrome_options.add_argument('--headless')
chrome_options.add_argument("--incognito")
chrome = webdriver.Chrome(options=chrome_options)



chrome.get("https://lirarate.com")
p_element = chrome.find_element_by_id(id_='latest-buy')

print(p_element.text)

chrome.quit()
