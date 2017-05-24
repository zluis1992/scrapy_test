from selenium import webdriver

path_to_chromedriver = "chromedriver\chromedriver.exe"
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

#aca escogemos la pagina que queremos hacer usar scraping
url = 'https://www.youtube.com/'
browser.get(url)

browser.find_element_by_id('masthead-search-term').clear()
browser.find_element_by_id('masthead-search-term').send_keys('Maluma')
browser.find_element_by_id('masthead-search-term').send_keys(u'\ue007')

resultado = []
resultado2 = []

resultado = browser.find_elements_by_css_selector('.yt-uix-tile-link.yt-ui-ellipsis.yt-ui-ellipsis-2.yt-uix-sessionlink.spf-link')

#para imprimir un elemento de la lista de resultados que obtuvimos
#for p in resultado : print p.get_attribute('title')
 	


#aca simplemente tomamos un elemento del que tenemos y lo volvemos a mandar a buscarlo
browser.find_element_by_id('masthead-search-term').clear()
browser.find_element_by_id('masthead-search-term').send_keys(resultado[4].get_attribute('title'))
browser.find_element_by_id('masthead-search-term').send_keys(u'\ue007')


#aca el resultado que nos dio le damos clic al primer video que aparece en la lista para reproducirlo.
resultado2 = browser.find_elements_by_css_selector('.yt-uix-tile-link.yt-ui-ellipsis.yt-ui-ellipsis-2.yt-uix-sessionlink.spf-link')
resultado2[0].click()

