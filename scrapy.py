from selenium import webdriver

import time
import platform
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException

plataforma = platform.system()

if plataforma == "Darwin":
	path_to_chromedriver = "chromedriver/chromedriver"
elif plataforma == "Windows":
	path_to_chromedriver = "chromedriver\chromedriver.exe"


browser = webdriver.Chrome(executable_path = path_to_chromedriver)

#aca escogemos la pagina que queremos hacer usar scraping
url = 'https://www.youtube.com/'
browser.get(url)

#le damos clic al boton de acceder
browser.implicitly_wait(10000) # seconds
wait = WebDriverWait(browser, 1000)
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.yt-uix-button.yt-uix-button-size-default.yt-uix-button-primary')))
browser.find_element_by_css_selector('.yt-uix-button.yt-uix-button-size-default.yt-uix-button-primary').click()

#escribimos el email y le damos en siguiente.
browser.find_element_by_id('identifierId').send_keys('sevequeesfalso1@gmail.com')
browser.find_element_by_id('identifierNext').click()


#esperamos que cargue el form del password y luego los digitamos y damos enter.
wait = WebDriverWait(browser, 1000)
element = wait.until(EC.element_to_be_clickable((By.ID, 'passwordNext')))
time.sleep(0.5)
browser.find_element_by_css_selector('.whsOnd.zHQkBf').click()
browser.find_element_by_css_selector('.whsOnd.zHQkBf').send_keys('#NoTengoNada123')
browser.find_element_by_css_selector('.whsOnd.zHQkBf').send_keys(u'\ue007')

#esperamos que logee y que cargue la pagina, luego damos clic y escribimos lo que deseamos buscar.
wait = WebDriverWait(browser, 1000)
element = wait.until(EC.element_to_be_clickable((By.ID, 'masthead-search-term')))
browser.find_element_by_id('masthead-search-term').click()
browser.find_element_by_id('masthead-search-term').clear()
browser.find_element_by_id('masthead-search-term').send_keys('shakiraVEVO')
browser.find_element_by_id('masthead-search-term').send_keys(u'\ue007')

#declaramos estas listas, que es donde se guardaran los videos.
resultado = []
resultado2 = []

#esperamos que cargue la lista de resultados y la guardamos en la list resultado.
wait = WebDriverWait(browser, 1000)
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.yt-uix-tile-link.yt-ui-ellipsis.yt-ui-ellipsis-2.g-hovercard.yt-uix-sessionlink.spf-link')))
#esta linea de abajo usa elements para traer muchos resultados a una lista.
#resultado = browser.find_elements_by_css_selector('.yt-uix-tile-link.yt-ui-ellipsis.yt-ui-ellipsis-2.yt-uix-sessionlink.spf-link')
browser.find_element_by_css_selector('.yt-uix-tile-link.yt-ui-ellipsis.yt-ui-ellipsis-2.g-hovercard.yt-uix-sessionlink.spf-link').click()


#para imprimir un elemento de la lista de resultados que obtuvimos
#for p in resultado : print p.get_attribute('title')
wait = WebDriverWait(browser, 1000)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="channel-navigation-menu"]/li[2]/a/span'))) 	


#aca le doy clic al boton subscribirse, se debe ahora para pruebas anular la subscripcion antes de volver a correr el script

try:
	browser.find_element_by_css_selector('.subscribe-label').click()
except ElementNotVisibleException:
	print('entre al boton que esta ya subscrito')


#browser.find_element_by_css_selector('.subscribe-label').click()
time.sleep(1) #segundos
browser.find_element_by_xpath('//*[@id="channel-navigation-menu"]/li[2]/a/span').click()

wait = WebDriverWait(browser, 1000)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="browse-items-primary"]/li[1]/button[1]'))) 	
browser.find_element_by_xpath('//*[@id="browse-items-primary"]/li[1]/button[1]').click()
browser.find_element_by_xpath('//*[@id="body"]/ul/li/span').click()

for x in xrange(1, 5):
	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(0.5)

resultado = browser.find_elements_by_css_selector('.yt-uix-sessionlink.yt-uix-tile-link.spf-link.yt-ui-ellipsis.yt-ui-ellipsis-2')

#este para se hizo para poder guardar todas los href de todos los videos.
for x in resultado:
	resultado2.append(x.get_attribute('href'))

for p in resultado2 :
	#print p.get_attribute('title')

	#browser.get(p.get_attribute('href'))
	browser.get(p)
	wait = WebDriverWait(browser, 1000)
	element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.watch-view-count')))

	for x in xrange(1, 3):
		browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(0.5) #espera un tiempo que sino no carga el cuadro de los comentarios
		browser.execute_script("window.scrollTo(0, 0);")

	# Se da like al video
	try:
		browser.find_element_by_css_selector('.yt-uix-button.yt-uix-button-size-default.yt-uix-button-opacity.yt-uix-button-has-icon.no-icon-markup.like-button-renderer-like-button.like-button-renderer-like-button-unclicked.yt-uix-post-anchor.yt-uix-tooltip').click()
	except ElementNotVisibleException:
		print('Ya se dio like anteriormente')
	
	# Se seleccciona el cuadro de comentarios, se escribe el comentario y se envia
	browser.find_element_by_css_selector('.comment-simplebox-renderer-collapsed-content').click()
	browser.find_element_by_css_selector('.comment-simplebox-text').send_keys('Buen video')
	browser.find_element_by_css_selector('.yt-uix-button.yt-uix-button-size-default.yt-uix-button-primary.yt-uix-button-empty.comment-simplebox-submit.yt-uix-sessionlink').click()
	print browser.find_element_by_id('eow-title').get_attribute('title')
	time.sleep(10) #demora 10 segundos para pasar al proximo video
	

#aca simplemente tomamos un elemento del que tenemos y lo volvemos a mandar a buscarlo
#wait = WebDriverWait(browser, 10000)
#element = wait.until(EC.element_to_be_clickable((By.ID, 'masthead-search-term')))
#browser.find_element_by_id('masthead-search-term').clear()
#browser.find_element_by_id('masthead-search-term').send_keys(resultado[4].get_attribute('title'))
#browser.find_element_by_id('masthead-search-term').send_keys(u'\ue007')


#aca el resultado que nos dio le damos clic al primer video que aparece en la lista para reproducirlo.
#resultado2 = browser.find_elements_by_css_selector('.yt-uix-tile-link.yt-ui-ellipsis.yt-ui-ellipsis-2.yt-uix-sessionlink.spf-link')
#resultado2[0].click()

