from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

path_to_chromedriver = "chromedriver\chromedriver.exe"
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

#aca escogemos la pagina que queremos hacer usar scraping
url = 'https://www.youtube.com/'
browser.get(url)

#le damos clic al boton de acceder
wait = WebDriverWait(browser, 1000)
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.yt-uix-button.yt-uix-button-size-default.yt-uix-button-primary')))
browser.find_element_by_css_selector('.yt-uix-button.yt-uix-button-size-default.yt-uix-button-primary').click()

#escribimos el email y le damos en siguiente.
browser.find_element_by_id('identifierId').send_keys('sevequeesfalso1@gmail.com')
browser.find_element_by_id('identifierNext').click()


#esperamos que cargue el form del password y luego los digitamos y damos enter.
wait = WebDriverWait(browser, 1000)
element = wait.until(EC.element_to_be_clickable((By.ID, 'passwordNext')))
browser.find_element_by_css_selector('.whsOnd.zHQkBf').click()
browser.find_element_by_css_selector('.whsOnd.zHQkBf').send_keys('#NoTengoNada123')
browser.find_element_by_css_selector('.whsOnd.zHQkBf').send_keys(u'\ue007')

#esperamos que logee y que cargue la pagina, luego damos clic y escribimos lo que deseamos buscar.
wait = WebDriverWait(browser, 1000)
element = wait.until(EC.element_to_be_clickable((By.ID, 'masthead-search-term')))
browser.find_element_by_id('masthead-search-term').click()
browser.find_element_by_id('masthead-search-term').clear()
browser.find_element_by_id('masthead-search-term').send_keys('Shakira')
browser.find_element_by_id('masthead-search-term').send_keys(u'\ue007')

resultado = []
resultado2 = []

#esperamos que cargue la lista de resultados y la guardamos en la list resultado.
wait = WebDriverWait(browser, 1000)
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.yt-uix-tile-link.yt-ui-ellipsis.yt-ui-ellipsis-2.yt-uix-sessionlink.spf-link')))
resultado = browser.find_elements_by_css_selector('.yt-uix-tile-link.yt-ui-ellipsis.yt-ui-ellipsis-2.yt-uix-sessionlink.spf-link')

#para imprimir un elemento de la lista de resultados que obtuvimos
#for p in resultado : print p.get_attribute('title')
 	


#aca simplemente tomamos un elemento del que tenemos y lo volvemos a mandar a buscarlo
wait = WebDriverWait(browser, 1000)
element = wait.until(EC.element_to_be_clickable((By.ID, 'masthead-search-term')))
browser.find_element_by_id('masthead-search-term').clear()
browser.find_element_by_id('masthead-search-term').send_keys(resultado[4].get_attribute('title'))
browser.find_element_by_id('masthead-search-term').send_keys(u'\ue007')


#aca el resultado que nos dio le damos clic al primer video que aparece en la lista para reproducirlo.
resultado2 = browser.find_elements_by_css_selector('.yt-uix-tile-link.yt-ui-ellipsis.yt-ui-ellipsis-2.yt-uix-sessionlink.spf-link')
resultado2[0].click()

